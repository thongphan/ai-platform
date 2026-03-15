from pydantic import BaseModel


class AppSettings(BaseModel):
    name: str
    log_level: str


class LLMSettings(BaseModel):
    provider:str
    base_url: str
    model: str
    api_key: str


class Settings(BaseModel):
    app: AppSettings
    llm: LLMSettings