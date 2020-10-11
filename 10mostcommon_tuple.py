#Finding 10 most common words in .txt file

handle = input("enter file name: ")		#Enter .txt file
try:
	handle = open(handle)
except:
	print(handle , "no such file exists.")
	quit()
count = dict()
for line in handle:
	words = line.split()
	for word in words:
		count[word] = count.get(word,0) + 1
temp = list()
for k,v in count.items():
	temp.append((v,k))
print(sorted(temp,reverse=True)[:10])