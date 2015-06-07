import sys
list = []
for str in sys.stdin:
    list.append(str)
list.sort()
for str in list:
    print(str)