import sys
d = {}
for str in sys.stdin:
    i = str.split(u"\t")
    if not d.has_key(i[0]):
        d[i[0]] = int(i[1])
    else:
        d[i[0]] = d[i[0]] + 1