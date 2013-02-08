import sys

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    route = []
    for i in xrange(n):
        d, p = map(int, sys.stdin.readline().split())
        route.append([p, d])
    route.sort(reverse=True)
    count = 0
    for c, l in route:
        if l < m:
            m -= l
        elif m <= l:
            count += (l - m) * c
            m = 0
    print count
