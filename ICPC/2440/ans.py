import sys
import collections


registered = set()
isLocked = True

n = int(sys.stdin.readline())
for i in xrange(n):
    ID = sys.stdin.readline().strip()
    registered.add(ID)

n = int(sys.stdin.readline())
for i in xrange(n):
    ID = sys.stdin.readline().strip()
    if ID not in registered:
        print 'Unknown', ID
    elif isLocked:
        print 'Opened by', ID
        isLocked = False
    else:
        print 'Closed by', ID
        isLocked = True
