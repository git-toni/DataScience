import sys
import json

#ORGANIZATION is LIKE this:
# terms =[noccurences, freq]
def gatherOcurrences(tweetfile):
    alines=tweetfile.readlines()
    terms={}
    for line in alines:
        tweet=json.loads(line)
        if "text" in tweet.keys():
            words=tweet["text"].split()
            for w in words:
                w=w.lower()
                if w in terms:
                    terms[w][0]+=1
                elif w not in terms:
                    terms[w]=[1,0.0]
    return terms

def computeFrequency(terms):
    ntotal=sum(t[0] for t in terms.itervalues())
    #print ntotal
    for w in terms.itervalues():
        w[1]=w[0]/float(ntotal)
    return terms

def printFrequency(terms):
    for w in terms:
        #print w+" "+str(terms[w][1])
        print "%s %.4f" %(w,terms[w][1])

def main():
    tweet_file=open(sys.argv[1])
    terms=gatherOcurrences(tweet_file)
    terms=computeFrequency(terms)
    printFrequency(terms)

if __name__ == '__main__':
    main()

