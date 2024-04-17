from typing import Optional
from pydantic import BaseModel

class Question(BaseModel):
    input: Optional[str] = None

class Answer(BaseModel):
    # 질문
    question: str | None = None
    # 검색된 판례
    originAnswer: str | None = None
    # 판례 요약
    shortAnswer: str | None = None
    # 판례 정보 일련 번호
    serialNumber: int | None = None
    # 사건 번호
    caseNumber: str | None = None
    # 선고 일자
    date: int | None = None
