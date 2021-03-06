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
    mr.emit_intermediate(record[0], record[1])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    nfriends=len(list_of_values)

    mr.emit((key, nfriends))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
