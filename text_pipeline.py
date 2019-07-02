#输入一个英文文本组成的列表，这个函数将列表分词后统一处理，进行分词、词干化、归一化,去停用词，返回处理后的词列表
from textblob import TextBlob
import numpy as np
import pandas as pd
import time
import nltk
import pdb
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))


def preprocess_pipeline(text_list):
    from nltk.stem.porter import PorterStemmer
    from nltk.stem import WordNetLemmatizer
    """tokenize&stemming"""
    text_tokens=[]
    porter_stemmer = PorterStemmer()
    
    for i in text_list:
#         pdb.set_trace()
        try:
            tokens = nltk.word_tokenize(str(i))
            text_tokens.extend(tokens)
        except:
            continue
    ###stopwords
#     text_tokens=[word.decode('asciai') for word in text_tokens]
#     text_tokens=[word.decode('utf8') for word in text_tokens]
#     text_tokens=[porter_stemmer.stem(word) for word in text_tokens]
    ###lemmatization
#     pdb.set_trace()
    wordnet_lematizer = WordNetLemmatizer()
#     text_tokens=[wordnet_lematizer.lemmatize(word) for word in text_tokens]
    text_tokens=[word.lower() for word in text_tokens]
    ###filter the type of words
    pos_tokens=nltk.pos_tag(text_tokens)
#     pdb.set_trace()
    text_tokens=[seq[0] for seq in pos_tokens if seq[1] in ['NN','JJ','NNP']]
    text_tokens=[word for word in text_tokens if word not in stop_words]
  
    return text_tokens