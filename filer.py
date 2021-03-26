f = open("thrfle.txt")
vwu = "t"
vtu = "T"
base = "0"
ful = f.read() 
for x in ful:
	if x == vwu:
		base = base + vtu
	else:
		base = base + x
print(base[1:])
		
		