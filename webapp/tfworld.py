
#Download and load model, embeddings, and data, will take a several minutes. Double click on this to pop open the hood and checkout the code.
import wget
import gdown

gdown.download("https://drive.google.com/uc?id=10LV9QbZOkUyOzR4nh8hxesoKJhpmvpM9", "CitationSimilarityVectors106Epochs.npy", quiet=True, proxy=None)   # citation vectors
gdown.download("https://drive.google.com/open?id=1wIRsAApaE2L7E1fjnDOSSVBG1fY-LT9i", "tfworld.zip", quiet=True, proxy=None)
gdown.download("https://drive.google.com/uc?id=1-23aNm7j0bnycvyd_OaQfofVYPTewgOI", "AbstractSimVectors.npy", quiet=True, proxy=None)
gdown.download("https://drive.google.com/uc?id=1NyUQwgUNj9bFsiCnZ2TfKmWn5r-Y6wav", "TitlesIdsAbstractsEmbedIdsCOMPLETE_12-30-19.json.gzip", quiet=True, proxy=None)
url = 'https://s3-us-west-2.amazonaws.com/ai2-s2-research/scibert/huggingface_pytorch/scibert_scivocab_uncased.tar'
wget.download(url) 
import tarfile
weights = tarfile.open('scibert_scivocab_uncased.tar')
weights.extractall()


import numpy as np
import tensorflow as tf
from time import time
from tqdm import tqdm_notebook as tqdm
from transformers import BertTokenizer
import pandas as pd
from pprint import pprint

citations_embeddings = np.load('CitationSimilarityVectors106Epochs.npy')
abstract_embeddings = np.load('AbstractSimVectors.npy')
assert citations_embeddings.shape == abstract_embeddings.shape

normalizedC = tf.nn.l2_normalize(citations_embeddings, axis=1)
normalizedA = tf.nn.l2_normalize(abstract_embeddings, axis=1) 

model = tf.saved_model.load('tfworld/inference_model/')
tokenizer = BertTokenizer(vocab_file='scibert_scivocab_uncased/vocab.txt')

df = pd.read_json('TitlesIdsAbstractsEmbedIdsCOMPLETE_12-30-19.json.gzip', compression = 'gzip')
embed2Title = pd.Series(df['title'].values,index=df['EmbeddingID']).to_dict()
embed2Abstract = pd.Series(df['paperAbstract'].values,index=df['EmbeddingID']).to_dict()
embed2Paper = pd.Series(df['id'].values,index=df['EmbeddingID']).to_dict()

# query = 
def Infer(query, top_k_results=1):

    if top_k_results%2 == 0:
        halfA = halfC = int(top_k_results/2)
    else:
        halfC = int(top_k_results/2) + 1
        halfA = int(top_k_results/2) 

    abstract_encoded = tokenizer.encode(query, max_length=512, pad_to_max_length=True)
    abstract_encoded = tf.constant(abstract_encoded, dtype=tf.int32)[None, :]

    bert_output = model(abstract_encoded)
    xq = tf.nn.l2_normalize(bert_output, axis=1)

    simNumpyC = np.matmul(normalizedC, tf.transpose(xq))
    simNumpyCTopK = (-simNumpyC[:,0]).argsort()[:halfC]
    simNumpyC_oTopK = -np.sort(-simNumpyC[:,0])[:halfC]
    allCit = np.vstack((simNumpyCTopK , simNumpyC_oTopK) )
    del simNumpyC

    simNumpyA = np.matmul(normalizedA, tf.transpose(xq))
    simNumpyATopK = (-simNumpyA[:,0]).argsort()[:halfA]
    simNumpyA_oTopK = -np.sort(-simNumpyA[:,0])[:halfA]
    allAbs = np.vstack((simNumpyATopK , simNumpyA_oTopK) )
    del simNumpyA

    allResults = np.concatenate((allAbs, allCit), axis = 1)

    title = []
    abstractR = []
    link = []
    for embed in allResults[0]:
        title.append(embed2Title[int(embed)])
        abstractR.append(embed2Abstract[int(embed)])
        paperId = embed2Paper[int(embed)]
        link.append('https://www.semanticscholar.org/paper/'+paperId)
    return title, abstractR, link