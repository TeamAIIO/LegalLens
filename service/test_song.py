import os

from dotenv import load_dotenv
import torch
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from sentence_transformers import SentenceTransformer, util
from resource.models import Test1, Precedent
from transformers import AutoTokenizer, AutoModel
from numpy import dot
from numpy.linalg import norm
import time
from multiprocessing import Pool

tokenizer = AutoTokenizer.from_pretrained('jhgan/ko-sroberta-multitask')
# model = AutoModel.from_pretrained('jhgan/ko-sroberta-multitask')
model = SentenceTransformer("jhgan/ko-sroberta-multitask")

load_dotenv()

def testData(input, db):
    
    li = db.query(Precedent.Target, Precedent.CaseSerialNumber).limit(1000).all()
    embedded_target = []
    case_serial_numbers = []
    start = time.time()
    for each_target in li:
        embedding_each_target = model.encode(str(each_target[0]), convert_to_tensor=True)
        embedded_target.append(embedding_each_target)
        case_serial_numbers.append(each_target[1])
    
    input_embedding = model.encode(input, convert_to_tensor=True)
    end = time.time()
    embedded_target_tensor = torch.stack(embedded_target)
    
    cosine_scores = util.cos_sim(input_embedding, embedded_target_tensor)
    
    max_score, max_index = torch.max(cosine_scores, dim=1)
    max_score = max_score.item()
    max_index = max_index.item()
    max_case_serial_number = case_serial_numbers[max_index]
    
    print(f"time : {end-start}")
    return {
        "max_score": max_score,
        "max_index": max_index,
        "max_case_serial_number": max_case_serial_number
    }

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

if __name__ == "__main__":
    ## 추후 input_output_function(db_relevent_get(input_text, db)) 
    print(input_output_function('자료는 없습니다.'))
