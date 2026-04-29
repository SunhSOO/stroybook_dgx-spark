from app.core.config import settings
from app.models.story import GeneratedAudio, Scene


class TtsClient:
    """Stub TTS client that can be replaced with voxcpm2 integration."""

    async def generate_audio(self, run_id: str, scenes: list[Scene]) -> list[GeneratedAudio]:
        return [
            GeneratedAudio(
                scene_number=scene.scene_number,
                emotion_ko=scene.emotion_ko,
                url=f"{settings.output_base_url}/{run_id}/audio/scene_{scene.scene_number:02d}.wav",
            )
            for scene in scenes
        ]
