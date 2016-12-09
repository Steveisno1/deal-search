# dealmoon
f = open('dealmoon_deals.json', 'r')
f2 = open('couponsModified.json', 'w')

# dealsea
f3 = open('dealsea_deals.json', 'r')
f4 = open('couponsModified1.json', 'w')

# slickdeal
f5 = open('slickdeal_deals.json', 'r')
f6 = open('couponsModified2.json', 'w')

'''
string = "\n             abcde\n     fghijk\n"
length = len(string)
i = 0


#modify item
while i < length:
	if string[i] == "\n":
		if i == 0:
			string = string[1:]
		else:
			string = string[0:i] + string[i+1:]
		length = len(string)
		if i < length:
			while string[i] == " ":
				if i == 0:
					string = string[1:]
				else:
					string = string[0:i] + string[i+1:]
				length = len(string)
	else:
		i += 1



print string

while 1:
	line = f.readline()
	if not line:
		break
	index = line.find('item')
	if index != -1 and line[index+8:index+9] != "]":
		line = line[:-2]
		f2.write(line + "\n")
'''
prev = ""
while 1:
	line = f.readline()
	if not line:
		f2.write(prev + "}")
		break
	index = line.find('item')
	if index != -1 and line[index+8:index+9] != "]":
		if prev == "":
			#f2.write(prev + "\n")
			line = line[:-2]
			prev = line
		else:
			f2.write(prev + "\n")
			line = line[:-2]
			prev = line

f2.close()
f.close()

prev = ""
while 1:
	line = f3.readline()
	if not line:
		f4.write(prev + "}")
		break
	index = line.find('item')
	if index != -1 and line[index+8:index+9] != "]":
		if prev == "":
			#f2.write(prev + "\n")
			line = line[:-2]
			prev = line
		else:
			f4.write(prev + "\n")
			line = line[:-2]
			prev = line

f4.close()
f3.close()

prev = ""
while 1:
	line = f5.readline()
	if not line:
		f6.write(prev + "}")
		break
	index = line.find('item')
	if index != -1 and line[index+8:index+9] != "]":
		if prev == "":
			#f2.write(prev + "\n")
			line = line[:-2]
			prev = line
		else:
			f6.write(prev + "\n")
			line = line[:-2]
			prev = line

f6.close()
f5.close()

