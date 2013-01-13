import sys


while True:
    n, r = map(int, sys.stdin.readline().split())
    if n == 0 and r == 0:
        break
    shuffle = []
    for i in xrange(r):
        shuffle.append(map(int, sys.stdin.readline().split()))
    shuffle.reverse()
    pile = range(n)
    for s in shuffle:
        pile[s[0] + s[1] - 1:s[0] + s[1] - 1] += pile[:s[1]]
        pile = pile[s[1]:]
#        print pile
    print len(pile) - pile.index(0)

"""10 9 8 7 6 5 4 3 2 1
1 10 9 8 7 6 5 4 3 2
4 3 2 1 10 9 8 7 6 5

0 1 2 3 4 5 6 7 8 9
3 4 5 6 7 8 9 0 1 2
4 5 6 7 8 9 0 1 2 3

5 4 3 2 1
3 5 4 2 1
4 3 5 2 1

0 1 2 3 4
1 2 0 3 4
2 0 1 3 4"""
