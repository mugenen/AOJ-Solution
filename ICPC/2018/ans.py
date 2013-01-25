import sys
import collections


while True:
    N, M, P = map(int, sys.stdin.readline().split())
    if N == 0:
        break
    X = []
    for n in xrange(N):
        X.append(int(sys.stdin.readline()))
    if X[M - 1] == 0:
        print 0
    else:
        print int(float(sum(X)) * 100 * (100 - P) / 100 / X[M - 1])
