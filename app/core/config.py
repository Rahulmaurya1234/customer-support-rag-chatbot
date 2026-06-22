from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    gemini_api_key: str
    model_name: str

    chunk_size: int
    chunk_overlap: int

    pdf_folder: str
    faiss_index_path: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()