import sys

MAX = 300001
candidate =[0 for i in xrange(MAX)]

for i in xrange(MAX):
    if i % 7 == 1 or i % 7 == 6:
        candidate[i] = 1

prime = []
for i in xrange(2, MAX):
    if candidate[i] == 1:
        prime.append(i)
        temp = i * 2
        while temp < MAX:
            candidate[temp] = 0
            temp += i

while True:
    n = int(sys.stdin.readline())
    if n == 1:
        break
    div = set()
    for p in prime:
        if n < p:
            break
        while n % p == 0:
#            n /= p
            div.add(p)
            break
    l_div = list(div)
    l_div.sort()
    print '{}:'.format(n),
    for d in l_div:
        print d,
    print
