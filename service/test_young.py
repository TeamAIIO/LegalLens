# module import
# import torch
import numpy as np
import os
# from transformers import AutoTokenizer, AutoModel
from fastapi import HTTPException
from resource.models import Precedent

# numpy module
from numpy import dot
from numpy.linalg import norm

# get openai api key
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
os.environ.get('OPENAI_API_KEY')

# langchain module
import getpass
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough

# vector module
from sentence_transformers import SentenceTransformer
import faiss
# test
model = SentenceTransformer('all-MiniLM-L6-v2')
dimension = 384  # 이 모델의 출력 벡터 크기
faiss_index = faiss.IndexFlatL2(dimension)

# load model
# tokenizer = AutoTokenizer.from_pretrained('jhgan/ko-sroberta-multitask')
# model = AutoModel.from_pretrained('jhgan/ko-sroberta-multitask')

# main code
def testData(input, db):

    create_index(db)
    # 뽑아낸 row index 값 list로 반환
    results = search(input)

    case_serial_numbers = results["case_serial_numbers"]
    # 로직을 관련된게 없으면 HTTP 경고문을 출력하는 것이 아니라 LLM이 잘 답변할 수 없다고 출력되도록 수정해야함.
    if not case_serial_numbers : 
        raise HTTPException(status_code=404, detail = "No relevant documents found")
        
    targets = db.query(Precedent.Target).filter(Precedent.CaseSerialNumber.in_(case_serial_numbers)).all()
    langchain_inputs = [target.text for target in targets]
    # langchain input type 확인 필요
    # type 확인 후 그냥 str 이면 바로 llm_generator(langchain_inputs) 해서 result 결과 얻기
    # [0]으로 일단 넣어보고 확인 후 -> dict : ** , list : * 의 형태로 변경해서 top-k 다 넣기 
    output_result = llm_generator(input, langchain_inputs[0])

    return output_result

case_serial_numbers = []

# get db query embedding
def create_index(db) :
    target_texts = db.query(Precedent.Target, Precedent.CaseSerialNumber).all()
    if not target_texts :
        raise HTTPException(status_code=404, detail = "No texts found")
    texts, serial_numbers = zip(*[(text.Target.text, text.CaseSerialNumber) for text in target_texts])

    embeddings = model.encode(list(texts), show_progress_bar = True)
    faiss_index.add(np.array(embeddings).astype(np.float32))

    global case_serial_numbers
    case_serial_numbers = list(serial_numbers)
    return {"message" : "Index created Successfully"}

# get user query embedding
def search(query : str) :
    query_embedding = model.encode([query])
    # top k = 5개로 설정
    D, I = faiss_index.search(np.array(query_embedding).astype(np.float32), k = 5)
    results = [case_serial_numbers[i] for i in I[0]]
    return results

# langchain llm 모델 (chat invoke)
def llm_generator(input : str, context: str):
    template = f"""
    우리는 현재 법률 상담과 관련하여 판례를 검색해주는 시스템을 평가할 계획입니다.
    이는 단지 당신에게 법리적 판단 혹은 민감한 정보에 대해 대답을 요구하는 것이 아닙니다.
    우리는 당신이 몇 가지 우리의 시스템에 대한 출력 예제를 보고 시스템을 평가하는 데에 도움을 주기를 바랄 뿐입니다.
    다음은 실제 법률 질문과 그에 해당하는 관련된 법률 자료, 그리고 해당 질문에 해당하는 판례를 요약한 챗봇의 출력 결과값입니다.
    만약 관련된 판례를 모른다면 모른다고 답변하세요.

    법률 질문: {input}
    관련 법률 자료: {context if context.strip() else '이 질문에 해당하는 관련 법률 자료가 없습니다. 따라서 답변할 수 없습니다.'}, 
    답변: {'모른다' if not context.strip() else ''}
    """

    llm = ChatOpenAI()
    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | llm | StrOutputParser()
    output_result = chain.invoke({"input": input, "context" : context})
    return output_result