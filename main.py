import os
from fastapi import Depends, FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from resource.base_models import Question
from resource.database import engine, SessionLocal
from sqlalchemy.orm import Session
from resource.models import Test1
from resource import models

from service.test_hun import testData as testHun
from service.test_hye import testData as testHye
from service.test_song import testData as testSong
from service.test_sun import testData as testYou
from service.test_young import testData as testYoung

app = FastAPI()

abs_path = os.path.dirname(os.path.realpath(__file__))
templates = Jinja2Templates(directory=f"{abs_path}/templates")
app.mount("/static", StaticFiles(directory=f"{abs_path}/static"))

# db model binding(sqlalchemy)
models.Base.metadata.create_all(bind=engine)

# task model binding
# question_answerer = pipeline("question-answering", model="stevhliu/my_awesome_qa_model")
# translator = pipeline("translation", model="stevhliu/my_awesome_opus_books_model")


# DB 연결
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# index
@app.get("/")
def goHome(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})

# test
@app.get("/test")
def getData(request: Request, db: Session = Depends(get_db)):
    list = db.query(Test1).all()
    print(list)
    return list

@app.post("/inputTestTest")
def getData(input: Question, db: Session = Depends(get_db)):
    list = db.query(Test1).all()
    return list

# song : 한송훈
@app.get("/testSong")
def getData(input: str, db: Session = Depends(get_db)):
    output = testSong(input, db)
    return output

# young : 박선영
@app.get("/testYoung")
def getData(input: Question, db: Session = Depends(get_db)):
    output = testYoung(input, db)
    return output

# hun : 조영훈
@app.get("/testHun")
def getData(input: str, db: Session = Depends(get_db)):
    output = testHun(input, db)
    return output

# hye : 손지혜
@app.get("/testHye")
def getData(input: str, db: Session = Depends(get_db)):
    output = testHye(input, db)
    return output

# you : 신유선
@app.post("/testYou")
def getData(input: Question, db: Session = Depends(get_db)):
    output = testYou(input, db)
    return output


# TODO
# 1) mysql에서 데이터 읽기 + 비교 : 전체
# 2) chroma에서 데이터 비교 : 팀장님
# 3) 유사성 높은 답변으로 프롬프팅 돌리기



