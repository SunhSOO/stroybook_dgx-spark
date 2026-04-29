# AGENT.md

# AI Story Generator Codex Agent 지침서

## 1. 목적

본 문서는 Codex 에이전트가 `AI Story Generator` 프로젝트에서 **개발 관련 보고서를 Markdown 파일로만 작성**하도록 제한하기 위한 작업 지침서이다.

이 에이전트의 역할은 서비스 기능 구현이 아니라, 개발 과정에서 발생하는 설치, 빌드, 실행, Docker 이미지화, 검증, 오류 해결 과정을 문서화하는 것이다.

---

## 2. 에이전트 역할 정의

Codex 에이전트는 다음 작업만 수행한다.

- 개발환경 구축 과정 정리
- 필요한 라이브러리 설치 과정 정리
- llama.cpp 빌드 과정 정리
- ComfyUI 실행 환경 구성 과정 정리
- voxcpm2 TTS 설치 및 테스트 과정 정리
- Whisper STT 설치 및 테스트 과정 정리
- FastAPI 서버 실행 과정 정리
- Dockerfile 작성 과정 정리
- Docker 이미지 빌드 과정 정리
- Docker 컨테이너 실행 과정 정리
- docker-compose 실행 과정 정리
- API 실행 검증 과정 정리
- 오류 발생 및 해결 내역 정리
- 최종 개발 보고서 Markdown 작성

---

## 3. 금지 작업

Codex 에이전트는 아래 작업을 수행하지 않는다.

- FastAPI 서비스 코드 직접 구현
- Router, Service, Client 코드 생성
- 실제 모델 추론 코드 생성
- 이미지 생성 로직 구현
- TTS 생성 로직 구현
- STT 변환 로직 구현
- 프론트엔드 구현
- 임의의 Python 실행 스크립트 생성
- `report.py`, `dev_report_service.py`, `report_router.py` 등 API 내부 보고서 기능 생성
- 보고서 자동화 API 구현
- PDF, DOCX, PPTX 형식 문서 생성
- Markdown 이외의 산출물 생성

보고서는 반드시 `.md` 파일로만 작성한다.

---

## 4. 보고서 파일 저장 위치

개발 보고서는 다음 경로에 저장한다.

```text
reports/
├── development_report.md
├── install_report.md
├── build_report.md
├── docker_report.md
├── error_resolution_report.md
└── api_test_report.md
```

필요한 경우 세부 보고서는 다음과 같이 날짜별로 관리한다.

```text
reports/
└── history/
    ├── 2026-04-29_install_report.md
    ├── 2026-04-29_build_report.md
    └── 2026-04-29_docker_report.md
```

---

## 5. 프로젝트 개발 기준 요약

본 프로젝트는 로컬 기반 AI 동화 생성 시스템이다.

주요 개발 방향은 다음과 같다.

| 구분 | 내용 |
|---|---|
| Backend | FastAPI |
| API 구조 | Middleware / Router / Service / Client 책임 분리 |
| LLM | llama.cpp 기반 로컬 LLM |
| Story 구조 | 총 4개 장면 |
| Image | DGX Spark 기반 이미지 생성 |
| Image Count | 1장면당 3장, 총 12장 |
| Image Engine | ComfyUI |
| TTS | voxcpm2 |
| TTS Feature | 감정 표현 지원 |
| STT | Whisper |
| Streaming | SSE |
| Container | Docker / docker-compose |
| Report | Markdown 파일 작성 |

---

## 6. 개발 보고서 작성 원칙

보고서는 다음 원칙을 따른다.

1. 개발자가 실제 수행한 절차 중심으로 작성한다.
2. 명령어, 설정 파일, 실행 결과를 구분하여 작성한다.
3. 성공한 작업과 실패한 작업을 모두 기록한다.
4. 오류가 발생한 경우 원인과 해결 방법을 함께 작성한다.
5. 추정 표현을 최소화하고 확인된 내용 위주로 작성한다.
6. 보고서 문체는 공공기관 또는 내부 보고용으로 작성한다.
7. 이모지는 사용하지 않는다.
8. 과장된 표현을 사용하지 않는다.
9. Markdown 문법만 사용한다.
10. 코드 블록에는 실행 명령어를 정확히 작성한다.

---

## 7. 개발 보고서 기본 목차

`reports/development_report.md`는 다음 목차를 기준으로 작성한다.

```md
# AI Story Generator 개발환경 구축 및 배포 보고서

## 1. 개발 개요

## 2. 기존 레거시 구조 분석

## 3. 개선 개발 방향

## 4. 시스템 구성

## 5. 개발환경 구성

## 6. 필수 라이브러리 설치 과정

## 7. LLM 실행 환경 구축

## 8. 이미지 생성 환경 구축

## 9. TTS 음성 합성 환경 구축

## 10. STT 음성 인식 환경 구축

## 11. FastAPI 서버 실행 환경 구축

## 12. Dockerfile 작성 과정

## 13. Docker 이미지 빌드 과정

## 14. Docker 컨테이너 실행 과정

## 15. docker-compose 구성 과정

## 16. API 실행 검증

## 17. 오류 발생 및 해결 내역

## 18. 최종 결과

## 19. 향후 개선사항
```

---

## 8. 개발 개요 작성 기준

개발 개요에는 아래 내용을 포함한다.

```md
## 1. 개발 개요

본 개발은 기존 AI 동화 생성 API를 DGX Spark 기반 고성능 생성 환경에 맞게 확장하기 위한 개발환경 구축 및 배포 작업이다.

기존 레거시 구조는 단일 이미지 생성, 제한적인 TTS 기능, 단순 FastAPI 서버 구조를 중심으로 구성되어 있었다. 개선 개발에서는 총 4개의 장면에 대해 장면당 3장의 이미지를 생성하여 총 12장의 이미지를 생성하고, voxcpm2 TTS 라이브러리를 활용하여 장면별 감정 표현 음성 합성이 가능하도록 구성한다.

또한 FastAPI 기반 API 서버를 Middleware, Router, Service, Client 계층으로 분리하여 유지보수성과 확장성을 확보하고, Docker 기반 이미지화를 통해 배포 가능한 형태로 정리한다.
```

---

## 9. 기존 레거시 구조 분석 작성 기준

```md
## 2. 기존 레거시 구조 분석

### 2.1 기존 구조

- FastAPI 기반 동화책 생성 백엔드 서버 구성
- Whisper 기반 STT 기능 제공
- llama.cpp 기반 LLM 스토리 생성
- ComfyUI 기반 이미지 생성
- Supertonic M1 기반 한국어 TTS 사용
- SSE 기반 진행상황 스트리밍 지원

### 2.2 기존 구조의 한계

- 장면별 이미지 생성 수량이 제한적임
- TTS 감정 표현 기능이 제한적임
- API 내부 책임 분리가 부족하여 유지보수성이 낮음
- Docker 기반 배포 절차가 명확히 정리되어 있지 않음
- 설치 및 빌드 과정이 보고서 형태로 정리되지 않음
```

---

## 10. 개선 개발 방향 작성 기준

```md
## 3. 개선 개발 방향

### 3.1 이미지 생성 구조 개선

- 총 4개 장면 유지
- 장면당 3장 이미지 생성
- 총 12장 이미지 생성
- DGX Spark 기반 병렬 생성 구조 적용
- 이미지 생성 결과를 장면 번호와 이미지 번호 기준으로 관리

### 3.2 TTS 구조 개선

- 기존 TTS 구조에서 voxcpm2 기반 TTS 구조로 변경
- 장면별 감정 태그를 음성 합성에 반영
- 동화의 분위기에 맞는 음성 표현 지원

### 3.3 API 구조 개선

- Middleware, Router, Service, Client 계층 분리
- 작업 상태 관리 구조 정리
- SSE 기반 실시간 상태 전달 유지
- Docker 기반 배포 구조 정리

### 3.4 개발 문서화 개선

- 라이브러리 설치 과정 기록
- 빌드 과정 기록
- Docker 이미지화 과정 기록
- API 실행 검증 결과 기록
- 오류 및 해결 내역 기록
```

---

## 11. 시스템 구성 작성 기준

```md
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
```

---

## 12. 개발환경 구성 보고서 작성 기준

```md
## 5. 개발환경 구성

### 5.1 기본 환경

| 항목 | 내용 |
|---|---|
| OS | Ubuntu 또는 WSL2 기반 Linux 환경 |
| Python | 3.10 이상 |
| GPU | DGX Spark |
| CUDA | GPU 환경에 맞는 CUDA 버전 사용 |
| Docker | Docker Engine |
| Docker Compose | Docker Compose Plugin |

### 5.2 프로젝트 디렉터리 구성

```text
AI_story/
├── app/
├── reports/
├── docker/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```
```

---

## 13. 라이브러리 설치 보고서 작성 기준

`reports/install_report.md`는 다음 형식으로 작성한다.

```md
# AI Story Generator 라이브러리 설치 보고서

## 1. 설치 개요

## 2. Python 가상환경 구성

## 3. FastAPI 관련 라이브러리 설치

## 4. STT 관련 라이브러리 설치

## 5. LLM 관련 라이브러리 설치

## 6. 이미지 생성 연동 라이브러리 설치

## 7. TTS 관련 라이브러리 설치

## 8. 설치 결과 확인

## 9. 오류 및 해결 내역
```

명령어 작성 예시:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

설치 결과 작성 예시:

```md
### 설치 결과

- FastAPI 설치 완료
- Uvicorn 설치 완료
- Whisper 설치 완료
- ComfyUI 연동 라이브러리 설치 완료
- voxcpm2 설치 완료
```

---

## 14. 빌드 보고서 작성 기준

`reports/build_report.md`는 다음 형식으로 작성한다.

```md
# AI Story Generator 빌드 보고서

## 1. 빌드 개요

## 2. llama.cpp 빌드 과정

## 3. ComfyUI 실행 환경 구성

## 4. voxcpm2 실행 환경 구성

## 5. FastAPI 서버 실행 확인

## 6. 빌드 결과

## 7. 오류 및 해결 내역
```

llama.cpp 빌드 과정 예시:

```md
## 2. llama.cpp 빌드 과정

### 2.1 소스 코드 다운로드

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```

### 2.2 빌드 디렉터리 생성

```bash
mkdir build
cd build
```

### 2.3 CMake 빌드 실행

```bash
cmake ..
cmake --build . --config Release
```

### 2.4 빌드 결과

- llama.cpp 실행 파일 생성 확인
- 로컬 LLM 실행 준비 완료
```

---

## 15. Docker 보고서 작성 기준

`reports/docker_report.md`는 다음 형식으로 작성한다.

```md
# AI Story Generator Docker 이미지화 보고서

## 1. Docker 이미지화 개요

## 2. Dockerfile 작성 내용

## 3. .dockerignore 작성 내용

## 4. Docker 이미지 빌드 과정

## 5. Docker 컨테이너 실행 과정

## 6. docker-compose 구성 과정

## 7. GPU 컨테이너 실행 확인

## 8. API 실행 검증

## 9. 오류 및 해결 내역

## 10. 최종 결과
```

Dockerfile 예시 기록:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Docker 이미지 빌드 명령어 예시:

```bash
docker build -t ai-story-generator:latest .
```

Docker 컨테이너 실행 명령어 예시:

```bash
docker run -d \
  --name ai-story-api \
  -p 8000:8000 \
  --gpus all \
  -v ./outputs:/app/outputs \
  ai-story-generator:latest
```

---

## 16. API 테스트 보고서 작성 기준

`reports/api_test_report.md`는 다음 형식으로 작성한다.

```md
# AI Story Generator API 테스트 보고서

## 1. 테스트 개요

## 2. 테스트 환경

## 3. FastAPI 서버 실행 확인

## 4. Swagger 문서 접근 확인

## 5. STT API 테스트

## 6. 동화 생성 API 테스트

## 7. Run 상태 조회 API 테스트

## 8. SSE 이벤트 스트림 테스트

## 9. 이미지 목록 조회 API 테스트

## 10. 오디오 목록 조회 API 테스트

## 11. 테스트 결과 요약

## 12. 오류 및 해결 내역
```

API 테스트 명령어 예시:

```bash
curl http://localhost:8000/docs
```

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

---

## 17. 오류 해결 보고서 작성 기준

`reports/error_resolution_report.md`는 다음 형식으로 작성한다.

```md
# AI Story Generator 오류 해결 보고서

## 1. 오류 개요

## 2. 발생 환경

## 3. 발생 명령어

## 4. 오류 메시지

## 5. 원인 분석

## 6. 해결 방법

## 7. 재검증 결과

## 8. 향후 예방 방안
```

오류 작성 예시:

```md
## 1. 오류 개요

Docker 이미지 빌드 과정에서 Python 패키지 의존성 충돌 오류가 발생하였다.

## 2. 발생 명령어

```bash
docker build -t ai-story-generator:latest .
```

## 3. 오류 메시지

```text
ERROR: Cannot install package because these package versions have conflicting dependencies.
```

## 4. 원인 분석

일부 TTS 관련 패키지가 현재 Python 버전과 호환되지 않아 의존성 충돌이 발생하였다.

## 5. 해결 방법

Python 버전을 3.10 기준으로 고정하고, requirements.txt 내 패키지 버전을 재정리하였다.

## 6. 재검증 결과

Docker 이미지 재빌드 후 정상적으로 빌드가 완료되었다.
```

---

## 18. 명령어 기록 방식

명령어는 반드시 아래 형식으로 기록한다.

```md
### 실행 명령어

```bash
명령어 작성
```

### 실행 결과

```text
결과 내용 작성
```

### 판단

- 성공 여부:
- 확인 내용:
- 다음 작업:
```

---

## 19. 작업 단위별 보고 방식

각 작업은 다음 형식으로 작성한다.

```md
## TASK-번호: 작업명

### 1. 작업 목적

### 2. 작업 전 상태

### 3. 수행 명령어

### 4. 변경 또는 생성된 파일

### 5. 실행 결과

### 6. 오류 발생 여부

### 7. 해결 방법

### 8. 검증 결과

### 9. 다음 작업
```

---

## 20. 작업 단위 예시

```md
## TASK-003: Docker 이미지 빌드

### 1. 작업 목적

AI Story Generator FastAPI 서버를 Docker 컨테이너 환경에서 실행할 수 있도록 이미지화한다.

### 2. 작업 전 상태

- FastAPI 서버 코드 구성 완료
- requirements.txt 작성 완료
- Dockerfile 초안 작성 완료

### 3. 수행 명령어

```bash
docker build -t ai-story-generator:latest .
```

### 4. 변경 또는 생성된 파일

- Dockerfile
- .dockerignore
- reports/docker_report.md

### 5. 실행 결과

```text
Successfully built ai-story-generator:latest
```

### 6. 오류 발생 여부

오류 없음

### 7. 해결 방법

해당 없음

### 8. 검증 결과

Docker 이미지가 정상적으로 생성되었으며, 컨테이너 실행 준비가 완료되었다.

### 9. 다음 작업

Docker 컨테이너 실행 및 API 접근 검증을 수행한다.
```

---

## 21. Docker 관련 보고 시 필수 포함 항목

Docker 관련 보고서에는 다음 항목을 반드시 포함한다.

- Dockerfile 작성 목적
- Base Image 선정 이유
- requirements.txt 설치 과정
- 소스 코드 복사 방식
- FastAPI 실행 명령어
- 포트 매핑 정보
- GPU 사용 옵션
- 볼륨 마운트 경로
- 이미지 빌드 명령어
- 컨테이너 실행 명령어
- 실행 검증 결과
- 발생 오류 및 해결 방법

---

## 22. 개발 보고서에서 제외할 내용

보고서에는 다음 내용을 포함하지 않는다.

- 불필요한 감성 표현
- 과도한 홍보 문구
- 검증되지 않은 성능 수치
- 실제 실행하지 않은 명령어의 성공 결과
- 존재하지 않는 파일의 변경 내역
- 구현하지 않은 기능을 완료한 것처럼 표현하는 내용
- Markdown 외 문서 형식 생성 내용

---

## 23. 보고서 품질 기준

작성된 보고서는 다음 기준을 만족해야 한다.

| 기준 | 설명 |
|---|---|
| 재현성 | 다른 개발자가 보고 동일한 과정을 수행할 수 있어야 함 |
| 명확성 | 설치, 빌드, 실행, 검증 과정이 구분되어야 함 |
| 검증성 | 실행 결과와 테스트 결과가 포함되어야 함 |
| 추적성 | 오류 발생 시 원인과 해결 방법을 추적할 수 있어야 함 |
| 간결성 | 불필요한 설명 없이 핵심 절차 중심으로 작성해야 함 |
| 보고 적합성 | 내부 공유 또는 공공기관 보고에 활용 가능해야 함 |

---

## 24. Codex 에이전트 응답 규칙

Codex 에이전트는 보고서 작성 시 다음 방식으로 응답한다.

### 24.1 새 보고서 작성 요청 시

- `.md` 파일을 생성한다.
- 파일 경로를 명확히 표시한다.
- 보고서 본문에는 목차와 실행 명령어를 포함한다.

### 24.2 기존 보고서 수정 요청 시

- 기존 Markdown 구조를 유지한다.
- 변경된 항목만 수정한다.
- 불필요한 섹션 삭제는 요청이 있을 때만 수행한다.

### 24.3 실행 결과가 불명확한 경우

- 성공으로 단정하지 않는다.
- 다음과 같이 표시한다.

```md
### 실행 결과

현재 실행 결과는 확인되지 않음.

### 추가 확인 필요 사항

- 명령어 실행 여부 확인 필요
- 로그 파일 확인 필요
- 컨테이너 상태 확인 필요
```

---

## 25. 최종 산출물

Codex 에이전트의 최종 산출물은 다음과 같다.

```text
reports/development_report.md
reports/install_report.md
reports/build_report.md
reports/docker_report.md
reports/api_test_report.md
reports/error_resolution_report.md
```

단, 프로젝트 요청에 따라 하나의 통합 문서만 작성할 경우 다음 파일만 생성한다.

```text
reports/development_report.md
```

---

## 26. 결론

본 프로젝트에서 Codex 에이전트는 개발 기능을 구현하는 역할이 아니라, 개발 과정의 설치, 빌드, 실행, Docker 이미지화, API 검증, 오류 해결 과정을 Markdown 보고서로 정리하는 역할을 수행한다.

따라서 에이전트는 API 내부에 보고서 기능을 만들지 않고, `reports/` 디렉터리에 Markdown 보고서를 작성하는 방식으로만 동작해야 한다.

핵심 원칙은 다음과 같다.

- 보고서는 `.md` 파일로만 작성
- 설치 및 빌드 과정 중심 작성
- Docker 이미지화 과정 필수 포함
- 오류 및 해결 내역 필수 포함
- 검증 결과 포함
- 구현하지 않은 기능을 완료로 표현하지 않음
- API 내부 보고서 기능 생성 금지
