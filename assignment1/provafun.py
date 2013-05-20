def retorna():
    scores={}
    scores["hola"]=34
    scores["adeu"]=22

    return scores

def pinta(scores):
    for i in scores.keys():
        print i +"value="+str(scores[i])


if __name__=="__main__":
    
    sco=retorna()
    pinta(sco)
    
