import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # A = L*M
    # B = M*K
    # C = L*K
    L = M = K = 5

    name = record[0]
    i = record[1]
    j = record[2]
    v = record[3]

    val = name + ' ' + str(i) + ' ' + str(j) + ' ' + str(v);
    if name == 'a':
        for t in range(0, K):
            mr.emit_intermediate(str(i)+' '+str(t), val)
    else:
        for t in range(0, L):
            mr.emit_intermediate(str(t)+' '+str(j), val)

def reducer(key, list_of_values):
    a = {}
    b = {}
    for val in list_of_values:
        name, i, j, v = val.split()
        if name == 'a':
            a[j] = int(v)
        else:
            b[i] = int(v)

    s = 0
    for k in a:
        if k in b:
            s = s + a[k]*b[k]
    
    items = key.split()
    i = int(items[0])
    j = int(items[1])
    mr.emit((i,j,s))

if __name__ == '__main__':
    inputData = open(sys.argv[1])
    mr.execute(inputData, mapper, reducer)