from app.core.config import settings
from app.models.story import GeneratedImage, Scene


class ImageClient:
    """Stub image client that can be replaced with ComfyUI integration."""

    async def generate_images(self, run_id: str, scenes: list[Scene]) -> list[GeneratedImage]:
        images: list[GeneratedImage] = []
        for scene in scenes:
            for index, prompt in enumerate(scene.image_prompts_ko, start=1):
                images.append(
                    GeneratedImage(
                        scene_number=scene.scene_number,
                        image_number=index,
                        prompt_ko=prompt,
                        url=(
                            f"{settings.output_base_url}/{run_id}/images/"
                            f"scene_{scene.scene_number:02d}_{index:02d}.png"
                        ),
                    )
                )
        return images
