from textblob import TextBlob
from collections import Counter


def char_rec(file):
    f=open(file,"r")
    lines=f.readlines()
    chars=[]
    for l in lines:
        obj=TextBlob(l)
        for i in obj.tags:
            if('NNP' in i):
                print("a")
                chars.append(i[0])
    new_chars=Counter(chars)
    f.close()
    return new_chars