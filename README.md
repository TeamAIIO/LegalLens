# LegalLens
Ai-x 4기 io팀 첫번째 미니 프로젝트입니다.

# 서비스 파이프라인
![pipeline](./readme_images/image.png)

# app 구동
python app_start.py

# local url
http://localhost:9000/

# OPENAI API KEY 파일 생성 필수
root 영역에 .env 파일 생성 후 아래 코드 입력
```
OPENAI_API_KEY = "팀장님께_문의_후_이_부분_수정할_것"
```

# requirements.txt 사용 전 설치 목록
```
pip install fastapi
pip install "uvicorn[standard]"
pip install jinja2 python-multipart
pip install pymysql
pip install sqlalchemy
pip install langchain_openai
pip install langchain
pip install langchain-chroma
pip install langchain-core 
pip install langchain-community
pip install transformers==4.37.1
pip install sentence-transformers
```
```
- 아래 목록은 보류
pip install jq
pip install faiss-gpu
pip install faiss
```