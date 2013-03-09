import sys
import bisect


while True:
    N, T, L, B = map(int, sys.stdin.readline().split())
    
    if N == 0:
        break
    
    state = [[0 for i in xrange(T + 2)] for j in xrange(N + 1)]
    
    lose = set()
    for i in xrange(L):
        lose.add(int(raw_input()))
    back = set()
    for i in xrange(B):
        back.add(int(raw_input()))
    
    state[0][0] = 1.0
    
    for i in xrange(T):
        for j in xrange(N):
            for k in xrange(1, 7):
                next = j + k
                if next > N:
                    next = N - (next - N)
                if next in lose:
                    state[next][i + 2] += state[j][i] / 6.0
                elif next in back:
                    state[0][i + 1] += state[j][i] / 6.0
                else:
                    state[next][i + 1] += state[j][i] / 6.0
        state[N][i + 1] += state[N][i]
    print '{:6f}'.format(state[N][T])
