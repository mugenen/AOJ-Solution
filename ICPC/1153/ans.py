import sys

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m ==0:
        break
    
    taro = []
    for i in xrange(n):
        x = int(sys.stdin.readline())
        
        taro.append(x)
    hanako = []
    for i in xrange(m):
        x = int(sys.stdin.readline())
        
        hanako.append(x)
    
    sum_taro = sum(taro)
    sum_hanako = sum(hanako)
    
    diff = -(sum_taro - sum_hanako) / 2.0
    if diff != int(diff):
        print -1
        continue
    MAX = max(taro + hanako) + 1
    result = MAX
    for t in taro:
        if t + diff in hanako:
            if result > t:
                result = t
    if result != MAX:
        print result, int(result + diff)
    else:
        print -1
