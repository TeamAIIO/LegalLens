import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

abs_path = os.path.dirname(os.path.realpath(__file__))
templates = Jinja2Templates(directory=f"{abs_path}/templates")
app.mount("/static", StaticFiles(directory=f"{abs_path}/static"))


@app.get("/")
def goHome(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})


# TODO : /service 하위에 서비스 만들고 끌어오기
# mysql에서 데이터 읽기 + 비교
# chroma에서 데이터 비교
# 유사성 높은 답변으로 프롬프팅 돌리기



