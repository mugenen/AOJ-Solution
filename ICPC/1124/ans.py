import sys
import collections

while True:
    N, Q = map(int, sys.stdin.readline().split())
    if N == 0:
        break
    counter = collections.Counter()
    for i in xrange(N):
        date = map(int, sys.stdin.readline().split())
        if date[0] != 0:
            counter.update(date[1:])
    
    if len(counter) == 0:
        print 0
        continue
    
    result = counter.most_common()
    largest = result[0][1]
    
    ret = -1
    if largest < Q:
        print 0
    else:
        smallest = 100
        for n, c in result:
            if c < largest:
                break
            if n < smallest:
                smallest = n
        print smallest
