while True:
    n, m, a = map(int, raw_input().split())
    if n == 0:
        break
    bar = []
    for i in xrange(m):
        h, p, q = map(int, raw_input().split())
        bar.append((h, p, q))
    bar.sort(key = lambda x: -x[0])
    last = 200
    cur = a
    for b in bar:
        if b[0] < last:
            if b[1] == cur:
                cur = b[2]
                last = b[0]
            elif b[2] == cur:
                cur = b[1]
                last = b[0]
    print cur
