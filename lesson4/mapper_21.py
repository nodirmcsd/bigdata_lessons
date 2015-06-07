import sys
for line in sys.stdin:
    key, val = line.strip().split("\t")
    print val + "\t1" 
	
