
"""
Adding string to environment

use WX notation
character level properties, before the character
~ anunAsikaM:1


Word level properties, after the character
! state:processed

"""


import re
import attributes
#from sUwranew import *

"""
Sabxa represents a sinlge character (phoneme/letter) that stores the
value as well as various properties of that particular character,
say whether it is an it marker etc.
"""


class Sabxa(object):

    def __init__(self, chara,properties = dict()):
        self.properties = dict()
        for item in properties.keys():
            self.properties[item]  = properties[item]
        self.properties['value'] = chara

    def putValue(self):
        return self.properties['value']

    def putProperties(self):
        print self.properties

    def addProperty(self,key,val):
        self.properties[key] = val

    def addProperties(self,extraDict = dict()):
        for item in extraDict.keys():
            self.properties[item] = extraDict[item]



"""
Collection of Sabxa objects that forms a coherent entity, say a pratyaya or a pada
The properties of that entity is encoded in the collection.
The class has follwoing attributes
items - list of Sabxa objects.
Characters in input text is converted to list of Sabxa objects
properties - A dictionary that contains all properties for the given
"""




class SabxaCollection(object):

    def __init__(self,inpText,properties=dict()):

        self.properties = dict()
        self.activesamFa = list()
        self.appliedRules = list()
        for item in properties.keys():
            self.properties[item] = properties[item]


        self.items = list()
        if type(inpText) == type(''):
            self.text2objs(inpText)
            self.labelWords()
        else:
            self.items.extend(inpText)

    def text2objs(self,chText):
        propDict = dict()
        begin = 0
        end = 0
        for chara in chText:
            if chara == '~':
                propDict['anunAsikaM'] = 1
            elif chara == '!':
                propDict['endWord'] = 1
            elif chara == ' ':
                wordProp = dict()
                propDict['virAmaH'] = 1
                self.items.append(Sabxa(chara,propDict))
                if 'endWord' in propDict.keys():
                    wordProp['state'] = 'processed'
                propDict = dict()
                try:
                    self.properties['words'].append(SabxaCollection(self.items[begin:end],wordProp))
                except:
                    self.properties['words'] = list()
                    self.properties['words'].append(SabxaCollection(self.items[begin:end],wordProp))

                begin = end + 1
                end = begin
            else:
                self.items.append(Sabxa(chara,propDict))
                propDict = dict()
                end = end +1
        try:
            self.properties['words'].append(SabxaCollection(self.items[begin:]))
        except:
            self.properties['words'] = list()
            self.properties['words'].append(SabxaCollection(self.items[begin:]))
    def objs2text(self):
        newText = str()
        for item in self.items:
            newText = newText + item.properties['value']
        return newText

    def labelWords(self):
        for item in self.properties['words']:
            labelSet = 0
            for stuff in attributes.sup:
                if item.objs2text() in stuff:
                    item.properties['sup'] = 1
                    labelSet = 1
            if item.objs2text() in attributes.semanticSenses:
                item.properties['semanticSense'] = 1
                labelSet = 1
            if item.objs2text() in attributes.tAp:
                item.properties['tAp'] = 1
                labelSet = 1
            if item.objs2text() in attributes.otherAffix:
                item.properties['otherAffix'] = 1
                labelSet = 1


            if labelSet == 0:
                item.properties['stem'] = 1


    def augment(self, sourceObj,newTet=None, newProps= None, startSpace = 1, endSpace = 1):
        sourceIndex = self.items.index(sourceObj.items[-1])
        newAugment = SabxaCollection(newTet,newProps)
        if len(self.items) > sourceIndex+1:
            if 'virAmaH' in self.items[sourceIndex+1].properties.keys():
                sourceIndex = sourceIndex+1
            if startSpace == 1:
                self.items = self.items[:sourceIndex+1] + newAugment.items +self.items[sourceIndex:]



    def updateTextval(self):
        self.properties['value'] = self.objs2text()

    def replace(self, replText="",newText="",replTxtIndex = None):
        itemText = self.objs2text()

        if replTxtIndex is None:
            itemSt = itemText.find(replText)
        else:
            itemSt = replTxtIndex
        if type(newText) == type(''):
            self.items = self.items[:itemSt] + SabxaCollection(newText).items + self.items[itemSt+len(replText):]
        else:
            self.items = self.items[:itemSt] + newText.items + self.items[itemSt+len(replText):]

    def elide(self, elideObj, space =0,word =0):

        if word == 1:
            for item in self.properties['words']:
                if elideObj.objs2text() in item.objs2text():
                    self.properties['words'].remove(item)

        if space == 1:
            try:
                if 'virAmaH' in self.items[self.items.index(elideObj.items[-1]) + 1].properties.keys():
                    del self.items[self.items.index(elideObj.items[-1]) + 1]
            except:
                pass

        if space == 0 and  word == 0:

            self.items.remove(elideObj)




"""
tin = "upagu fas! apawya~m"
env = SabxaCollection(tin)
print env.objs2text()
print env.properties


for item  in env.properties['words']:
    print item.objs2text(), item.properties


a = SabxaCollection('aN',{'state':'processed'})

env.replace('apawyam',a)

print env.objs2text()
"""