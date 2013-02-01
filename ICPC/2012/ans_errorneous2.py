import sys
import math

while True:
    e = int(sys.stdin.readline())
    if e == 0:
        break
    result = 10000000
    for z in xrange(1000001):
        if z ** 3 > e:
            break
        for y in xrange(1000001):
            if z ** 3 + y ** 2 > e:
                break
            x = e - z ** 3 - y ** 2
            result = min(result, int(x + y + z))
    print result
