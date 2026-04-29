# AI Story Generator API 테스트 보고서

## 1. 테스트 개요

본 보고서는 AI Story Generator API 실행 검증 과정을 기록하기 위한 문서이다.

현재 저장소에는 FastAPI 서버 코드가 확인되지 않았으며, API 테스트 명령어는 실행되지 않았다.

## 2. 테스트 환경

| 항목 | 내용 |
|---|---|
| API 서버 | 현재 확인되지 않음 |
| 실행 포트 | 현재 확인되지 않음 |
| 테스트 도구 | curl 사용 예정 |
| 테스트 일자 | 2026-04-29 |

## 3. FastAPI 서버 실행 확인

FastAPI 서버 실행 결과는 현재 확인되지 않았다.

## 4. Swagger 문서 접근 확인

### 실행 명령어

```bash
curl http://localhost:8000/docs
```

### 실행 결과

```text
현재 실행 결과는 확인되지 않음.
```

## 5. STT API 테스트

STT API 테스트 결과는 현재 확인되지 않았다.

## 6. 동화 생성 API 테스트

### 실행 명령어

```bash
curl -X POST http://localhost:8000/api/runs \
  -H "Content-Type: application/json" \
  -d '{
    "era_ko": "현대",
    "place_ko": "숲",
    "characters_ko": "토끼, 다람쥐",
    "topic_ko": "우정",
    "tts_enabled": true,
    "scene_count": 4,
    "image_count_per_scene": 3
  }'
```

### 실행 결과

```text
현재 실행 결과는 확인되지 않음.
```

## 7. Run 상태 조회 API 테스트

Run 상태 조회 API 테스트 결과는 현재 확인되지 않았다.

## 8. SSE 이벤트 스트림 테스트

SSE 이벤트 스트림 테스트 결과는 현재 확인되지 않았다.

## 9. 이미지 목록 조회 API 테스트

이미지 목록 조회 API 테스트 결과는 현재 확인되지 않았다.

## 10. 오디오 목록 조회 API 테스트

오디오 목록 조회 API 테스트 결과는 현재 확인되지 않았다.

## 11. 테스트 결과 요약

현재 API 테스트 결과는 확인되지 않았다.

## 12. 오류 및 해결 내역

현재 API 테스트 과정에서 보고된 오류는 없다.

추가 테스트 로그가 확보되면 오류 메시지, 원인 분석, 해결 방법, 재검증 결과를 본 항목에 기록한다.

## 13. 실제 서비스 개발 단계 API 테스트 결과

### 13.1 테스트 명령어

```bash
python -m pytest -q
```

### 13.2 테스트 결과

```text
2 passed in 0.27s
```

### 13.3 검증된 항목

- `/health` 응답 상태 확인
- `/api/runs` 생성 요청 확인
- `/api/runs/{run_id}` 상태 조회 확인
- 기본 4장면 생성 확인
- 장면당 3장, 총 12개 이미지 결과 확인
- TTS 활성화 시 4개 오디오 결과 확인

### 13.4 추가 확인 필요 사항

- 실제 서버 실행 후 curl 기반 검증
- SSE 스트림 장시간 연결 검증
- STT 파일 업로드 API 검증
- Docker 컨테이너 기반 API 검증

## 14. 임시 서버 실행 검증

### 14.1 실행 방식

PowerShell Job으로 uvicorn 서버를 임시 실행한 뒤 `/health` API를 호출하고 Job을 종료하였다.

### 14.2 검증 결과

```text
{"status":"ok","app":"AI Story Generator","version":"0.1.0","environment":"local"}
```

### 14.3 비고

현재 자동화 실행 환경에서는 장기 실행 백그라운드 서버 프로세스가 유지되지 않아 임시 실행 방식으로 서버 기동을 검증하였다.
