def max_occurence(arr):
	count = 0
	arr.sort()
	res = arr[0]
	count = 0
	temp = count
	for i in range(0,len(arr)):
		if(i==0):
			count+=1
		elif(arr[i]==arr[i-1]):
			count+=1
			if(temp < count):
				res = arr[i]
				temp = count
		else:
			count = 1
	return res

arr = []
while True:
	inp = input("Enter elements of array / enter 'done' : ")
	if(inp == "done"):
		break
	try:
		inp = int(inp)
	except:
		print("Incorrect input.")
		continue
	else:
		arr.append(inp)
res = max_occurence(arr)
print("The element occuring maximum number of times is: {}".format(res))