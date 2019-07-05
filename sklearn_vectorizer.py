from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer




#Customization
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
import nltk
from nltk.stem.porter import PorterStemmer
def custom_tokenizer(document):
    porter_stemmer = PorterStemmer()
    doc_nltk= nltk.word_tokenize(document)
#     pdb.set_trace()
    doc_nltk=[w.upper() for w in doc_nltk]
#     doc_nltk=[porter_stemmer.stem(word) for word in doc_nltk]
#     pdb.set_trace()
    doc_nltk=[w for w in doc_nltk if w not in stop_words]
    return doc_nltk




lemma_vect = TfidfVectorizer(vocabulary=voc_)
X=lemma_vect.fit_transform(texts_list)
voc_=lemma_vect.vocabulary_#get the vocabulary dict

#export fequency list 
word=lemma_vect.get_feature_names()
freq=X.toarray().sum(axis=0)

pd.DataFrame({'word':word,'freq':freq}).to_csv('freq.csv',encoding='utf-8')