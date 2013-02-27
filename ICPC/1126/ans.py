import sys
import collections

while True:
    W, H = map(int, sys.stdin.readline().split())
    if W == 0:
        break
    area = [[-10**80 for i in xrange(H + 2)] for j in xrange(W + 2)]
    result = -1
    for i in xrange(H):
        line = sys.stdin.readline().strip()
        for j in xrange(W):
            if '0' <= line[j] <= '9':
                area[j + 1][i + 1] = int(line[j])
    for i in xrange(H):
        for j in xrange(W):
            area[j + 1][i + 1] = max(area[j + 1][i + 1], area[j + 1][i + 1] + area[j + 1][i] * 10, area[j + 1][i + 1] + area[j][i + 1] * 10)
            result = max(result, area[j + 1][i + 1])
    print result
