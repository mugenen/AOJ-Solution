while True:
    N = int(raw_input())
    if N == 0:
        break
    secret = []
    for i in xrange(N):
        secret.append(set(map(int, raw_input().split())[1:]))
    leak = set(map(int, raw_input().split())[1:])
    candidate = -1
    for i in xrange(N):
        if leak.issubset(secret[i]):
            if candidate == -1:
                candidate = i + 1
            else:
                candidate = -1
                break
    print candidate
