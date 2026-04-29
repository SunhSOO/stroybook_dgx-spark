from app.models.story import Scene, StoryRunRequest


class LlmClient:
    """Stub LLM client that can be replaced with llama.cpp integration."""

    async def generate_story(self, request: StoryRunRequest) -> list[Scene]:
        scenes: list[Scene] = []
        characters = request.characters_ko
        for index in range(1, request.scene_count + 1):
            emotion = self._emotion_for_scene(index)
            text = (
                f"{request.era_ko}의 {request.place_ko}에서 {characters}는 "
                f"{request.topic_ko}에 대해 배우는 {index}번째 장면을 맞이한다. "
                "서로의 마음을 확인하며 다음 장면으로 이어질 단서를 발견한다."
            )
            prompts = [
                (
                    f"{request.place_ko} 배경의 동화 삽화, {characters}, "
                    f"{request.topic_ko}, 장면 {index}, 이미지 {image_index}"
                )
                for image_index in range(1, request.image_count_per_scene + 1)
            ]
            scenes.append(
                Scene(
                    scene_number=index,
                    title_ko=f"{index}장면: {request.topic_ko}",
                    text_ko=text,
                    emotion_ko=emotion,
                    image_prompts_ko=prompts,
                )
            )
        return scenes

    def _emotion_for_scene(self, scene_number: int) -> str:
        emotions = ["호기심", "긴장", "기쁨", "따뜻함"]
        return emotions[(scene_number - 1) % len(emotions)]
