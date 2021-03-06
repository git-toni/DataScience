import sys
import json
#import tweet_sentiment as ts

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def createdictionary(afinnfile):
    #afinnfile=open("AFINN-111.txt")
    scores={}
    for line in afinnfile:
        term,score=line.split("\t") #file tab-delimited
        term=term.decode('utf-8')
        scores[term]=int(score)
    return scores

def findSentiment(filein,filesentiment,scores):

    #Discard first line
    #first=filein.readline()
    #Get all lines
    alines=filein.readlines()
    sentiments=list()
    #for all tweets
    for line in alines:
        #convert to JSON
        tweet=json.loads(line)
        #If there's text tag an lang=en
        if "text" in tweet :
            words=tweet["text"].split(" ")
            suma=0.0
            for w in words:
                if w.lower() in scores:
                    suma+=scores[w.lower()]
            sentiments.append(suma)
    return sentiments

def findLineSentiment(tweet,scores):
    #If there's text tag an lang=en
    if "text" in tweet :
        words=tweet["text"].split(" ")
        suma=0.0
        for w in words:
            if w.lower() in scores:
                suma+=scores[w.lower()]
        return True,suma
    else:
        return False,0

def termSentiment(filein,scores):
    #scores: AFINN txt
    #sentiments: computed tweet sentiments
    #filein.readline()
    #print sentiments[0]
    alines=filein.readlines()
    terms={}
    for li in range(len(alines)):
        #Convert to json
        tweet=json.loads(alines[li])
        #save computed sentiment of tweet
        hasmood,mood=findLineSentiment(tweet,scores)
        if(hasmood):
            if mood>0:
                moodindex=1#positive mood
            elif mood<0:
                moodindex=2#negativ emood
            elif mood==0:
                moodindex=3#neutral mood
            #separate all words
            if "text" in tweet.keys():
                words=tweet["text"].split()
                for w in words:
                    w=w.lower()
                    if w not in scores:
                        if w in terms:
                            terms[w][0]+=mood
                            terms[w][moodindex]+=1
                        elif w not in terms:
                            terms[w]=[mood,0,0,0]
                            terms[w][moodindex]+=1
    return terms

def printTerms(termin):
    for term in termin.keys():
        ntotal=termin[term][1]+termin[term][2]+termin[term][3]
        average=termin[term][0]/(ntotal)
        
        #posneg=termin[term][1]/termin[term][2]
        #print t+" mean:"+str(average)+" posneg:"+str(posneg) 
        if average!=0.0:
            #print term+" mean:"+str(average) +" npos:"+str(termin[term][1])+" nneg:"+str(termin[term][2])
            print term+"\t"+str(average)




def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores=createdictionary(sent_file)
    #sentiments=findSentiment(tweet_file,sent_file,scores)
    #reset to beginning
    tweet_file.seek(0)
    allterms=termSentiment(tweet_file,scores)
    printTerms(allterms)





if __name__ == '__main__':
    main()
