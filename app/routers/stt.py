from fastapi import APIRouter, File, UploadFile

from app.clients.stt_client import SttClient
from app.models.story import TranscriptionResponse

router = APIRouter(prefix="/stt", tags=["stt"])
stt_client = SttClient()


@router.post("/transcriptions", response_model=TranscriptionResponse)
async def transcribe_audio(audio_file: UploadFile = File(...)) -> TranscriptionResponse:
    return await stt_client.transcribe(audio_file)
