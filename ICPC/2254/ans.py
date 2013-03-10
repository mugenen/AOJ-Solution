import sys
import collections


while True:
    N = int(raw_input())
    if N == 0:
        break
    time = []
    for i in xrange(N):
        time.append(map(int, raw_input().split()))
    
    memo = {}
    def dp(state):
        if tuple(state) in memo:
            return memo[tuple(state)]
        
        L = len(state)
        if L <= 1:
            return time[state[0]][0]
        else:
            temp = []
            for i in state:
                copy = state[:]
                copy.remove(i)
                min_time = time[i][0]
                for j in xrange(len(time[i]) - 1):
                    if j in copy:
                        min_time = min(min_time, time[i][j + 1])
                temp.append(dp(copy) + min_time)
            memo[tuple(state)] = min(temp)
            return memo[tuple(state)]
    state = range(N)
    print dp(state)
