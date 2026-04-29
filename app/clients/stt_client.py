from fastapi import UploadFile

from app.models.story import TranscriptionResponse


class SttClient:
    """Stub STT client that can be replaced with Whisper integration."""

    async def transcribe(self, audio_file: UploadFile) -> TranscriptionResponse:
        filename = audio_file.filename or "audio"
        return TranscriptionResponse(
            text_ko=f"{filename} 파일의 음성 인식 결과는 현재 placeholder입니다.",
            engine="whisper-placeholder",
        )
