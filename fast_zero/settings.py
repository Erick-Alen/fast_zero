from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )
    ACCESS_TOKEN_EXPIRES_AT: int
    ALGORITHM: str
    DATABASE_URL: str
    SECRET_KEY: str
