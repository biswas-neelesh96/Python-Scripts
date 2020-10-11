def recursive_index(arr,n,m,res):
	if(n<0):
		return 0;
	else:
		if(arr[n]==m):
			res.append(n)
		n = n-1
		recursive_index(arr,n,m,res)


arr = []
res = []
while True:
	inp = input("Enter the elements of array / Enter 'done' : ")
	if(inp == 'done'):
		break
	try:
		inp = int(inp)
	except:
		print("Incorrect input.")
		continue
	else:
		arr.append(inp)
while True:
	inp = input("Enter an integer : ")
	try:
		m = int(inp)
	except:
		print("Incorrect input.")
		continue
	else:
		break
recursive_index(arr,len(arr)-1,m,res)
print("The indices with elements equal to " ,m, " are : " ,res)