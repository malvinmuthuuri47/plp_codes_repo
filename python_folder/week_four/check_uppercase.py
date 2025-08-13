with open("output.txt", "r") as f:
	text = f.read()
	
	if text.isupper():
		print("The file content is uppercase")
	else:
		print("The file content is lowercase")
