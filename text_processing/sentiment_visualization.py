from textblob import TextBlob
import seaborn as sns
def senti_visual(texts_list):
    #get sentiments_polarity and sentiments_subjectivity based on text
    sentiments_polarity=[]
    sentiments_subjectivity=[]
    for i in texts_list:
#         pdb.set_trace()
        try:
            blob=TextBlob(str(i))
#             pdb.set_trace()
            sentiments_polarity.append(blob.sentiment.polarity)
            sentiments_subjectivity.append(blob.sentiment.subjectivity)
        except UnicodeEncodeError: 
#             i=unicode(i,'ascii').encode('UTF-8')
            blob=TextBlob(i)
            sentiments_polarity.append(blob.sentiment.polarity)
            sentiments_subjectivity.append(blob.sentiment.subjectivity)
    df=pd.DataFrame({'sentiments_polarity':sentiments_polarity,'sentiments_subjectivity':sentiments_subjectivity})
    sns.jointplot(df.iloc[:,0],df.iloc[:,1],kind='hex')