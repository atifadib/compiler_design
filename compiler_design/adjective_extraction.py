from textblob import TextBlob

def connectfile(filename):
    file=open(filename,"r")
    lines=file.readlines()
    return lines

def getAdj(filename):
    file=open(filename,"r")
    lines=file.readlines()    
    negative=[]
    positive=[]
    neutral=[]
    for l in lines:
        l=l.lower()
        obj=TextBlob(l)
        for i in obj.tags:
            if('JJ' in i):
                sen=TextBlob(i[0])
                if(sen.sentiment.polarity>0):
                    positive.append(i[0])
                else:
                    negative.append(i[0])
    return positive,negative                
    