import sys

for line in sys.stdin:
    if line[0] == '#':
        break
    line = line.strip()
    step = [0, 0]
    before = int(line[0]) % 3 if int(line[0]) % 3 != 0 else 3
    NULL = 1000000
    for c in line[1:]:
        n = int(c) % 3 if int(c) % 3 != 0 else 3
        if n > before:
            step[0], step[1] = NULL, min(step[0], step[1] + 1)
        elif n < before:
            step[0], step[1] = min(step[0] + 1, step[1]), NULL
        else:
            step[0], step[1] = step[1], step[0]
        before = n
    print min(step)