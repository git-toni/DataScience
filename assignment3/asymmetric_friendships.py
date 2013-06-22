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
        #emit them as key and friend
    mr.emit_intermediate((record[0], record[1]),1)
    mr.emit_intermediate((record[1], record[0]),1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #print list_of_values
    ntimes=len(list_of_values)
    #print ntimes, key
    if ntimes == 1:
        mr.emit((key[0], key[1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
