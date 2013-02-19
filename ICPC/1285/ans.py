import sys
import collections

while True:
    n, w = map(int, sys.stdin.readline().split())
    
    if n == 0:
        break
    
    count = collections.Counter()
    for i in xrange(n):
        count[int(raw_input()) / w] += 1
    largest_value = count.most_common(1)[0][1]
    largest_key = max(count.keys())
    ink = 0
    for i, v in count.iteritems():
        if i >= largest_key:
            continue
        ink += (largest_key - float(i)) / (largest_key) * v / largest_value
    print ink + 0.01
