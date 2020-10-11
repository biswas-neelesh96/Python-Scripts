count = dict()
while True:
	inp = input("Enter a file name: ")
	try:
		file = open(inp)
	except:
		print("No file exists with ",inp," name.")
		continue
	else:
		break
for line in file:
	words = line.split()
	for word in words:
		count[word.lower()] = count.get(word.lower(),0) + 1
bigword = None
bigcount = None
smallword = None
smallcount = 100000000
for word,value in count.items():
	if bigcount is None or value > bigcount:
		bigword = word
		bigcount = value
	if smallcount > value:
		smallword = word
		smallcount = value
print(f"The word {bigword} occurs maximum number of times: {bigcount}")
print(f"The word {smallword} occurs minimum number of times: {smallcount}")