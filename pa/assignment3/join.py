import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	tableName = record[0]
	orderId = record[1]
	values = []
	values.append(tableName)

	for i in xrange(1, len(record)):
		values.append(record[i])

	mr.emit_intermediate(orderId, values)


def reducer(key, list_of_values):
	order_list = []
	line_item_list = []
	for record in list_of_values:
		if record[0]=='order':
			order_list.append(record)
		else:
			line_item_list.append(record)
	for r1 in order_list:
		for r2 in line_item_list:
			mr.emit(r1 +  r2)

if __name__ == '__main__':
	inputData = open(sys.argv[1])
	mr.execute(inputData, mapper, reducer)