from sqlalchemy import Column, Integer, String
from resource.database import Base

class Test1(Base):
    __tablename__ = 'test1'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String(100))