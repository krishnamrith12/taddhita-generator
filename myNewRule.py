f = open('onlyapawya.py').read().split('\n')

classDef = list()

for item in f:

    if 'class IVone' in item:
        classDef.append(item)



for item in classDef:
    print item.split('(')[1].split('c)')[0]+'.register('+item.split(' ')[1].split('c(')[0]+')'