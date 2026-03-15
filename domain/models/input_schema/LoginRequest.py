from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    name: str = Field(
        default="User name to login",
        description="User name"
    )

    password: str = Field(
        default="Provide a password",
        description="User password"
    )