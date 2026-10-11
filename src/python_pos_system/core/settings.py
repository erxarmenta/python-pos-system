from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    PROJECT_NAME: str = "Python POS System"
    PROJECT_DESCRIPTION: str = "A simple pos system created with FastAPI"
    PROJECT_VERSION: str = "1.0.0"

    # Database
    DB_URL: str

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()