# AI Story Generator 개발환경 구축 및 배포 보고서

## 1. 개발 개요

본 개발은 기존 AI 동화 생성 API를 DGX Spark 기반 생성 환경에 맞게 확장하기 위한 개발환경 구축 및 배포 절차를 문서화하는 작업이다.

현재 저장소의 `agent.md`는 Codex 에이전트의 역할을 서비스 기능 구현이 아닌 Markdown 개발 보고서 작성으로 제한하고 있다. 따라서 본 보고서는 FastAPI 서비스 코드, Router, Service, Client, 모델 추론 코드, 이미지 생성 로직, TTS 로직, STT 로직을 직접 구현하지 않고, 개발 절차와 검증 기준을 기록하는 용도로 작성한다.

## 2. 기존 레거시 구조 분석

### 2.1 기존 구조

- FastAPI 기반 동화책 생성 백엔드 서버 구성을 목표로 함
- Whisper 기반 STT 기능 제공을 목표로 함
- llama.cpp 기반 LLM 스토리 생성을 목표로 함
- ComfyUI 기반 이미지 생성을 목표로 함
- voxcpm2 기반 감정 표현 TTS 적용을 목표로 함
- SSE 기반 진행상황 스트리밍 지원을 목표로 함

### 2.2 기존 구조의 한계

- 현재 저장소에는 실제 애플리케이션 코드가 확인되지 않음
- 현재 저장소에는 Dockerfile, docker-compose.yml, requirements.txt가 확인되지 않음
- 설치, 빌드, 실행, API 검증 결과 보고서가 아직 작성되지 않음
- 실행 결과를 검증할 수 있는 로그 또는 테스트 결과가 아직 제공되지 않음

## 3. 개선 개발 방향

### 3.1 문서화 기반 개발 진행

- `agent.md`의 보고서 전용 지침 준수
- `reports/` 하위 Markdown 보고서 작성
- 실행하지 않은 작업은 완료로 표시하지 않음
- 확인되지 않은 결과는 추가 확인 필요 사항으로 분리

### 3.2 하네스 엔지니어링 적용

- `reports/harness_engineering_design.md`에 하네스 엔지니어링 설계 작성 완료
- 에이전트가 읽을 수 있는 저장소 문서를 근거로 보고서 작성
- 명령어, 실행 결과, 오류, 재검증 결과를 분리하여 기록

### 3.3 향후 개발 절차

- 개발환경 구성 명령어 확인
- 필수 라이브러리 설치 결과 확인
- llama.cpp, ComfyUI, voxcpm2, Whisper 실행 환경 확인
- FastAPI 서버 실행 결과 확인
- Docker 이미지화 및 컨테이너 실행 결과 확인
- API 실행 검증 결과 확인

## 4. 시스템 구성

| 구성 요소 | 사용 기술 | 역할 |
|---|---|---|
| Backend API | FastAPI | 동화 생성 API 서버 |
| ASGI Server | Uvicorn | FastAPI 실행 서버 |
| LLM | llama.cpp | 4장면 동화 스토리 생성 |
| Image Engine | ComfyUI | 장면별 이미지 생성 |
| Hardware | DGX Spark | 이미지 생성 및 AI 추론 가속 |
| TTS | voxcpm2 | 감정 표현 음성 합성 |
| STT | Whisper | 음성 입력 텍스트 변환 |
| Streaming | SSE | 생성 진행상황 실시간 전달 |
| Container | Docker | 실행 환경 이미지화 |
| Orchestration | docker-compose | 복수 서비스 실행 관리 |
| Report | Markdown | 개발 과정 문서화 |

## 5. 개발환경 구성

### 5.1 기본 환경

| 항목 | 내용 |
|---|---|
| 작업일 | 2026-04-29 |
| 저장소 경로 | `C:\Users\sunhy\Desktop\동화창작DGX-spark` |
| 현재 확인된 파일 | `agent.md`, `README.md`, `reports/harness_engineering_design.md` |
| Python | 현재 확인되지 않음 |
| Docker | 현재 확인되지 않음 |
| GPU | 현재 확인되지 않음 |

### 5.2 현재 저장소 구조

```text
동화창작DGX-spark/
├── README.md
├── agent.md
└── reports/
    └── harness_engineering_design.md
```

## 6. 필수 라이브러리 설치 과정

현재 필수 라이브러리 설치 명령어는 실행되지 않았으며, `requirements.txt` 파일도 확인되지 않았다.

세부 내용은 `reports/install_report.md`에 기록한다.

## 7. LLM 실행 환경 구축

llama.cpp 설치 및 빌드 결과는 현재 확인되지 않았다.

세부 내용은 `reports/build_report.md`에 기록한다.

## 8. 이미지 생성 환경 구축

ComfyUI 실행 환경 구성 결과는 현재 확인되지 않았다.

세부 내용은 `reports/build_report.md`에 기록한다.

## 9. TTS 음성 합성 환경 구축

voxcpm2 설치 및 테스트 결과는 현재 확인되지 않았다.

세부 내용은 `reports/build_report.md` 또는 `reports/install_report.md`에 기록한다.

## 10. STT 음성 인식 환경 구축

Whisper 설치 및 테스트 결과는 현재 확인되지 않았다.

세부 내용은 `reports/install_report.md` 또는 `reports/api_test_report.md`에 기록한다.

## 11. FastAPI 서버 실행 환경 구축

FastAPI 서버 코드와 실행 결과는 현재 확인되지 않았다.

## 12. Dockerfile 작성 과정

Dockerfile은 현재 저장소에서 확인되지 않았다.

세부 내용은 `reports/docker_report.md`에 기록한다.

## 13. Docker 이미지 빌드 과정

Docker 이미지 빌드 명령어는 현재 실행되지 않았다.

세부 내용은 `reports/docker_report.md`에 기록한다.

## 14. Docker 컨테이너 실행 과정

Docker 컨테이너 실행 명령어는 현재 실행되지 않았다.

세부 내용은 `reports/docker_report.md`에 기록한다.

## 15. docker-compose 구성 과정

docker-compose.yml 파일은 현재 저장소에서 확인되지 않았다.

세부 내용은 `reports/docker_report.md`에 기록한다.

## 16. API 실행 검증

API 실행 검증은 현재 수행되지 않았다.

세부 내용은 `reports/api_test_report.md`에 기록한다.

## 17. 오류 발생 및 해결 내역

현재 개발 실행 과정에서 보고된 오류는 없다.

단, PowerShell 콘솔에서 한글 Markdown을 출력할 때 문자 인코딩이 깨져 보이는 현상이 확인되었다. 파일 자체는 UTF-8로 읽을 경우 정상 한글로 확인되었다.

세부 내용은 `reports/error_resolution_report.md`에 기록한다.

## 18. 최종 결과

현재까지 완료된 작업은 다음과 같다.

- `agent.md` 지침 확인
- `reports/harness_engineering_design.md` 확인
- 보고서 전용 개발 진행 범위 확인
- 기본 개발 보고서 작성

## 19. 향후 개선사항

- 개발자가 실제 수행한 설치 명령어 및 실행 로그 확보
- requirements.txt 존재 여부 확인
- Dockerfile 및 docker-compose.yml 작성 여부 확인
- FastAPI 서버 실행 로그 확보
- API 테스트 결과 확보
- 각 단계별 보고서에 확인된 결과 반영

## 20. 실제 서비스 개발 이력

### 20.1 개발 범위

사용자가 실제 서비스 개발 진행을 명시적으로 요청하여 FastAPI 기반 최소 실행 가능 서비스를 구현하였다.

이번 단계에서는 실제 llama.cpp, ComfyUI, voxcpm2, Whisper 엔진을 직접 호출하지 않고, 동일한 API 계약을 검증할 수 있는 placeholder Client 계층을 구성하였다.

### 20.2 생성된 주요 파일

- `app/main.py`
- `app/routers/health.py`
- `app/routers/runs.py`
- `app/routers/stt.py`
- `app/services/story_service.py`
- `app/services/run_store.py`
- `app/clients/llm_client.py`
- `app/clients/image_client.py`
- `app/clients/tts_client.py`
- `app/clients/stt_client.py`
- `app/models/story.py`
- `tests/test_api.py`
- `requirements.txt`
- `requirements-dev.txt`
- `Dockerfile`
- `.dockerignore`
- `docker-compose.yml`
- `.gitignore`

### 20.3 구현된 API

- `GET /health`
- `POST /api/runs`
- `GET /api/runs/{run_id}`
- `GET /api/runs/{run_id}/events`
- `GET /api/runs/{run_id}/images`
- `GET /api/runs/{run_id}/audio`
- `POST /api/stt/transcriptions`

### 20.4 검증 결과

```bash
python -m compileall app tests
```

```text
구문 검증 통과
```

```bash
python -m pytest -q
```

```text
2 passed in 0.27s
```

```text
임시 uvicorn 서버 실행 후 /health 응답 확인
{"status":"ok","app":"AI Story Generator","version":"0.1.0","environment":"local"}
```

### 20.5 다음 작업

- 실제 llama.cpp 클라이언트 연동
- 실제 ComfyUI 이미지 생성 클라이언트 연동
- 실제 voxcpm2 TTS 클라이언트 연동
- 실제 Whisper STT 클라이언트 연동
- Docker 이미지 빌드 및 컨테이너 실행 검증
- DGX Spark GPU 환경 검증
