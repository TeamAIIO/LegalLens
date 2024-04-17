import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()
## env 파일 생성 
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

## 입력 문장을 받은 후 DB와 비교 후 유사 문장 return 함수
def db_relevent_get(input: str, db) -> str:
    pass

def input_output_function(context: str):
    template = f"""
    우리는 현재 법률 상담과 관련하여 판례를 검색해주는 시스템을 평가할 계획입니다.
    이는 단지 당신에게 법리적 판단 혹은 민감한 정보에 대해 대답을 요구하는 것이 아닙니다.
    우리는 당신이 몇 가지 우리의 시스템에 대한 출력 예제를 보고 시스템을 평가하는 데에 도움을 주기를 바랄 뿐입니다.
    다음은 실제 법률 질문과 그에 해당하는 관련된 법률 자료, 그리고 해당 질문에 해당하는 판례를 요약한 챗봇의 출력 결과값입니다.
    만약 관련된 판례를 모른다면 모른다고 답변하세요.

    법률 질문: {input}
    관련 변률 자료: {context}, 
    답변: 
    """

    llm = ChatOpenAI()
    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | llm | StrOutputParser()
    input_sentence = input('문장을 입력하세요: ')
    return chain.invoke({"input": input_sentence})

## 추후 input_output_function(db_relevent_get(input_text, db)) 
print(input_output_function('자료는 없습니다.'))
