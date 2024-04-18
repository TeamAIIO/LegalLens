import numpy as np
from sentence_transformers import SentenceTransformer, util
import torch

from resource.base_models import Answer
from resource.models import Precedent
from service.langchain import getShortAnswer

# model 선언
model = SentenceTransformer("all-MiniLM-L6-v2")

# question 받아서 answer 돌려줌
def setUserData(input_text, db):
    # 판례 모음 DB 조회
    total_list = db.query(Precedent.CaseSerialNumber, Precedent.Target).filter(Precedent.Target.isnot(None)).order_by(Precedent.JudgmentDate.desc()).limit(1000).all()
    target_text_list = [precedent.Target for precedent in total_list]
    
    # similarity 체크
    max_index = searchHighestSimilarityIndex(input_text, target_text_list)

    # 유사도 가장 높은 답변 정보 가져오기
    search_data: Precedent = total_list[max_index]
    first_data: Precedent = db.query(Precedent).filter(Precedent.CaseSerialNumber == search_data.CaseSerialNumber).first()
    print('================\n', first_data.__dict__, '\n================')

    # LLM 요약
    short_answer = getShortAnswer(input_text, first_data.Target)

    # 응답 생성
    answer: Answer = Answer()
    answer.question = input_text
    answer.shortAnswer = short_answer
    answer.originAnswer = first_data.Summary if first_data.Summary != None else first_data.Matter
    answer.serialNumber = first_data.CaseSerialNumber
    answer.caseNumber = first_data.CaseNumber
    answer.date = first_data.JudgmentDate
    answer.referenceArticle = first_data.ReferenceArticle
    answer.referenceCase = first_data.ReferenceCase

    return answer


# sentences list 중 가장 유사도 높은 index를 반환
def searchHighestSimilarityIndex(input, target_list):
    sentences1 = [input]
    embeddings1 = model.encode(sentences1, convert_to_tensor=True)

    sentences2 = target_list
    embeddings2 = model.encode(sentences2)

    cosine_scores = util.cos_sim(embeddings1, embeddings2)
    maxIndex = torch.argmax(cosine_scores[0])
    print(maxIndex)
    print(sentences2[maxIndex])

    return np.array(maxIndex)