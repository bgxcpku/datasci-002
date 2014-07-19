import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    id = record[0]
    nu = record[1][0:len(record[1])-10]
    mr.emit_intermediate(nu, id)

def reducer(key, list_of_values):
    mr.emit(key)

if __name__ == '__main__':
    inputData = open(sys.argv[1])
    mr.execute(inputData, mapper, reducer)