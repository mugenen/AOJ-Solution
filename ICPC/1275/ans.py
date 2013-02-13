import sys

while True:
    n, k, m = map(int, sys.stdin.readline().split())
    
    if n == 0:
        break
    
    stone = range(1, n + 1)
    stone.pop(m - 1)
    cur = m - 2
    for i in xrange(n - 2):
        cur = (cur + k) % len(stone)
        stone.pop(cur)
        cur -= 1
    print stone[0]

