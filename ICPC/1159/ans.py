import sys

while True:
    n, p = map(int, sys.stdin.readline().split())
    if n == 0 and p == 0:
        break
    hand = [0 for i in xrange(n)]
    cur = 0
    cur_p = p
    success = False
    while True:
        if cur_p > 0:
            hand[cur] += 1
            cur_p -= 1
            
            if hand[cur] == p:
                success = True
                print cur
                break
        else:
            cur_p = hand[cur]
            hand[cur] = 0
        cur += 1
        cur %= n
