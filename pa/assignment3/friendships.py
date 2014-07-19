import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    a = record[0]
    b = record[1]
    mr.emit_intermediate(a + ' ' + b, 1)
    mr.emit_intermediate(b + ' ' + a, 1)

def reducer(key, list_of_values):
    friends = set(list_of_values)
    a, b = key.split()
    if len(list_of_values)==1:
        mr.emit((a, b))


if __name__ == '__main__':
    inputData = open(sys.argv[1])
    mr.execute(inputData, mapper, reducer)