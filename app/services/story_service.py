from app.clients.image_client import ImageClient
from app.clients.llm_client import LlmClient
from app.clients.tts_client import TtsClient
from app.models.story import StoryResult, StoryRunRequest
from app.services.run_store import RunRecord, RunStore, run_store


class StoryService:
    def __init__(
        self,
        store: RunStore,
        llm_client: LlmClient,
        image_client: ImageClient,
        tts_client: TtsClient,
    ) -> None:
        self._store = store
        self._llm_client = llm_client
        self._image_client = image_client
        self._tts_client = tts_client

    def create_run(self) -> RunRecord:
        return self._store.create()

    async def process_run(self, run_id: str, request: StoryRunRequest) -> None:
        try:
            self._store.update(
                run_id,
                status="running",
                progress=10,
                message="스토리 생성을 시작했습니다.",
                event_type="story_started",
            )
            scenes = await self._llm_client.generate_story(request)

            self._store.update(
                run_id,
                status="running",
                progress=45,
                message="이미지 프롬프트 기반 결과를 준비하고 있습니다.",
                event_type="image_started",
            )
            images = await self._image_client.generate_images(run_id, scenes)

            audio = []
            if request.tts_enabled:
                self._store.update(
                    run_id,
                    status="running",
                    progress=75,
                    message="장면별 음성 결과를 준비하고 있습니다.",
                    event_type="tts_started",
                )
                audio = await self._tts_client.generate_audio(run_id, scenes)

            result = StoryResult(scenes=scenes, images=images, audio=audio)
            self._store.complete(run_id, result)
        except Exception as exc:
            self._store.fail(run_id, str(exc))


story_service = StoryService(
    store=run_store,
    llm_client=LlmClient(),
    image_client=ImageClient(),
    tts_client=TtsClient(),
)
