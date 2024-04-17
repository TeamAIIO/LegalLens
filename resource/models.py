from sqlalchemy import Column, Integer, String, Text, BigInteger
from resource.database import Base

class Test1(Base):
    __tablename__ = 'test1'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String(100))

class Precedent(Base):
    __tablename__ = 'precedent'
    CaseSerialNumber = Column(BigInteger, primary_key=True)
    CaseName = Column(Text)
    CaseNumber = Column(Text)
    JudgmentDate = Column(BigInteger)
    JudgmentType = Column(Text)
    CourtName = Column(Text)
    CaseType = Column(Text)
    VerdictType = Column(Text)
    Matter = Column(Text)
    Summary = Column(Text)
    ReferenceArticle = Column(Text)
    ReferenceCase = Column(Text)
    FullText = Column(Text)
