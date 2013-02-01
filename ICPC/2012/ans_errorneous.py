import sys
import math

while True:
    e = int(sys.stdin.readline())
    if e == 0:
        break
    result = 10000000
    for z in xrange(int(math.pow(e, 1.0/3)), -1, -1):
        if z < 0 or e - math.pow(z, 3) < 0:
            continue
        for y in xrange(int(math.pow(e - math.pow(z, 3), 1.0 / 2)), -1, -1):
            if y < 0:
                continue
            x = e - math.pow(z, 3) - math.pow(y, 2)
            if x < 0:
                continue
            result = min(result, int(x + y + z))
    print result
