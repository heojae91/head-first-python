
man = []
other = []

try:
	data = open('/Users/Ashburn/HeadFirstPython/Chapter 4/sketch.txt')
	
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print('The datafile is missing!')

try:
	man_file = open('/Users/Ashburn/HeadFirstPython/Chapter 4/man_data.txt', 'w')
	other_file = open('/Users/Ashburn/HeadFirstPython/Chapter 4/other_data.txt', 'w')

	print(man, file=man_file)
	print(other, file = other_file)

except IOError:
	print('File Error!')
finally:
	if 'data' in locals():
		data.close()
	man_file.close()
	other_file.close()