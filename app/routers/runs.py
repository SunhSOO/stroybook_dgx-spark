import asyncio
import json

from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import StreamingResponse

from app.models.story import (
    AudioListResponse,
    ImageListResponse,
    StoryRunCreated,
    StoryRunRequest,
    StoryRunStatus,
)
from app.services.run_store import run_store
from app.services.story_service import story_service

router = APIRouter(prefix="/runs", tags=["runs"])


@router.post("", response_model=StoryRunCreated, status_code=202)
async def create_run(
    request: StoryRunRequest,
    background_tasks: BackgroundTasks,
) -> StoryRunCreated:
    record = story_service.create_run()
    background_tasks.add_task(story_service.process_run, record.run_id, request)
    return StoryRunCreated(
        run_id=record.run_id,
        status=record.status,
        progress=record.progress,
        message=record.message,
    )


@router.get("/{run_id}", response_model=StoryRunStatus)
async def get_run_status(run_id: str) -> StoryRunStatus:
    status = run_store.status(run_id)
    if status is None:
        raise HTTPException(status_code=404, detail="run not found")
    return status


@router.get("/{run_id}/images", response_model=ImageListResponse)
async def get_run_images(run_id: str) -> ImageListResponse:
    status = run_store.status(run_id)
    if status is None:
        raise HTTPException(status_code=404, detail="run not found")
    images = status.result.images if status.result else []
    return ImageListResponse(run_id=run_id, images=images)


@router.get("/{run_id}/audio", response_model=AudioListResponse)
async def get_run_audio(run_id: str) -> AudioListResponse:
    status = run_store.status(run_id)
    if status is None:
        raise HTTPException(status_code=404, detail="run not found")
    audio = status.result.audio if status.result else []
    return AudioListResponse(run_id=run_id, audio=audio)


@router.get("/{run_id}/events")
async def stream_run_events(run_id: str) -> StreamingResponse:
    if run_store.get(run_id) is None:
        raise HTTPException(status_code=404, detail="run not found")

    async def event_generator():
        index = 0
        while True:
            events = run_store.events(run_id, start_index=index)
            for event in events:
                index += 1
                yield _format_sse(event.type, event.model_dump(mode="json"))

            status = run_store.status(run_id)
            if status and status.status in {"completed", "failed"} and not events:
                break

            await asyncio.sleep(0.5)

    return StreamingResponse(event_generator(), media_type="text/event-stream")


def _format_sse(event_name: str, data: dict) -> str:
    return f"event: {event_name}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"
