def senti_ana(text_list):
    #对评论内容调用情感分析函数，结果存入sentiments_polarity和sentiments_subjectivity中
    sentiments_polarity=[]
    sentiments_subjectivity=[]
    for i in texts_list:
#         pdb.set_trace()
        try:
            blob=TextBlob(str(i))
#             pdb.set_trace()
            sentiments_polarity.append(blob.sentiment.polarity)
            sentiments_subjectivity.append(blob.sentiment.subjectivity)
            #将评论情感转换为数据框
        except UnicodeEncodeError: 
            i=unicode(i,'ascii').encode('UTF-8')
            blob=TextBlob(i)
            sentiments_polarity.append(blob.sentiment.polarity)
            sentiments_subjectivity.append(blob.sentiment.subjectivity)
            #将评论情感转换为数据框
                

    df=pd.DataFrame({'sentiments_polarity':sentiments_polarity,'sentiments_subjectivity':sentiments_subjectivity})
    return df