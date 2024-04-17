# module import
import torch
import numpy as np
import os
from transformers import AutoTokenizer, AutoModel
# numpy module
from numpy import dot
from numpy.linalg import norm


# load model
tokenizer = AutoTokenizer.from_pretrained('jhgan/ko-sroberta-multitask')
model = AutoModel.from_pretrained('jhgan/ko-sroberta-multitask')

def testData(input, db):
    return

# Embedding & cosine similarity
def mean_pooling(model_output, attention_mask) :
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def cos_sim(A, B) :
    return dot(A, B) / (norm(A)*norm(B))