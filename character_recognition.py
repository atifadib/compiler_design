from textblob import TextBlob
from collections import Counter

import nltk

def char_rec(file):
    f=open(file,"r")
    lines=f.read()
    chars=[]
    
    
    obj=TextBlob(lines)
    tagging=nltk.ne_chunk(obj.tags,binary=True)
    
    for i in tagging:
        x=str(i)
        if('NE' in x):
            chars.append(str(i[0][0]).lower())
    f.close()
    
    return Counter(chars)
