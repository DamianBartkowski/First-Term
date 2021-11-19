color = ["red", "blue" , "green"]
with open('file1.txt','w+') as f:
	for i in color:
		f.write('%s\n'%i)
with open('file1.txt') as f:
	print(f.read())
