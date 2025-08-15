from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://dinodex:dinodex@localhost/dinodex')

settings = Settings()
