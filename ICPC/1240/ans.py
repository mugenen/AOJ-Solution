import sys
import bisect

n = int(sys.stdin.readline())
for z in xrange(n):
    order = sys.stdin.readline().strip()
    string = sys.stdin.readline().strip()
    
    half = len(string) / 2
    num = set(map(str, [0,1,2,3,4,5,6,7,8,9]))
    for o in order[::-1]:
#        print string, o
        if o == 'J':
            string = string[-1:] + string[:-1]
        elif o == 'C':
            string = string[1:] + string[:1]
        elif o == 'E':
            string = string[-half:] + string[:half] if half * 2 == len(string) or half == 0 else string[-half:] + string[half] + string[:half]
        elif o == 'A':
            string = string[::-1]
        elif o == 'P':
            temp = list(string)
            for i in xrange(len(temp)):
                if temp[i] in num:
                    temp[i] = str(int(temp[i]) + 10 - 1)[-1:]
            string = ''.join(temp)
        elif o == 'M':
            temp = list(string)
            for i in xrange(len(temp)):
                if temp[i] in num:
                    temp[i] = str(int(temp[i]) + 1)[-1:]
            string = ''.join(temp)
    print string
