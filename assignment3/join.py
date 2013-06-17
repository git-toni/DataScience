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
    #words = valiue.split()
    #for all fields
    for w in range(2,len(record)):
      mr.emit_intermediate(order_id, record[w])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    #NOW APPENDING ALL FIELDS TO TOTAL
    total = []
    for v in list_of_values:
      total.append(v)
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
