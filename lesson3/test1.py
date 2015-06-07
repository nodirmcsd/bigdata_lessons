dic = { 0: "a", 1: "b" , 2: "c"}
print sum(dic.keys())
del dic[1]
for i in dic.values():
	print i	