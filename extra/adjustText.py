count = 0
numbers = []

f = open("./10seg-1-clean.txt", "w")
with open('texto.txt', 'r') as file:
	for line in file:
		if '0.' in line:
			f.write(str(count)+"-"+str(line))
		count += 1