from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV_NAME: str = "local"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


settings = Settings()

