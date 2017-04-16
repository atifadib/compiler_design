from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from random import randint

def char_dev(charac,adj_pos,adj_neg,filename):
    charac=charac.lower()
    r_part1="[\w+\s]*"
    r_part2="["+charac+"]"
    r_part3="\s[\w+\s]*"
    k=0
    lst1=[]
    lst2=[]
    while(k<3):
        a=randint(0,len(adj_pos)-1)
        lst1.append(adj_pos[a])
        k+=1
    k=0
    while(k<3):
        a=randint(0,len(adj_neg)-1)
        lst2.append(adj_neg[a])
        k+=1
    lst=lst1+lst2
    s='|'.join(lst)
    r_part4="["+s+"]"
    r_part5="\s*[\w+\s]*\w*"
    regex=r_part1+r_part2+r_part3+r_part4+r_part5
    s1=0
    c1=1
    s2=0
    c2=1
    s3=0
    c3=1
    s4=0
    c4=1
    s5=0
    c5=1
    file1=open(filename,"r")
    lines=file1.readlines()
    length=len(lines)
    part=length/5
    part=int(part)
    counter=0
    for i in lines:
        if(charac in i.lower()):
            obj=TextBlob(i)
            if(counter in range(0,part)):
                s1+=obj.sentiment.polarity
                c1+=1
            if(counter in range(part,part*2)):
                s2+=obj.sentiment.polarity
                c2+=1
            if(counter in range(part*2,part*3)):
                s3+=obj.sentiment.polarity
                c3+=1                
            if(counter in range(part*3,part*4)):
                s4+=obj.sentiment.polarity
                c4+=1                    
            if(counter in range(part*4,part*5)):
                s5+=obj.sentiment.polarity
                c5+=1
        counter+=1        
    sentiments=((s1/c1)*100,(s2/c2)*75,(s3/c3)*50,(s4/c4)*25,(s5/c5)*12.5)
    
    
    n_groups=5
    fig, ax = plt.subplots()
    
    index = np.arange(n_groups)
    bar_width = 0.35
    std_err=(1,1,1,1,1)
    
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
    plt.title('TEXT DOCUMENT ANALYSIS WITH LEXICAL ANALYZER')
    plt.xticks(index + bar_width / 2, (charac+':1',charac+':2',charac+':3',charac+':4',charac+':5'))
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    return regex
