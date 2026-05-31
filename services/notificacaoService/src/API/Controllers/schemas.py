from pydantic import BaseModel

class VersionDTO(BaseModel):
    version: str
    environment: str