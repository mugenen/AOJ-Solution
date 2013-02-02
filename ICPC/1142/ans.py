import sys

n = int(sys.stdin.readline())

for line in sys.stdin:
    line = line.strip()
    L = len(line)
    cand = set()
    for i in xrange(L):
        head = line[:i]
        tail = line[i:]
        cand.add(head + tail)
        cand.add(head[::-1] + tail)
        cand.add(head + tail[::-1])
        cand.add(head[::-1] + tail[::-1])
        cand.add(tail + head)
        cand.add(tail[::-1] + head)
        cand.add(tail + head[::-1])
        cand.add(tail[::-1] + head[::-1])
    print len(cand)
