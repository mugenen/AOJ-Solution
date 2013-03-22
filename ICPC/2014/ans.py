import sys
import math

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0:
        break
    field = [[-2 for i in xrange(h + 2)] for j in xrange(w + 2)]
    white = [[0 for i in xrange(h + 2)] for j in xrange(w + 2)]
    black = [[0 for i in xrange(h + 2)] for j in xrange(w + 2)]
    
    cand_white = []
    cand_black = []
    for i in xrange(h):
        line = raw_input()
        for j in xrange(w):
            if line[j] == 'W':
                field[j + 1][i + 1] = 1
                cand_white.append((j + 1, i + 1))
            elif line[j] == 'B':
                field[j + 1][i + 1] = -1
                cand_black.append((j + 1, i + 1))
            else:
                field[j + 1][i + 1] = 0
    next = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while len(cand_white) > 0:
        cur_x, cur_y = cand_white.pop()
        for n_x, n_y in next:
            if field[cur_x + n_x][cur_y + n_y] == 0 and white[cur_x + n_x][cur_y + n_y] == 0:
                cand_white.append((cur_x + n_x, cur_y + n_y))
                white[cur_x + n_x][cur_y + n_y] = 1
    while len(cand_black) > 0:
        cur_x, cur_y = cand_black.pop()
        for n_x, n_y in next:
            if field[cur_x + n_x][cur_y + n_y] == 0 and black[cur_x + n_x][cur_y + n_y] == 0:
                cand_black.append((cur_x + n_x, cur_y + n_y))
                black[cur_x + n_x][cur_y + n_y] = 1
    count_black = 0
    count_white = 0
    for i in xrange(h):
        for j in xrange(w):
            if white[j + 1][i + 1] > black[j + 1][i + 1]:
                count_white += 1
            if black[j + 1][i + 1] > white[j + 1][i + 1]:
                count_black += 1
    print count_black, count_white
