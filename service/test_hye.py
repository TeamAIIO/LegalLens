from resource.base_models import Answer


def testData(input, db):
    return

def tempData():
    answer_temp: Answer = Answer()
    answer_temp.question = '이것은 고객의 질문입니다ㄹㄹㄹㄹㄹㄹ'
    answer_temp.serialNumber = 123123 # 내부 확인용입니다, 고객 노출 x
    answer_temp.originAnswer = 'DB에서 뽑은 Target 답변입니다'
    answer_temp.shortAnswer = 'GPT가 요약해줄 것입니다'
    answer_temp.caseNumber = '85다카794'
    answer_temp.date = 20240417 #2024-04-17

    print('method', answer_temp)

    return answer_temp

# from fastapi import FastAPI, HTTPException, Request
# from pydantic import BaseModel

# app = FastAPI()

# # Pydantic 모델을 사용하여 요청 데이터 정의
# class Question(BaseModel):
#     question: str

# # '/submitQuestion' 엔드포인트에 POST 요청을 처리하는 핸들러 함수
# @app.post("/submitQuestion")
# async def submit_question(question: Question):
#     # 클라이언트로부터 받은 질문 데이터를 가져옴
#     user_question = question.question
    
#     # 여기서는 임시 데이터를 반환함. 실제로는 질문에 대한 처리를 수행하여 데이터를 생성해야 함.
#     temp_data = {
#         'shortAnswer': 'GPT가 요약해줄 것입니다',
#         'serialNumber': 123123,
#         'date': 20240417,
#         'caseNumber': '85다카794'
#     }

#     return temp_data
