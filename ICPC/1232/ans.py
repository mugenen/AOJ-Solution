import sys
import bisect


MAX = 100001
prime = [-1] * MAX
i = 2
p = []
while MAX > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		p.append(i)
		temp = i * 2
		while temp < MAX:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2


while True:
    m, a, b = map(int, sys.stdin.readline().split())
    if m == 0:
        break
    cand = (-1, -1, -1)
    for q in p:
        idx = bisect.bisect_right(p, min(m / q, q)) - 1
        if idx == -1:
            continue
        value = p[idx]
        if value >= float(a) / b * q and cand[0] < q * value and value <= q:
            cand = (q * value, value, q)
    print cand[1], cand[2]
