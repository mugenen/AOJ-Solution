import sys
import collections

while True:
    pc, student = map(int, sys.stdin.readline().split())
    if pc == student == 0:
        break
    
    record = collections.defaultdict(list)
    r = int(raw_input())
    for i in xrange(r):
        t, n, m, s = map(int, sys.stdin.readline().split())
        record[m].append((t, n, s))
    q = int(raw_input())
    for i in xrange(q):
        start, end, q_student = map(int, sys.stdin.readline().split())
        temp_start = start
        time = 0
        f_open = set()
        for i_t, i_n, i_s in record[q_student]:
            if start <= i_t <= end:
                if i_s == 1:
                    if len(f_open) == 0:
                        temp_start = i_t
                    f_open.add(i_n)
                else:
                    f_open.remove(i_n)
                    if len(f_open) == 0:
                        time += i_t - temp_start
                        temp_start = -1
            elif i_t < start:
                if i_s == 1:
                    f_open.add(i_n)
                else:
                    f_open.remove(i_n)
        if len(f_open) > 0:
            time += end - temp_start
        print time
