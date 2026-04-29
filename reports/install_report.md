# AI Story Generator 라이브러리 설치 보고서

## 1. 설치 개요

본 보고서는 AI Story Generator 개발환경에서 필요한 라이브러리 설치 과정을 기록하기 위한 문서이다.

현재 저장소에는 `requirements.txt` 파일이 확인되지 않았으며, 실제 라이브러리 설치 명령어는 실행되지 않았다.

## 2. Python 가상환경 구성

### 실행 명령어

```bash
python -m venv .venv
```

### 실행 결과

```text
현재 실행 결과는 확인되지 않음.
```

### 추가 확인 필요 사항

- Python 설치 여부 확인 필요
- Python 버전 확인 필요
- 가상환경 생성 여부 확인 필요

## 3. FastAPI 관련 라이브러리 설치

### 실행 명령어

```bash
pip install fastapi uvicorn
```

### 실행 결과

```text
현재 실행 결과는 확인되지 않음.
```

## 4. STT 관련 라이브러리 설치

Whisper 관련 라이브러리 설치 결과는 현재 확인되지 않았다.

## 5. LLM 관련 라이브러리 설치

llama.cpp 관련 설치 또는 빌드 결과는 현재 확인되지 않았다.

## 6. 이미지 생성 연동 라이브러리 설치

ComfyUI 연동 라이브러리 설치 결과는 현재 확인되지 않았다.

## 7. TTS 관련 라이브러리 설치

voxcpm2 설치 결과는 현재 확인되지 않았다.

## 8. 설치 결과 확인

현재 설치 결과는 확인되지 않았다.

## 9. 오류 및 해결 내역

현재 라이브러리 설치 과정에서 보고된 오류는 없다.

추가 설치 로그가 확보되면 오류 메시지, 원인 분석, 해결 방법, 재검증 결과를 본 항목에 기록한다.

## 10. 실제 서비스 개발 단계 설치 파일 작성

### 10.1 생성된 파일

- `requirements.txt`
- `requirements-dev.txt`

### 10.2 requirements.txt

```text
fastapi>=0.111,<1.0
uvicorn[standard]>=0.30,<1.0
pydantic>=2.7,<3.0
python-multipart>=0.0.9,<1.0
```

### 10.3 requirements-dev.txt

```text
-r requirements.txt
pytest>=8.2,<9.0
httpx>=0.27,<1.0
```

### 10.4 확인 결과

현재 Python 환경에서 `python -m pytest -q` 실행이 가능했으며, 테스트가 통과하였다.

## 11. 외부 엔진 코드 다운로드

### 11.1 작업 목적

실제 LLM, 이미지 생성, TTS 연동을 위해 `llama.cpp`, `ComfyUI`, `VoxCPM` 공식 저장소 코드를 `external/` 하위에 다운로드하였다.

### 11.2 수행 명령어

```bash
git clone --depth 1 https://github.com/ggml-org/llama.cpp.git external/llama.cpp
git clone --depth 1 https://github.com/comfyanonymous/ComfyUI.git external/ComfyUI
git clone --depth 1 https://github.com/OpenBMB/VoxCPM.git external/VoxCPM
```

### 11.3 실행 결과

```text
external/llama.cpp 다운로드 완료
external/ComfyUI 다운로드 완료
external/VoxCPM 다운로드 완료
```

### 11.4 확인된 버전

| 엔진 | ref | commit |
|---|---|---|
| llama.cpp | `refs/heads/master` | `fc2b0053ffe8` |
| ComfyUI | `refs/heads/master` | `fce0398470fe` |
| VoxCPM | `refs/heads/main` | `19b6bf759002` |

### 11.5 변경 또는 생성된 파일

- `external/llama.cpp`
- `external/ComfyUI`
- `external/VoxCPM`
- `.gitignore`
- `.env.example`
- `docs/engine_setup.md`

### 11.6 추가 확인 필요 사항

- llama.cpp 빌드 필요
- ComfyUI 전용 가상환경 및 의존성 설치 필요
- VoxCPM 패키지 설치 필요
- VoxCPM2 모델 가중치 다운로드 필요
- LLM GGUF 모델 다운로드 필요
- ComfyUI checkpoint 모델 다운로드 필요

## 12. VoxCPM 패키지 설치 확인

### 12.1 확인 명령어

```bash
python -m pip show torch voxcpm huggingface_hub modelscope
```

### 12.2 확인 결과

```text
torch 2.9.1+cu130
voxcpm 2.0.2
huggingface_hub 1.10.2
modelscope 1.35.4
```

### 12.3 CUDA 확인

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

```text
2.9.1+cu130
True
NVIDIA GeForce RTX 3080 Ti
```

### 12.4 VoxCPM CLI 확인

```powershell
$env:PYTHONIOENCODING='utf-8'
& "$env:APPDATA\Python\Python312\Scripts\voxcpm.exe" --help
```

```text
VoxCPM CLI 도움말 출력 확인
```

## 13. ComfyUI 의존성 설치 시도

### 13.1 venv 생성 명령어

```bash
python -m venv external\ComfyUI\.venv
```

### 13.2 실행 결과

```text
ensurepip 단계에서 PermissionError 발생
```

### 13.3 글로벌 환경 실행 확인

```bash
python external\ComfyUI\main.py --help
```

```text
ComfyUI 도움말 출력 확인
```

### 13.4 quick test 결과

```bash
python external\ComfyUI\main.py --quick-test-for-ci --cpu --disable-auto-launch --disable-all-custom-nodes
```

```text
ModuleNotFoundError: No module named 'comfy_aimdo'
WARNING: blake3 package not installed
```

### 13.5 의존성 설치 시도

```bash
python -m pip install comfy-aimdo==0.3.0 blake3
```

```text
WinError 10013 네트워크 소켓 권한 오류로 설치 실패
```

## 14. VoxCPM2 모델 가중치 다운로드 시도

### 14.1 실행 명령어

```bash
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='openbmb/VoxCPM2', local_dir='models/VoxCPM2')"
```

### 14.2 실행 결과

```text
httpx.ConnectError: [WinError 10013] 액세스 권한에 의해 숨겨진 소켓에 액세스를 시도했습니다
huggingface_hub.errors.LocalEntryNotFoundError
```

### 14.3 판단

현재 Codex 실행 환경의 네트워크 소켓 권한 제한으로 VoxCPM2 모델 가중치를 다운로드하지 못하였다.
