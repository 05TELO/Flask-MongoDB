from pydantic import BaseModel


class Alarm(BaseModel):
    message: str
    used_memory: float
