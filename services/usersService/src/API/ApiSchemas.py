from pydantic import BaseModel, ConfigDict, Field


class UserCreateRequest(BaseModel):
    userName: str = Field(min_length=3)
    email: str
    name: str = Field(min_length=2)
    password: str = Field(min_length=8, max_length=128)


class UserUpdateRequest(BaseModel):
    userName: str | None = Field(default=None, min_length=3)
    email: str | None = None
    name: str | None = Field(default=None, min_length=2)
    password: str | None = Field(default=None, min_length=8, max_length=128)


class UserResponse(BaseModel):
    id: int | None
    userName: str
    email: str
    name: str
    cargo: str | None

    model_config = ConfigDict(from_attributes=True)


class ErrorResponse(BaseModel):
    detail: str
