from pydantic import BaseModel

class Question(BaseModel):
    input: str | None = None

class Answer(BaseModel):
    output: str | None = None
