import sys


pair = {')': '(', ']': '['}
for line in sys.stdin:
    if line == '.':
        break
    st = []
    for c in line:
        if c == '(' or c == '[':
            st.append(c)
        elif c == ')' or c == ']':
            if len(st) > 0 and st[-1] == pair[c]:
                st.pop()
            else:
                print 'no'
                break
    else:
        if len(st) == 0:
            print 'yes'
        else:
            print 'no'
