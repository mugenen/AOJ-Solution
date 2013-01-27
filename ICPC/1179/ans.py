import sys

def daysOfYear(y):
    if y <= 0:
        return 0
    elif y % 3 == 0:
        return 200
    else:
        return 195

def daysOfMonth(y, m):
    if y % 3 == 0 or m % 2 == 1:
        return 20
    else:
        return 19


mil = 1
for i in xrange(1, 1000):
    mil += daysOfYear(i)

raw_input()
for line in sys.stdin:
    y, m, d = map(int, line.split())
    s = 0
    for i in xrange(1, y):
        s += daysOfYear(i)
    for i in xrange(1, m):
        s += daysOfMonth(y, i)
    print mil - s - d
