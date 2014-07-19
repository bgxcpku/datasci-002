import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
	# key: document identifier
	# value: document contents
	key = record[0]
	value = record[1]
	words = set(value.split())
	for w in words:
		mr.emit_intermediate(w, key);


def reducer(key, list_of_values):
	# key: word
	# value: list of document identifiers which contains the word
	mr.emit((key, list_of_values));

if __name__ == '__main__':
	inputData = open(sys.argv[1])
	mr.execute(inputData, mapper, reducer)