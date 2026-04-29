import os
from dataclasses import dataclass, field


def _split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "AI Story Generator")
    app_version: str = os.getenv("APP_VERSION", "0.1.0")
    environment: str = os.getenv("APP_ENV", "local")
    cors_origins: list[str] = field(
        default_factory=lambda: _split_csv(os.getenv("CORS_ORIGINS", "*"))
    )
    output_base_url: str = os.getenv("OUTPUT_BASE_URL", "/outputs")
    llama_cpp_dir: str = os.getenv("LLAMA_CPP_DIR", "external/llama.cpp")
    llama_cpp_server_url: str = os.getenv("LLAMA_CPP_SERVER_URL", "http://127.0.0.1:8080")
    comfyui_dir: str = os.getenv("COMFYUI_DIR", "external/ComfyUI")
    comfyui_api_url: str = os.getenv("COMFYUI_API_URL", "http://127.0.0.1:8188")
    voxcpm_dir: str = os.getenv("VOXCPM_DIR", "external/VoxCPM")
    voxcpm_model_path: str = os.getenv("VOXCPM_MODEL_PATH", "models/VoxCPM2")


settings = Settings()
