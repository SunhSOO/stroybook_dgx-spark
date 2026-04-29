from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from threading import RLock
from uuid import uuid4

from app.models.story import RunEvent, RunStatus, StoryResult, StoryRunStatus


def _now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class RunRecord:
    run_id: str
    status: RunStatus
    progress: int
    message: str
    created_at: datetime
    updated_at: datetime
    result: StoryResult | None = None
    error: str | None = None
    events: list[RunEvent] = field(default_factory=list)


class RunStore:
    def __init__(self) -> None:
        self._records: dict[str, RunRecord] = {}
        self._lock = RLock()

    def create(self) -> RunRecord:
        now = _now()
        record = RunRecord(
            run_id=str(uuid4()),
            status="queued",
            progress=0,
            message="작업이 생성되었습니다.",
            created_at=now,
            updated_at=now,
        )
        record.events.append(
            RunEvent(
                type="queued",
                progress=record.progress,
                message=record.message,
                created_at=now,
            )
        )
        with self._lock:
            self._records[record.run_id] = record
        return record

    def update(
        self,
        run_id: str,
        *,
        status: RunStatus,
        progress: int,
        message: str,
        event_type: str,
    ) -> RunRecord:
        with self._lock:
            record = self._get_locked(run_id)
            record.status = status
            record.progress = progress
            record.message = message
            record.updated_at = _now()
            record.events.append(
                RunEvent(
                    type=event_type,
                    progress=progress,
                    message=message,
                    created_at=record.updated_at,
                )
            )
            return record

    def complete(self, run_id: str, result: StoryResult) -> RunRecord:
        with self._lock:
            record = self._get_locked(run_id)
            record.status = "completed"
            record.progress = 100
            record.message = "동화 생성 작업이 완료되었습니다."
            record.result = result
            record.updated_at = _now()
            record.events.append(
                RunEvent(
                    type="completed",
                    progress=100,
                    message=record.message,
                    created_at=record.updated_at,
                )
            )
            return record

    def fail(self, run_id: str, error: str) -> RunRecord:
        with self._lock:
            record = self._get_locked(run_id)
            record.status = "failed"
            record.progress = max(record.progress, 1)
            record.message = "동화 생성 작업이 실패했습니다."
            record.error = error
            record.updated_at = _now()
            record.events.append(
                RunEvent(
                    type="failed",
                    progress=record.progress,
                    message=error,
                    created_at=record.updated_at,
                )
            )
            return record

    def get(self, run_id: str) -> RunRecord | None:
        with self._lock:
            return self._records.get(run_id)

    def status(self, run_id: str) -> StoryRunStatus | None:
        record = self.get(run_id)
        if record is None:
            return None
        return StoryRunStatus(
            run_id=record.run_id,
            status=record.status,
            progress=record.progress,
            message=record.message,
            created_at=record.created_at,
            updated_at=record.updated_at,
            result=record.result,
            error=record.error,
        )

    def events(self, run_id: str, start_index: int = 0) -> list[RunEvent]:
        with self._lock:
            record = self._records.get(run_id)
            if record is None:
                return []
            return list(record.events[start_index:])

    def _get_locked(self, run_id: str) -> RunRecord:
        record = self._records.get(run_id)
        if record is None:
            raise KeyError(f"run not found: {run_id}")
        return record


run_store = RunStore()
