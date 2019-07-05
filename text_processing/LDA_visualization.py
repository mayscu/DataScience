def LDA_visualization(text_,stop_words,n_topics):
    #Vectorizing,stemming, tf-idf
    from sklearn.feature_extraction.text import TfidfVectorizer
    vect = TfidfVectorizer(stop_words=stop_words,max_df=100000,min_df=5,encoding='utf-8',ngram_range=(1, 1))
    X=vect.fit_transform(text_)

    from sklearn.decomposition import LatentDirichletAllocation
    lda=LatentDirichletAllocation(n_components=10,learning_method='batch',max_iter=25,random_state=0)#random_state influence the results
    documemt_topics=lda.fit_transform(X)

    sorting=np.argsort(lda.components_,axis=1)[:,::-1]
    feature_names=np.array(vect.get_feature_names()) #get the name of features

    #print first 10 docuements
    mglearn.tools.print_topics(topics=range(n_topics),feature_names=feature_names,sorting=sorting,topics_per_chunk=5,n_words=10)
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(1,2,figsize=(10,10))
    topic_names=["{:>2}".format(i)+" ".join(words)
            for i,words in enumerate(feature_names[sorting[:,:2]])]

#
    for col in [0,1]:
        start=col*(n_topics/2)
        end=(col+1)*((n_topics/2))
        ax[col].barh(np.arange(5),np.sum(documemt_topics,axis=0)[start:end])
        ax[col].set_yticks(np.arange(5))
        ax[col].set_yticklabels(topic_names[start:end], ha="left", va="top")
        ax[col].invert_yaxis()
        ax[col].set_xlim(0, 1000)
        yax = ax[col].get_yaxis()
        yax.set_tick_params(pad=130)
    plt.tight_layout()