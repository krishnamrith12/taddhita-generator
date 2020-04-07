from notify.all import *
from samFa import *

sup = [['su','O','jas'],['am','Ot','Sas'],['tA','ByAM','Bis'],
    ['fe','ByAM','Byas'],['fasi','ByAM','Byas'],['fas','os','Am'],
    ['fi','os','sup']]

upaxESa = ['aN','Pak']
prawyaya = list()
saMhiwa = {'o':['a']}

iFstems = [' ']
semanticSenses = ['apawyam','gowra','yuvAM']

tAp = ['tAp']

saMKya = ['xvi']

waxAja = ['aN','aF','iF','Nya','Fyaf']



svAxi = ['aN','Pak','Ayana']
sarvanAmasWAna = ['']


otherAffix = ['aN','iF','aF','PiF']

vqxXa = ['']

for item in sup:
	prawyaya.extend(item)


XAwupATaH = []
prawyaya = []

#1.1.7
def valPrinter(val):
	print val
	print type(val)
	print 'checkppoint'


saMyoga = Variable()
saMyoga.changed.connect(valPrinter)

def saMyoga_Finder(Sabxa):
	hal = prawyAhAra('h','l')
	word = Sabxa.split('+')[0]
	saMyoga.value = re.findall('['+hal+']['+hal+']+',word)	



#1.2.45



prAwipaxikam = Variable()
def prAwipaxikam_Finder(Sabxa):
	pList = list()
	print prawyaya
	for item in Sabxa.split('+'):
		if item not in XAwupATaH and item not in prawyaya:
			pList.append(item)
	

	#shall I just a make valid list and of gaNapATa
	# why apawya is not a prAwipaxika
	prAwipaxikam.value = pList
prAwipaxikam.changed.connect(valPrinter)
"""																																										

prAwipaxikam.changed.connect(IIThird46)
prAwipaxikam.changed.connect(IFour103)
"""
