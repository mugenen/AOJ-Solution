import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    
    if N == M == 0:
        break
    
    packet = []
    for i in xrange(M):
        packet.append(map(int, raw_input().split()))
    packet.sort()
    infected = set([1])
    for p in packet:
        if p[1] in infected:
            infected.add(p[2])
    print len(infected)
