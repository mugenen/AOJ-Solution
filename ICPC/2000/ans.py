import sys
import collections

Gem = collections.namedtuple('Gem', 'x y')

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    gem = set()
    for i in xrange(n):
        x, y = map(int, sys.stdin.readline().split())
        gem.add(Gem(x, y))
    M = int(sys.stdin.readline())
    cur_x = cur_y = 10
    check = set()
    for i in xrange(M):
        d, l = sys.stdin.readline().split()
        l = int(l)
        if d == 'N':
            for g in gem:
                if cur_x == g.x and cur_y <= g.y <= cur_y + l:
                    check.add(g)
            cur_y += l
        elif d == 'S':
            for g in gem:
                if cur_x == g.x and cur_y - l <= g.y <= cur_y:
                    check.add(g)
            cur_y -= l
        elif d == 'E':
            for g in gem:
                if cur_x <= g.x <= cur_x + l and cur_y == g.y:
                    check.add(g)
            cur_x += l
        elif d == 'W':
            for g in gem:
                if cur_x - l <= g.x <= cur_x and cur_y == g.y:
                    check.add(g)
            cur_x -= l
    if len(check) == len(gem):
        print 'Yes'
    else:
        print 'No'
