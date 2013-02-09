import sys


def parse(n):
    temp = 0
    digit = 1
    for c in n:
        if c == 'm':
            temp += digit * 1000
            digit = 1
        elif c == 'c':
            temp += digit * 100
            digit = 1
        elif c == 'x':
            temp += digit * 10
            digit = 1
        elif c == 'i':
            temp += digit
            digit = 1
        else:
            digit = int(c)
    return temp

def transform(n):
    temp = ''
    key = ['i', 'x', 'c', 'm']
    for i in xrange(3, -1, -1):
        digit = n / (10**i)
        if digit > 0:
            temp += '' if digit == 1 else str(digit)
            temp += key[i]
            n %= 10**i
    return temp


n = int(sys.stdin.readline())
for z in xrange(n):
    a, b = sys.stdin.readline().split()
    print transform(parse(a) + parse(b))
