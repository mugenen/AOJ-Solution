import sys

for line in sys.stdin:
    if line == '.':
        break
    st = []
    for c in line:
        if c == '(' or c == '[' or c == ')' or c == ']':
            st.append(c)
        
        clean = ''.join(st)
        while '()' in clean or '[]' in clean:
            clean = clean.replace('()', '').replace('[]', '')
    if len(clean) == 0:
        print 'yes'
    else:
        print 'no'
