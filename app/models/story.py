from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


RunStatus = Literal["queued", "running", "completed", "failed"]


class StoryRunRequest(BaseModel):
    era_ko: str = Field(..., min_length=1, examples=["현대"])
    place_ko: str = Field(..., min_length=1, examples=["숲"])
    characters_ko: str = Field(..., min_length=1, examples=["토끼, 다람쥐"])
    topic_ko: str = Field(..., min_length=1, examples=["우정"])
    tts_enabled: bool = True
    scene_count: int = Field(default=4, ge=1, le=8)
    image_count_per_scene: int = Field(default=3, ge=1, le=6)


class Scene(BaseModel):
    scene_number: int
    title_ko: str
    text_ko: str
    emotion_ko: str
    image_prompts_ko: list[str]


class GeneratedImage(BaseModel):
    scene_number: int
    image_number: int
    prompt_ko: str
    status: Literal["placeholder", "generated"] = "placeholder"
    url: str


class GeneratedAudio(BaseModel):
    scene_number: int
    emotion_ko: str
    status: Literal["placeholder", "generated"] = "placeholder"
    url: str


class StoryResult(BaseModel):
    scenes: list[Scene]
    images: list[GeneratedImage]
    audio: list[GeneratedAudio]


class StoryRunCreated(BaseModel):
    run_id: str
    status: RunStatus
    progress: int
    message: str


class RunEvent(BaseModel):
    type: str
    progress: int
    message: str
    created_at: datetime


class StoryRunStatus(BaseModel):
    run_id: str
    status: RunStatus
    progress: int
    message: str
    created_at: datetime
    updated_at: datetime
    result: StoryResult | None = None
    error: str | None = None


class ImageListResponse(BaseModel):
    run_id: str
    images: list[GeneratedImage]


class AudioListResponse(BaseModel):
    run_id: str
    audio: list[GeneratedAudio]


class TranscriptionResponse(BaseModel):
    text_ko: str
    engine: str
    status: Literal["placeholder", "transcribed"] = "placeholder"
