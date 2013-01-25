import sys

raw_input()

key = ['.,!? ', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

for line in sys.stdin:
    state = -1
    line = line.strip()
    result = ''
    count = 0
    for c in line:
        c = int(c) - 1
        if c == -1 and state != -1:
            result += key[state][count % len(key[state])]
            state = -1
        elif state == c:
            count += 1
        else:
            state = c
            count = 0
    print result
