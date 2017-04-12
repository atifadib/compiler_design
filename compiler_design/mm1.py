
f=open("adj_good1.txt","w")
a=Counter(positive)
for x,y in a.items():
    m=str(x)
    n=str(y)
    f.write(m+" "+n+"\n")
f.close()
f=open("adj_bad.txt","w")
a=Counter(negative)
for x,y in a.items():
    m=str(x)
    n=str(y)
    f.write(m+" "+n+"\n")
f.close()
f=open("adj_neutral.txt","w")
a=Counter(neutral)
for x,y in a.items():
    m=str(x)
    n=str(y)
    f.write(m+" "+n+"\n")
f.close()




if(t.sentiment.polarity>0):
    positive.append(i[0])
if(t.sentiment.polarity<0):
    negative.append(i[0])
if(t.sentiment.polarity==0):
    neutral.append(i[0])