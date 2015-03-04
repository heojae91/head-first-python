with open('/Users/Ashburn/HeadFirstPython/Chapter 5/hfpy_ch5_data/james.txt') as jaf:
	data = jaf.readline()
james = data.strip().split(',')
with open('/Users/Ashburn/HeadFirstPython/Chapter 5/hfpy_ch5_data/julie.txt') as juf:
	data = juf.readline()
julie = data.strip().split(',')
with open('/Users/Ashburn/HeadFirstPython/Chapter 5/hfpy_ch5_data/mikey.txt') as mif:
	data = mif.readline()
mikey = data.strip().split(',')
with open('/Users/Ashburn/HeadFirstPython/Chapter 5/hfpy_ch5_data/sarah.txt') as saf:
	data = saf.readline()
sarah = data.strip().split(',')

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))