while True:
    a, l = map(int, raw_input().split())
    if a == l == 0:
        break
    check = {}
    i = 0
    while a not in check:
        temp = list(str(a).zfill(l))
        temp.sort()
        check[a] = i
        a = int(''.join(temp[::-1])) - int(''.join(temp))
        i += 1
    print check[a], a, i - check[a]
