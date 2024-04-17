from resource.models import Test1
from transformers import AutoTokenizer, AutoModel

# db
from sqlalchemy.orm import Session

import torch
import numpy as np
import os

# numpy module
from numpy import dot
from numpy.linalg import norm

# load model
tokenizer = AutoTokenizer.from_pretrained('jhgan/ko-sroberta-multitask')
model = AutoModel.from_pretrained('jhgan/ko-sroberta-multitask')

def testData(input, db):
    print('question', input)
    list = db.query(Test1).all()
    print(list)
    return list


# Embedding & cosine similarity
def mean_pooling(model_output, attention_mask) :
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def cos_sim(A, B) :
    return dot(A, B) / (norm(A)*norm(B))


def get_precedent(db : Session = Depends(get_db)) :
    # db 에서 판례 가져오기
    precedent_files = db.query(Test1).all()
    precednet_info = [{'precedent_num' : idx+1, 'title' : Test1.title, 'content' : Test1.content} for idx, Test1 in enumerate(precedent_files)]
