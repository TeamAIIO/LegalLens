from sqlalchemy import Column, Integer, String, Text, BigInteger
from resource.database import Base

class Test1(Base):
    __tablename__ = 'test1'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String(100))

class Precedent(Base):
    __tablename__ = 'precedent_test'
    # 판례정보일련번호
    CaseSerialNumber = Column(BigInteger, primary_key=True)
    # 사건명
    CaseName = Column(Text)
    # 사건번호
    CaseNumber = Column(Text)
    # 선고일자
    JudgmentDate = Column(BigInteger)
    # 선고
    JudgmentType = Column(Text)
    # 법원명
    CourtName = Column(Text)
    # 사건종류명
    CaseType = Column(Text)
    # 판결유형
    VerdictType = Column(Text)
    # 판시사항
    Matter = Column(Text)
    # 판결요지
    Summary = Column(Text)
    # 참조조문
    ReferenceArticle = Column(Text)
    # 참조판례
    ReferenceCase = Column(Text)
    # Matter + Summary 통합 텍스트
    Target = Column(Text)
