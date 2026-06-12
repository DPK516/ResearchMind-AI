from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    mistral_api_key: str
    tavily_api_key: str
    
    model_name: str = "mistral-small-latest"
    temperature: float = 0.0
    timeout_seconds: int = 15

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()