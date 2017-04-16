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
    for l in lines:
        l=l.lower()
        obj=TextBlob(l)
        for i in obj.tags:
            if('JJ' in i):
                if(i[0] not in positive and i[0] not in negative):
                    sen=TextBlob(i[0])
            
                    if(sen.sentiment.polarity>0):
                        positive.append(i[0])
                    else:
                        negative.append(i[0])
    return positive,negative                
    