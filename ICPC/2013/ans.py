import sys
import math

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    time = []
    for z in xrange(n):
        start, end = map(int, raw_input().replace(':', '').split())
        time.append((end, start))
    time.sort()
    train = [0]
    for end, start in time:
        for i in xrange(len(train)):
            if train[i] <= start:
                train[i] = end
                break
        else:
            train.append(end)
        train.sort(reverse=True)
    print len(train)
