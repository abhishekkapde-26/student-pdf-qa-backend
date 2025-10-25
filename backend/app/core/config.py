import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://app:secret@localhost:5432/appdb",
    )
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    storage_path: str = os.getenv("STORAGE_PATH", "./data/storage")
    faiss_index_path: str = os.getenv("FAISS_INDEX_PATH", "./data/faiss.index")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    chunk_size: int = 800  # characters
    chunk_overlap: int = 120

settings = Settings()
