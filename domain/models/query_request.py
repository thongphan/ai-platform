from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    name: str = Field(
        default="Thong",
        description="User name"
    )

    query: str = Field(
        default="Explain dependency injection in Python",
        description="User query prompt"
    )