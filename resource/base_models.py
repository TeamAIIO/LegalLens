from pydantic import BaseModel

class Question(BaseModel):
    input: str | None

class Answer(BaseModel):
    # 질문
    question: str | None
    # 검색된 판례
    originAnswer: str
    # 판례 요약
    shortAnswer: str
    # 판례 정보 일련 번호
    serialNumber: int
    # 사건 번호
    caseNumber: int
    # 선고 일자
    date: str
