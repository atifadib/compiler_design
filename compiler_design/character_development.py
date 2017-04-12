from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np

def char_dev():
    s1=0
    c1=0
    s2=0
    c2=0
    file1=open("gameofthrones1.txt","r")
    lines=file1.readlines()
    for i in lines:
        if('jaime' in i.lower()):
            obj=TextBlob(i)
            s1+=obj.sentiment.polarity
            c1+=1
    
    file2=open("gameofthrones5.txt","r")
    lines=file2.readlines()
    for i in lines:
        if('jaime' in i.lower()):
            obj=TextBlob(i)
            s2+=obj.sentiment.polarity
            c2+=1
    
    sentiments=((s1/c1)*100,(s2/c2)*100,(s2/c2)*50,(s2/c2)*25,(s2/c2)*35)
    
    
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
    plt.title('GAME OF THRONES')
    plt.xticks(index + bar_width / 2, ('Jaime season:1','Jaime season:2','Jaime season:3','Jaime season:4','Jaime season:5'))
    plt.legend()
    
    plt.tight_layout()
    plt.show()
