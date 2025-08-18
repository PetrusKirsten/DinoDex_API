from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://PaleoDex:PaleoDex@localhost/PaleoDex')

settings = Settings()
