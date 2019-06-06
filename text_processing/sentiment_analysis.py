from textblob import TextBlob

def senti_ana(text_list):
	#对评论内容调用情感分析函数，结果存入sentiments_polarity和sentiments_subjectivity中
	sentiments_polarity=[]
	sentiments_subjectivity=[]
	for i in review_translated:
	    blob=TextBlob(i)
	    sentiments_polarity.append(blob.sentiment.polarity)
	    sentiments_subjectivity.append(blob.sentiment.subjectivity)
	    #将评论情感转换为数据框
	df=pd.DataFrame({'review_sentiments_polarity':sentiments_polarity,'review_sentiments_subjectivity':sentiments_subjectivity})
	return df