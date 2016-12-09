import json

# dealmoon
f = open('couponsModified.json', 'r')
f2 = open('newcouponModified.json', 'w')

# dealsea
f3 = open('couponsModified1.json', 'r')
f4 = open('newcouponModified1.json', 'w')

# slickdeal
f5 = open('couponsModified2.json', 'r')
f6 = open('newcouponModified2.json', 'w')


while 1:
	line = f.readline()
	if not line:
		break
	else:
		length = len(line)
		i = 0
		while i < length:
			if line[i] == "\\" and line[i+1] == "n":
				if i == 0:
					line = line[2:]
				else:
					line = line[0:i] + line[i+2:]
				length = len(line)
				if i < length:
					while line[i] == " ":
						if i == 0:
							line = line[1:]
						else:
							line = line[0:i] + line[i+1:]
						length = len(line)
			else:
				i += 1
		i = 0
		while i < length:
			if line[i] == "\\" and line[i+1] == "u":
				line = line[0:i] + line[i+6:]
				length = len(line)
				# i += 2
			else:
				i += 1
		i = 0
		while i < length:
			if line[i] == "'":
				line = line[0:i] + "'" + line[i:]
				i += 2
			else:
				i += 1

	'''
	index = line.find('", "')
	while index != -1:
		line = line[0:index-1] + line[index+4:]
		index = line.find('", "')
	'''
	f2.write(line)

'''
line = f.readline()
length = len(line)
i = 0
while i < length:
	if line[i] == "\n":
		if i == 0:
			line = line[1:]
		else:
			line = line[0:i] + line[i+1:]
		length = len(line)
		if i < length:
			while line[i] == " ":
				if i == 0:
					line = line[1:]
				else:
					line = line[0:i] + line[i+1:]
				length = len(line)
	else:
		i += 1
print line
'''
f.close()
f2.close()


while 1:
	line = f3.readline()
	if not line:
		break
	else:
		length = len(line)
		i = 0
		while i < length:
			if line[i] == "\\" and line[i+1] == "n":
				if i == 0:
					line = line[2:]
				else:
					line = line[0:i] + line[i+2:]
				length = len(line)
				if i < length:
					while line[i] == " ":
						if i == 0:
							line = line[1:]
						else:
							line = line[0:i] + line[i+1:]
						length = len(line)
			else:
				i += 1
		i = 0
		while i < length:
			if line[i] == "\\" and line[i+1] == "u":
				line = line[0:i] + line[i+6:]
				length = len(line)
				# i += 2
			else:
				i += 1
		i = 0
		while i < length:
			if line[i] == "'":
				line = line[0:i] + "'" + line[i:]
				i += 2
			else:
				i += 1

	'''
	index = line.find('", "')
	while index != -1:
		line = line[0:index-1] + line[index+4:]
		index = line.find('", "')
	'''
	f4.write(line)

'''
line = f.readline()
length = len(line)
i = 0
while i < length:
	if line[i] == "\n":
		if i == 0:
			line = line[1:]
		else:
			line = line[0:i] + line[i+1:]
		length = len(line)
		if i < length:
			while line[i] == " ":
				if i == 0:
					line = line[1:]
				else:
					line = line[0:i] + line[i+1:]
				length = len(line)
	else:
		i += 1
print line
'''
f3.close()
f4.close()


while 1:
	line = f5.readline()
	if not line:
		break
	else:
		length = len(line)
		i = 0
		while i < length:
			if line[i] == "\\" and line[i+1] == "n":
				if i == 0:
					line = line[2:]
				else:
					line = line[0:i] + line[i+2:]
				length = len(line)
				if i < length:
					while line[i] == " ":
						if i == 0:
							line = line[1:]
						else:
							line = line[0:i] + line[i+1:]
						length = len(line)
			else:
				i += 1
		i = 0
		while i < length:
			if line[i] == "\\" and line[i+1] == "u":
				line = line[0:i] + line[i+6:]
				length = len(line)
				# i += 2
			else:
				i += 1
		i = 0
		while i < length:
			if line[i] == "'":
				line = line[0:i] + "'" + line[i:]
				i += 2
			else:
				i += 1

	'''
	index = line.find('", "')
	while index != -1:
		line = line[0:index-1] + line[index+4:]
		index = line.find('", "')
	'''
	f6.write(line)

'''
line = f.readline()
length = len(line)
i = 0
while i < length:
	if line[i] == "\n":
		if i == 0:
			line = line[1:]
		else:
			line = line[0:i] + line[i+1:]
		length = len(line)
		if i < length:
			while line[i] == " ":
				if i == 0:
					line = line[1:]
				else:
					line = line[0:i] + line[i+1:]
				length = len(line)
	else:
		i += 1
print line
'''
f5.close()
f6.close()
