# AI Story Generator 오류 해결 보고서

## 1. 오류 개요

현재 개발 실행 과정에서 보고된 설치, 빌드, Docker, API 오류는 없다.

다만 PowerShell 콘솔에서 `Get-Content`로 한글 Markdown 파일을 출력할 때 문자 인코딩이 깨져 보이는 현상이 확인되었다.

## 2. 발생 환경

| 항목 | 내용 |
|---|---|
| OS | Windows |
| Shell | PowerShell |
| 저장소 경로 | `C:\Users\sunhy\Desktop\동화창작DGX-spark` |
| 대상 파일 | `agent.md`, `reports/harness_engineering_design.md` |

## 3. 발생 명령어

```powershell
Get-Content -Raw -LiteralPath 'agent.md'
```

## 4. 오류 메시지

명령어가 실패한 것은 아니지만, 콘솔 출력에서 한글 문자가 깨져 보였다.

```text
AI Story Generator Codex Agent 吏移⑥꽌
```

## 5. 원인 분석

파일 자체는 UTF-8로 저장되어 있으나, PowerShell 콘솔 출력 인코딩 또는 실행 환경의 문자 표시 설정으로 인해 한글이 깨져 보이는 것으로 판단된다.

UTF-8로 파일을 읽었을 때는 한글 본문이 정상적으로 확인되었다.

## 6. 해결 방법

UTF-8 인코딩을 명시하여 파일 내용을 확인하였다.

```powershell
python -c "from pathlib import Path; text=Path('agent.md').read_text(encoding='utf-8'); print(text[:5000])"
```

## 7. 재검증 결과

UTF-8로 읽은 결과 `agent.md`의 한글 내용이 정상적으로 확인되었다.

## 8. 향후 예방 방안

- 한글 Markdown 파일 확인 시 UTF-8 인코딩을 명시한다.
- 콘솔 출력 결과만으로 파일이 깨졌다고 판단하지 않는다.
- 보고서 작성 시 파일 저장 인코딩은 UTF-8을 유지한다.

## 9. pytest 캐시 디렉터리 권한 경고

### 9.1 오류 개요

`python -m pytest -q` 실행 중 pytest 캐시 디렉터리 생성 권한 경고가 발생하였다.

### 9.2 발생 명령어

```bash
python -m pytest -q
```

### 9.3 경고 메시지

```text
PytestCacheWarning: could not create cache path ... [WinError 5] 액세스가 거부되었습니다.
```

### 9.4 원인 분석

테스트 실행 중 pytest가 캐시 디렉터리를 생성하려 했으나 현재 작업 디렉터리의 일부 캐시 경로에 접근 권한 문제가 발생하였다.

### 9.5 해결 방법

테스트 자체는 정상 통과하였다. 재발 방지를 위해 `.gitignore`에 pytest 캐시 및 Python 캐시 제외 규칙을 추가하였다.

이후 pytest 임시 캐시 디렉터리가 테스트 수집 대상에 포함되어 `PermissionError`가 발생하였다. 해당 디렉터리가 일반 삭제 권한으로 삭제되지 않아 `pytest.ini`를 추가하고 테스트 탐색 범위를 `tests` 디렉터리로 제한하였다.

```ini
[pytest]
testpaths = tests
norecursedirs =
    .git
    .venv
    __pycache__
    .pytest_cache
    pytest-cache-files-*
addopts = -p no:cacheprovider
```

### 9.6 재검증 결과

```text
2 passed in 0.27s
```
