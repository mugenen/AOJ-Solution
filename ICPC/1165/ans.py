import sys
import collections

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    
    pos = {0:(0, 0)}
    
    for i in xrange(N - 1):
        n, d = map(int, sys.stdin.readline().split())
        if d == 0:
            pos[i + 1] = (pos[n][0] - 1, pos[n][1])
        elif d == 1:
            pos[i + 1] = (pos[n][0], pos[n][1] - 1)
        elif d == 2:
            pos[i + 1] = (pos[n][0] + 1, pos[n][1])
        elif d == 3:
            pos[i + 1] = (pos[n][0], pos[n][1] + 1)
    
    max_x = min_x = max_y = min_y = 0
    for x, y in pos.values():
        max_x = max(x, max_x)
        min_x = min(x, min_x)
        max_y = max(y, max_y)
        min_y = min(y, min_y)
    
    print max_x - min_x + 1, max_y - min_y + 1