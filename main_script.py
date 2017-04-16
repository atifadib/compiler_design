from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
import re
from random import randint

def main(charlist,adj_pos,adj_neg,filename):
    character=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    sentiment=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    counts=[1.0,1.0,1.0,1.0,1.0,1.0,1.0]
    
    file=open(filename,"r")
    wordlist=[]
    chars=[]
    for x,y in charlist.items():
        chars.append(x)
    k=0    
    while(k<7):
        a=randint(0,len(chars)-1)
        if(chars[a] not in wordlist):
            wordlist.append(chars[a])
            k+=1
    regexs0=""
    regexs1=""
    regexs2=""
    regexs3=""
    regexs4=""
    regexs5=""
    regexs6=""
    for i in range(0,7):
        r_part1="[\w+\s]*"
        r_part2="["+str(wordlist[i])+"]"
        r_part3="\s[\w+\s]*"
        k=0
        lst1=[]
        lst2=[]
        while(k<3):
            a=randint(0,len(adj_pos)-1)
            if re.match(r'^\w+$', adj_pos[a]):
                lst1.append(adj_pos[a])
                k+=1
        k=0
        while(k<3):
            a=randint(0,len(adj_neg)-1)
            if re.match(r'^\w+$', adj_neg[a]):
                lst2.append(adj_neg[a])
                k+=1
        lst=lst1+lst2  
        s='|'.join(lst)
        
        r_part4="["+s+"]"
        r_part5="\s*[\w+\s]*\w*"
        if(i==0):
            regex0=r_part1+r_part2+r_part3+r_part4+r_part5
            
        if(i==1):
            regex1=r_part1+r_part2+r_part3+r_part4+r_part5
            #print(regex1)
        if(i==2):
            regex2=r_part1+r_part2+r_part3+r_part4+r_part5
            #print(regex2)
        if(i==3):
            regex3=r_part1+r_part2+r_part3+r_part4+r_part5
            #print(regex3)
        if(i==4):
            regex4=r_part1+r_part2+r_part3+r_part4+r_part5
            #print(regex4)
        if(i==5):
            regex5=r_part1+r_part2+r_part3+r_part4+r_part5
            #print(regex5)                                   
        if(i==6):
            regex6=r_part1+r_part2+r_part3+r_part4+r_part5
            #print(regex6)
    res1=[]#str(regex0)+"\n"+str(regex1)+"\n"+str(regex2)+"\n"+str(regex3)+"\n"+str(regex4)+"\n"+str(regex5)+"\n"+str(regex5)+"\n"
    res1.append(regex0)
    res1.append(regex1)
    res1.append(regex2)
    res1.append(regex3)
    res1.append(regex4)
    res1.append(regex5)
    res1.append(regex6)
    
    lines=file.readlines()
    
    for i in lines:
        words=i.lower()
        #print(words)
        if(wordlist[0] in words.lower()):
            #print("here0")
            if(re.match(regex0,words)):
                character[0]+=1.0
            obj=TextBlob(i)
            sentiment[0]+=obj.sentiment.polarity
            counts[0]+=1.0
        if(wordlist[1] in words.lower()):
            #print("here1")        
            if(re.match(regex1,words)):
                character[1]+=1.0
            obj=TextBlob(i)
            sentiment[1]+=obj.sentiment.polarity
            counts[1]+=1.0
        if(wordlist[2] in words.lower()):
            #print("here2")
            if(re.match(regex2,words)):
                character[2]+=1.0
            obj=TextBlob(i)        
            sentiment[2]+=obj.sentiment.polarity
            counts[2]+=1.0
        if(wordlist[3] in words.lower()):
            #print("here3")
            if(re.match(regex3,words)):
                character[3]+=1.0
            obj=TextBlob(i)
            sentiment[3]+=obj.sentiment.polarity
            counts[3]+=1.0
        if(wordlist[4] in words.lower()):
            #print("here4")
            if(re.match(regex4,words)):
                character[4]+=1.0        
            obj=TextBlob(i)
            sentiment[4]+=obj.sentiment.polarity
            counts[4]+=1.0
        if(wordlist[5] in words.lower()):
            #print("here5")
            if(re.match(regex5,words)):
                character[5]+=1.0        
            obj=TextBlob(i)
            sentiment[5]+=obj.sentiment.polarity
            counts[5]+=1.0
        if(wordlist[6] in words.lower()):
            if(re.match(regex6,words)):
                character[6]+=1.0        
            obj=TextBlob(i)
            sentiment[6]+=obj.sentiment.polarity
            counts[6]+=1.0
    a=[]
    for x,y in zip(sentiment,counts):
        res=x/y
        a.append(res)
    sentiments=(a[0]*100,a[1]*100,a[2]*100,a[3]*100,a[4]*100,a[5]*100,a[6]*100)
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
    plt.title('TEXT DOCUMENT ANALYSIS')
    plt.xticks(index + bar_width / 2, wordlist)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    return res1

