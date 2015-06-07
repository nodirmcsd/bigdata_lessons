import sys
for line in sys.stdin:
    for token in line.strip().split():
        print((token.decode("utf-8").lower() + u"\t1"))