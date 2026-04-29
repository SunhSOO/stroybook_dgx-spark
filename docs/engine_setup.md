# AI Story Generator 외부 엔진 설치 메모

## 1. 개요

실제 서비스 연동을 위해 다음 공식 저장소 코드를 `external/` 하위에 다운로드하였다.

| 엔진 | 로컬 경로 | 용도 | 확인된 ref | 확인된 commit |
|---|---|---|---|---|
| llama.cpp | `external/llama.cpp` | 로컬 LLM 실행 | `refs/heads/master` | `fc2b0053ffe8` |
| ComfyUI | `external/ComfyUI` | 이미지 생성 엔진 | `refs/heads/master` | `fce0398470fe` |
| VoxCPM | `external/VoxCPM` | VoxCPM2 TTS 코드 | `refs/heads/main` | `19b6bf759002` |

`external/`, `models/`, `pretrained_models/` 및 주요 모델 가중치 확장자는 `.gitignore`에 등록하여 GitHub에 업로드하지 않는다.

## 2. 공식 설치 기준

### 2.1 llama.cpp

공식 빌드 문서 기준으로 코드는 다음 명령으로 받는다.

```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
```

CPU 빌드는 CMake를 사용한다.

```bash
cmake -B build
cmake --build build --config Release
```

CUDA 빌드는 NVIDIA CUDA Toolkit이 설치된 환경에서 다음 옵션을 사용한다.

```bash
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release
```

### 2.2 ComfyUI

공식 수동 설치 절차는 가상환경 생성, ComfyUI 저장소 clone, 의존성 설치, 실행 순서로 진행된다. ComfyUI는 별도 Python 환경에서 실행하는 것을 권장한다.

```bash
cd external/ComfyUI
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

GPU용 PyTorch 설치 명령은 실제 CUDA 버전에 맞춰 별도 선택해야 한다.

### 2.3 VoxCPM2

VoxCPM2는 OpenBMB의 VoxCPM 프로젝트에서 제공된다. 패키지 설치명은 `voxcpm`이다.

```bash
pip install voxcpm
```

VoxCPM2 모델은 `openbmb/VoxCPM2`로 로드할 수 있다. 모델 가중치는 약 5GB 수준이므로 코드 저장소와 별도로 `models/` 또는 `pretrained_models/` 하위에 보관한다.

```python
from voxcpm import VoxCPM

model = VoxCPM.from_pretrained("openbmb/VoxCPM2", load_denoiser=False)
```

로컬에 먼저 다운로드할 경우 다음과 같은 구조를 권장한다.

```text
models/
└── VoxCPM2/
```

## 3. 현재 완료 상태

- `external/llama.cpp` 다운로드 완료
- `external/ComfyUI` 다운로드 완료
- `external/VoxCPM` 다운로드 완료
- VoxCPM 패키지 `2.0.2` 설치 확인
- PyTorch `2.9.1+cu130` 및 CUDA 사용 가능 확인
- GPU `NVIDIA GeForce RTX 3080 Ti` 확인
- VoxCPM CLI는 `C:\Users\sunhy\AppData\Roaming\Python\Python312\Scripts\voxcpm.exe`에서 확인
- ComfyUI `main.py --help` 실행 확인
- VoxCPM2 모델 가중치 다운로드는 네트워크 권한 오류로 실패
- ComfyUI 전용 venv 생성은 `ensurepip` 임시 디렉터리 권한 오류로 실패
- ComfyUI quick test는 `comfy_aimdo`, `blake3` 누락으로 실패
- llama.cpp 빌드는 CMake 컴파일러 식별 실패로 완료되지 않음

## 4. 다음 작업

1. CUDA 및 GPU 환경 확인
2. llama.cpp 빌드
3. LLM GGUF 모델 다운로드
4. ComfyUI 전용 가상환경 구성
5. ComfyUI checkpoint 모델 다운로드
6. VoxCPM2 모델 가중치 다운로드
7. FastAPI Client 계층에서 실제 엔진 호출로 전환

## 5. 로컬 PowerShell 재실행 명령

현재 Codex 실행 환경에서는 네트워크 소켓과 일부 임시 디렉터리 권한이 제한되어 다음 명령은 사용자가 로컬 PowerShell에서 직접 실행해야 한다.

### 5.1 ComfyUI 누락 의존성 설치

```powershell
python -m pip install comfy-aimdo==0.3.0 blake3
```

또는 전체 requirements를 다시 설치한다.

```powershell
python -m pip install -r external\ComfyUI\requirements.txt
```

### 5.2 VoxCPM2 모델 가중치 다운로드

```powershell
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='openbmb/VoxCPM2', local_dir='models/VoxCPM2')"
```

### 5.3 VoxCPM CLI 확인

```powershell
$env:PYTHONIOENCODING='utf-8'
& "$env:APPDATA\Python\Python312\Scripts\voxcpm.exe" --help
```

### 5.4 ComfyUI quick test

```powershell
$env:PYTHONIOENCODING='utf-8'
python external\ComfyUI\main.py --quick-test-for-ci --cpu --disable-auto-launch --disable-all-custom-nodes
```

### 5.5 llama.cpp 빌드

Visual Studio 개발자 PowerShell 또는 개발자 명령 프롬프트에서 실행한다.

```powershell
cd external\llama.cpp
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release -j 8
```

## 6. 참고 공식 문서

- llama.cpp build: https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md
- ComfyUI manual install: https://docs.comfy.org/installation/manual_install
- ComfyUI system requirements: https://docs.comfy.org/installation/system_requirements
- VoxCPM installation: https://voxcpm.readthedocs.io/en/latest/installation.html
- VoxCPM GitHub: https://github.com/OpenBMB/VoxCPM
- VoxCPM2 model: https://huggingface.co/openbmb/VoxCPM2
