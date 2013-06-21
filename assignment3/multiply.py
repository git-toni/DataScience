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
  #HARDCODE dimensions
  ndim=5
  matrix = record[0]
  fil = record[1]
  col = record[2]
  val = record[3]

  #We send a key=1 cause we want them all together
  if matrix == 'a':
	  for d in range(ndim):
		  mr.emit_intermediate( (fil,d),(col,val) )
  elif matrix == 'b':
	  for d in range(ndim):
		  mr.emit_intermediate( (d,col),(fil,val) )

def reducer(key, list_of_values):
  ndim=5
  #products=[1]*ndim
  products=[[0],[0],[0],[0],[0]]
  for tu in list_of_values:
	pos=tu[0]
	val=tu[1]
	products[pos].append(val)
  for tu in range(len(products)):
    mida=len(products[tu])
    if(mida<3):
	  products[tu]=0
    else:
	  products[tu]=products[tu][1]*products[tu][2]

  total=sum(products) 
  mr.emit((key[0],key[1],total))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
