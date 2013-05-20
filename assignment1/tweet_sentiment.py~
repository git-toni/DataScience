import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def createdictionary(afinnfile):
    #afinnfile=open("AFINN-111.txt")
    scores={}
    for line in afinnfile:
        term,score=line.split("\t") #file tab-delimited
        scores[term]=int(score)
    return scores

def findSentiment(filein,filesentiment,scores):

    #Discard first line
    first=filein.readline()
    #Get all lines
    alines=filein.readlines()
    sentiments=list()
    #for all tweets
    for line in alines:
        #convert to JSON
        tweet=json.loads(line)
        #If there's text tag an lang=en
        if "text" in tweet :
            #print tweet["text"]
            words=tweet["text"].split(" ")
            suma=0.0
            for w in words:
                if w.lower() in scores:
                    suma+=scores[w.lower()]
            #print "<sentiment:"+str(suma)+">\n"
        #print "appending"
        sentiments.append(suma)
            #print str(suma)
            #filesentiment.write("<sentiment: "+str(suma)+">\n")
    #print "mida sentiments "+str(len(sentiments))
    return sentiments

def printSentiments(sentiments):
    #print len(sentiments)
    for s in range(len(sentiments)):
        print str(sentiments[s])







def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores=createdictionary(sent_file)
    sentiments=findSentiment(tweet_file,sent_file,scores)
    printSentiments(sentiments)

if __name__ == '__main__':
    main()
