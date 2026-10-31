from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Pengaturan aplikasi, dibaca dari file .env atau environment variable."""

    model_config = SettingsConfigDict(env_file=".env")

    database_url: str


settings = Settings()
