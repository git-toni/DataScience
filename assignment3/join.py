import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #key = record[0]
    #value = record[1]
    table = record[0]
    order_id = record[1]
    #print order_id
    #words = valiue.split()
    #for all fields
    for w in record:
      mr.emit_intermediate(order_id, w)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    #NOW APPENDING ALL FIELDS TO TOTAL
    #total = []
    #print len(list_of_values)
    #print list_of_values[4]
    nitems=(len(list_of_values)-10)/17
    #print nitems
    orderlist=[] 
    for v in range(10):
      orderlist.append(list_of_values[v])

    for ni in range(nitems):
        #create new list based on order base
        whole=list(orderlist)
        startpoint=10+ni*17
        endpoint=startpoint+17
        whole.extend(list_of_values[startpoint:endpoint])
        mr.emit((whole))





      

    #mr.emit((key, total))
    #mr.emit((total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
