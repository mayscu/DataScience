#使用googleAPI将所有文本检测语种并且都翻译成英语，并存入list中

def detecting_translating(df):
    from googletrans import Translator
    review_translated=[]
    review_orginal=[]
    for i in df:
        translator = Translator(service_urls=['translate.google.cn'])
        source = i
        src = 'auto'
        dest = 'en'
        try:
            trans_result = translator.translate(source,src = src,dest = dest)
            a=trans_result.text
        except:
            a="#####" #对于出错的行直接标为井号
            
        print(a)
        review_translated.append(a)
        review_orginal.append(i)
        time.sleep(1)#避免被ban
    #将生成的翻译和原始文本合并到一个数据框中
    df={'original_review':review_orginal,'translated_review':review_translated}
    return df