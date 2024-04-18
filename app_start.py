import uvicorn


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True) # 외부 접속 허용
    # uvicorn.run("main:app", host="localhost", port=8000, reload=True)