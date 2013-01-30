import sys
import collections

x = [1, 1, 0, -1, -1, -1, 0, 1]
y = [0, 1, 1, 1, 0, -1, -1, -1]
while True:
    W, H = map(int, sys.stdin.readline().split())
    if W == 0:
        break
    
    tile = [[-1 for i in xrange(W + 2)] for j in xrange(H + 2)]
    
    
    for i in xrange(H):
        line = raw_input().strip().split()
        for j in xrange(W):
            if line[j] == '1':
                tile[i + 1][j + 1] = 1
            elif line[j] == '0':
                tile[i + 1][j + 1] = 0
    result = 0
    for h in xrange(1, H + 1):
        for w in xrange(1, W + 1):
            if tile[h][w] == 1:
                result += 1
                next = set([(h, w)])
                while len(next) > 0:
                    temp_next = set()
                    for n_h, n_w in next:
                        tile[n_h][n_w] = -1
                        for i in xrange(len(x)):
                            temp = (n_h + x[i], n_w + y[i])
                            if tile[temp[0]][temp[1]] == 1:
                                temp_next.add(temp)
                    next = temp_next
    print result

