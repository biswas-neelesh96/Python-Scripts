def naive_count(names,count):
	for name in names:
		if name not in count:
			count[name] = 1
		else:
			count[name] += 1
	return count

def fast_count(names,count):
	for name in names:
		count[name] = count.get(name,0) + 1
	return count

count = dict()
names = []
while True:
	inp = input("enter name / 'done : ")
	if(inp == 'done'):
		break
	names.append(inp)
#ount = naive_count(names,count)
count = fast_count(names,count)
print(count)