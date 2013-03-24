import sys
import collections

while True:
    n = int(raw_input())
    if n == 0:
        break
    
    state = []
    free = []
    for i in xrange(n):
        temp = map(int, raw_input().split())
        if temp[0] != 0:
            free.append(set(temp[1:]))
        else:
            free.append(set())
        state.append(set([i]))
    
    for i in xrange(1, 31):
        cand = []
        new = set()
        for j in xrange(n):
            if i in free[j]:
                cand.append(j)
                new |= state[j]
        for c in cand:
            state[c] = new
        if len(new) == n:
            print i
            break
    else:
        print -1
