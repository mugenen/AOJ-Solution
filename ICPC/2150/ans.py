import sys
import bisect

MAX = 2000000
prime = [-1] * MAX
prime_list = []
i = 2
while MAX > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		temp = i * 2
		prime_list.append(i)
		while temp < MAX:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2

while True:
    N, P = map(int, sys.stdin.readline().split())
    
    if N == P == -1:
        break
    
    start = bisect.bisect_right(prime_list, N)
    candidate = []
    for i in xrange(start, min(start + 101, MAX)):
        for j in xrange(i, min(start + 101, MAX)):
            candidate.append(prime_list[i] + prime_list[j])
    candidate.sort()
    print candidate[P - 1]

