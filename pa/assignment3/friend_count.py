import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    a = record[0]
    b = record[1]
    mr.emit_intermediate(a, b)

def reducer(key, list_of_values):
    mr.emit((key, len(list_of_values)))


if __name__ == '__main__':
    inputData = open(sys.argv[1])
    mr.execute(inputData, mapper, reducer)