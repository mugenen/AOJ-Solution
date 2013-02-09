def coin(n):
    return n / 500 + (n % 500) / 100 + (n % 100) / 50 + (n % 50) / 10

ret = ''

while True:
    n = int(raw_input())
    if n == 0:
        break
    c10, c50, c100, c500 = map(int, raw_input().split())
    m = 20000
    result = []
    for i in xrange(c10 + 1):
        for j in xrange(c50 + 1):
            for k in xrange(c100 + 1):
                for l in xrange(c500 + 1):
                    money = 500 * l + 100 * k + 50 * j + 10 * i
                    if money >= n:
                        if coin(money - n) < m:
                            m = coin(money - n)
                            result = [i, j, k, l]
    if result[0] != 0:
        ret += '10 ' + str(result[0])
        ret += '\n'
    if result[1] != 0:
        ret += '50 ' + str(result[1])
        ret += '\n'
    if result[2] != 0:
        ret += '100 ' + str(result[2])
        ret += '\n'
    if result[3] != 0:
        ret += '500 ' + str(result[3])
        ret += '\n'
    ret += '\n'

print ret[:-1]