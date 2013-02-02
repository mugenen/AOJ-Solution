import sys

MAX = 2500000
prime = [-1] * MAX
i = 2
while MAX > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		temp = i * 2
		while temp < MAX:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2

while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break

    count = 0
    for i in xrange(n + 1,  2 * n + 1):
        if prime[i - 1] == 0:
            count += 1
    print count
