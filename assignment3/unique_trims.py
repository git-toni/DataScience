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
  seq_id = record[0]
  nucleo = record[1]
  trimmed_nucleo = nucleo[:-10]
  #We send a key=1 cause we want them all together
  mr.emit_intermediate(1,trimmed_nucleo)

def reducer(key, list_of_values):
  #print len(list_of_values)
  #removing duplicates
  unique_nucleo=list(set(list_of_values))
  #print len(unique_nucleo )
  for v in unique_nucleo:
    mr.emit((v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
