while True:
    n, m, a = map(int, raw_input().split())
    if n == 0:
        break
    bar = [[-1 for i in xrange(n + 1)] for j in xrange(1001)]
    for i in xrange(m):
        h, p, q = map(int, raw_input().split())
        bar[h][p] = q
        bar[h][q] = p
    
    cur = a
    
    for i in xrange(1000, -1, -1):
        if bar[i][cur] != -1:
            cur = bar[i][cur]
    print cur
