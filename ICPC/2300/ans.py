import itertools

memo = {}

def dist(x, y):
    key = (x, y)
    if key in memo:
        return memo[key]
    
    v = sum(map(lambda x: (x[0] - x[1]) ** 2, zip(x, y)))
    memo[key] = v
    return v


N, M = map(int, raw_input().split())
color = []
for i in xrange(N):
    l, a, b = map(float, raw_input().split())
    color.append((l, a, b))

m = -1
for c in itertools.combinations(color, M):
    temp = 0
    for i in xrange(M - 1):
        for j in xrange(i + 1, M):
            temp += dist(c[i], c[j])
#            print dist(c[i], c[j]), c[i], c[j]
    m = max(m, temp)

print '{:.10f}'.format(m)
