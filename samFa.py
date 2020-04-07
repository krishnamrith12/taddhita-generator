import re

def prawyAhAra(start,iwMarker,sin=1,later=0):
	SivasUwra = [['a','i','u','A','I','U','N'],['q','Q','L','k'],['e','o','f'],['E','O','c'],['h','y','v','r','t'], ['l','N'],['F', 'm', 'f', 'N', 'n', 'm'], ['J', 'B', 'F'],['G', 'D', 'X', 'R'], ['j', 'b', 'g', 'd', 'x', 'S'], ['K', 'P', 'C', 'T', 'W', 'c','t', 'w','v'],['k', 'p', 'y'],['S','R','s','r'],['h','l']]
	prawyAhAra = ""	
	stIndex = tuple()
	iwIndex = tuple()
	iwprawyAhAra = ['N','k','f','c','t','N','m','F','R','S','v','y','r','l']
	for i,x in enumerate(SivasUwra):
		if start in x:
			stIndex = (i, x.index(start))
			break					

	for i,x in enumerate(SivasUwra):
		if iwMarker == x[-1]:
			iwIndex = (i, x.index(iwMarker))
			break	


	if sin == 1:
		prawyAhAra = prawyAhAra + '|'.join(SivasUwra[stIndex[0]][stIndex[1]:-1]) + '|'
	elif sin == 0:
		for i in SivasUwra[stIndex[0]][stIndex[1]:-1]:
			prawyAhAra = prawyAhAra + '|' + i[0]

	if  stIndex[0] < iwIndex[0]:	
		for i in range(stIndex[0]+1,iwIndex[0]+1):
			if sin == 1:
				prawyAhAra = prawyAhAra + '|'.join(SivasUwra[i][:-1]) + '|'
			elif sin == 0:	
				for k in SivasUwra[i][:-1]:
					prawyAhAra = prawyAhAra + '|' + k[0]


	return prawyAhAra[0:-1]







#1.1.1
def vrixXiH(var):
	if var == 'a':
		return 'A'
	if var == 'e':
		return 'E'
	if var == 'u':
		return 'O'

#1.1.2
def guNa(var):
	if var == 'a':
		return 'A'
	if var == 'u':
		return 'o'
	if var == 'i':
		return 'e'




print prawyAhAra('a','c')