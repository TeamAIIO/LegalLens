# 초기 db 설정파일입니다.

# resource 상대경로 설정
import sys
import os
import json
sys.path.insert(0, os.path.abspath('../'))

import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, Date, text, insert
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import sessionmaker
from resource.db_env import user, password, host, db_name

# 데이터베이스 연결 설정
# db_url = "mysql+pymysql://root:1234@localhost:3306/legal_db"
db_url = f"mysql+pymysql://{user}:{password}@{host}:3306/{db_name}"
engine = create_engine(db_url)
metadata = MetaData()

# 테이블 정의
precedent_table = Table('precedent_test', metadata,
    Column('CaseSerialNumber', Integer, primary_key=True, comment='판례정보일련번호'),
    Column('CaseName', Text, comment='사건명'),
    Column('CaseNumber', Text, comment='사건번호'),
    Column('JudgmentDate', Integer, comment='선고일자'),
    Column('JudgmentType', Text, comment='선고'),
    Column('CourtName', Text, comment='법원명'),
    Column('CaseType', Text, comment='사건종류명'),
    Column('VerdictType', Text, comment='판결유형'),
    Column('Matter', Text, comment='판시사항'),
    Column('Summary', Text, comment='판결요지'),
    Column('ReferenceArticle', Text, comment='참조조문'),
    Column('ReferenceCase', Text, comment='참조판례'),
    Column('Target', Text, comment='통합텍스트')
)

# 기존 테이블 삭제 후 새 테이블 생성
metadata.drop_all(engine)
metadata.create_all(engine)

# 데이터 로드
df = pd.read_csv("precedent.csv", index_col=0)
df = df.rename(columns={
    '판례정보일련번호': 'CaseSerialNumber',
    '사건명': 'CaseName',
    '사건번호': 'CaseNumber',
    '선고일자': 'JudgmentDate',
    '선고': 'JudgmentType',
    '법원명': 'CourtName',
    '사건종류명': 'CaseType',
    '판결유형': 'VerdictType',
    '판시사항': 'Matter',
    '판결요지': 'Summary',
    '참조조문': 'ReferenceArticle',
    '참조판례': 'ReferenceCase',
    'Target': 'Target'
})
df = df.where(pd.notna(df), None)
json_str = df.to_json(orient='records')
json_df = pd.DataFrame(json.loads(json_str))
json_df.columns = [str(col) for col in json_df.columns]
# print(json_df.columns)
# 데이터 삽입
Session = sessionmaker(bind=engine)
session = Session()
try:
    for index, row in json_df.iterrows():
        data_dict = {key: row[key] for key in ['CaseSerialNumber', 'CaseName', 'CaseNumber', 'JudgmentType', 'JudgmentDate', 'CourtName', 'CaseType', 'VerdictType', 'Matter', 'Summary', 'ReferenceArticle', 'ReferenceCase', 'Target']}
        stmt = insert(precedent_table).values(**data_dict)
        print(data_dict)
        session.execute(stmt)
    session.commit()
except Exception as e:
    session.rollback()
    print(e)
finally:
    session.close()

# with engine.connect() as conn:
#     query = text("INSERT INTO precedent_test (JSON) VALUES (:json_data)")
#     conn.execute(query, {'json_data' : json_str})