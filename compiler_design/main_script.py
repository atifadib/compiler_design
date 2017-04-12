from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
import re

def main():
    file=open("gameofthrones1.txt","r")
    eddard,count_eddard=0.0,0.0
    jon,count_jon=0.0,0.0
    cersei,count_cersei=0.0,0.0
    jaime,count_jaime=0.0,0.0
    tyrion,count_tyrion=0.0,0.0
    daenerys,count_daenerys=0.0,0.0
    joffrey,count_joffrey=0.0,0.0
    
    pattern_tyrion="[\w+\s]*[Tyrion|tyrion]\s[\w+\s]*[good|bad|killer|savior|harsh|evil|great|forgiving|strong|weak|fighter]\s*[\w+\s]*\w*"
    pattern_eddard="[\w+\s]*[Arya|arya]\s[\w+\s]*[good|bad|killer|savior|harsh|evil|great|forgiving|strong|weak|fighter]\s*[\w+\s]*\w*"
    pattern_jon="[\w+\s]*[Jon|jon|jon,|Jon,]\s[\w+\s]*[good|bad|killer|savior|harsh|evil|great|forgiving|strong|weak|fighter]\s*[\w+\s]*\w*"
    pattern_cersei="[\w+\s]*[Cersei|cersei]\s[\w+\s]*[good|bad|killer|savior|harsh|evil|great|forgiving|strong|weak|fighter]\s*[\w+\s]*\w*"
    pattern_jaime="[\w+\s]*[Jaime|jaime]\s[\w+\s]*[good|bad|killer|savior|harsh|evil|great|forgiving|strong|weak|fighter]\s*[\w+\s]*\w*"
    pattern_daenerys="[\w+\s]*[daenerys|Daenerys]\s[\w+\s]*[good|bad|killer|savior|harsh|evil|great|forgiving|strong|weak|fighter]\s*[\w+\s]*\w*"
    pattern_joffery="[\w+\s]*[Joffery|joffery]\s[\w+\s]*[good|bad|killer|savior|harsh|evil|great|forgiving|strong|weak|fighter]\s*[\w+\s]*\w*"
    wordlist=['Eddard','Jon','Cersei','Jaime','Tyrion','Daenerys','Joffrey']
    
    positive_adj=['good','saviour','great','forgiving','strong','fighter']
    negative_adj=['bad','killer','harsh','evil','weak']
    
    tyrion,jon,eddard,cersei,daenerys,joffery,jaime=0.0,0.0,0.0,0.0,0.0,0.0,0.0
    
    lines=file.readlines()
    
    for i in lines:
        words=i
        #print(words)
        if('eddard' in words.lower()):
            #print("here0")
            if(re.match(pattern_eddard,words)):
                eddard+=1.0
            obj=TextBlob(i)
            eddard+=obj.sentiment.polarity
            count_eddard+=1.0
        if('jon' in words.lower()):
            #print("here1")        
            if(re.match(pattern_jon,words)):
                jon+=1.0
            obj=TextBlob(i)
            jon+=obj.sentiment.polarity
            count_jon+=1.0
        if('cersei' in words.lower()):
            #print("here2")
            if(re.match(pattern_cersei,words)):
                cersei+=1.0
            obj=TextBlob(i)        
            cersei+=obj.sentiment.polarity
            count_cersei+=1.0
        if('jaime' in words.lower()):
            #print("here3")
            if(re.match(pattern_jaime,words)):
                jaime+=1.0
            obj=TextBlob(i)
            jaime+=obj.sentiment.polarity
            count_jaime+=1.0
        if('tyrion' in words.lower()):
            #print("here4")
            if(re.match(pattern_tyrion,words)):
                tyrion+=1.0        
            obj=TextBlob(i)
            tyrion+=obj.sentiment.polarity
            count_tyrion+=1.0
        if('daenerys' in words.lower()):
            #print("here5")
            if(re.match(pattern_daenerys,words)):
                daenerys+=1.0        
            obj=TextBlob(i)
            daenerys+=obj.sentiment.polarity
            count_daenerys+=1.0
        if('joffrey' in words.lower()):
            if(re.match(pattern_joffery,words)):
                joffery+=1.0        
            obj=TextBlob(i)
            joffrey+=obj.sentiment.polarity
            count_joffrey+=1.0
    
    eddard=eddard/count_eddard
    jon=jon/count_jon
    cersei=cersei/count_cersei
    jaime=jaime/count_jaime
    tyrion=tyrion/count_tyrion
    daenerys=daenerys/count_daenerys
    joffrey=joffrey/count_joffrey
    
    print("eddard ",eddard)
    print("jon ",jon)
    print("cersei ",cersei)
    print("jaime ",jaime)
    print("tyrion ",tyrion)
    print("daenerys ",daenerys)
    print("Joffrey ",joffrey)
    
    sentiments=(eddard*100,jon*100,cersei*100,jaime*100,tyrion*100,daenerys*100,joffrey*100)
    n_groups=7
    fig, ax = plt.subplots()
    
    index = np.arange(n_groups)
    bar_width = 0.35
    std_err=(0.001,0.001,0.001,0.001,0.001,0.001,0.001)
    
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, sentiments, bar_width,
                     alpha=opacity,
                     color='r',
                     yerr=std_err,
                     error_kw=error_config,
                     )
    plt.xlabel('Group')
    plt.ylabel('Scores')
    plt.title('GAME OF THRONES')
    plt.xticks(index + bar_width / 2, wordlist)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

