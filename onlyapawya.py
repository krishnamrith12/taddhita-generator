# -*- coding: utf-8 -*-
import re
from abc import ABCMeta, abstractmethod
from copy import deepcopy

from Sabxa import *
#import gaNapATa
from samFa import *
import sys
import attributes
import gaNapATa


class sUwra(object):

    def __init__(self, anu="", tex=""):
        self.properties = dict()
        self.properties['anuvriwwi'] = anu
        self.properties['sUwraText'] = tex
        self.regiRules = list()
        self.candidateList = list()
        self.flag = 0
        self.parent = None

    def register(self,regObj=None):
        self.regiRules.append(regObj)
        regObj.parent = self

    def superCheck(self,SabxarUpa, rule=None):
            self.flag = 0
            if rule is not None:
                print 'going to call particular rule check', rule
                self.flag = rule.check(SabxarUpa,rule=1)
                self.flag =1
            else:
                print 'Broadcast inside check',self
                self.broadcast(SabxarUpa)

            print 'finally',self.candidateList
            if len(self.candidateList) == 1:
                SabxarUpa.appliedRules.append(self.candidateList[0])
                self.candidateList[0].execute(SabxarUpa)
            return self.flag

    def execute(self, SabxarUpa, candiList=None):
        if len(self.candidateList) == 1:
            SabxarUpa.appliedRules.append(self.candidateList[0])
            self.candidateList[0].execute(SabxarUpa)
        self.candidateList= list()

    def check(self, SabxarUpa,rule=0):
        self.candidateList = []
        print 'inside check',self
        self.broadcast(SabxarUpa)
        if len(self.candidateList) == 1:
            self.parent.candidateList.extend(self.candidateList)
            if rule == 1:
                generalsUwra.candidateList.extend(self.candidateList)
        elif len(self.candidateList) > 1:
            self.resolve(SabxarUpa)
        print 'about to clean', self
        self.candidateList = []

#    def checkTrue(self, SabxarUpa):

    def broadcast(self, SabxarUpa):
        for item in self.regiRules:
            item.check(SabxarUpa)

    def resolveOld(self, SabxarUpa, candiList):
        self.candidateList.extend(candiList)
        print 'resolve for generalsuwra'
        print self.candidateList
        for item in self.candidateList:
            if item in SabxarUpa.appliedRules:
                self.candidateList.remove(item)
        if len(self.candidateList) ==0:
            print 'zero candidateList for generalsuwra resolve'


    def resolve(self, SabxarUpa, candiList):
        print 'resolve', self
        for item in candiList:
                for stuff in candiList:
                    try:
                        if stuff in item.optionalTo:
                            candiList.remove(stuff)
                            print candiList
                    except:
                        pass
        print candiList


        maxItem = candiList[0]
        for item in candiList:
            print item.ider,maxItem.ider
            if item.ider > maxItem.ider:
                maxItem = item
        print maxItem
        candiList = [maxItem]
        print candiList
        if len(candiList) == 1:
            self.parent.candidateList.extend(candiList)
            self.candidateList = []

        else:
            print 'more resolve needed'
            sys.exit()



class IIIone1c(sUwra):


    def __init__(self):
        super(IIIone1c, self).__init__()


class IVone76c(IIIone1c):

    def __init__(self):
        super(IVone76c, self).__init__()



class IVone82c(IVone76c):

    def __init__(self):
        super(IVone82c, self).__init__()


class IVone83c(IVone82c):

    def __init__(self):

        super(IVone83c, self).__init__()
        self.senses=['apawyam', 'gowra', 'yuvAM']

    def execute(self,SabxarUpa,replText="apawyam"):
        print 'IVone83 Execute',self
        aN = SabxaCollection('a~N',{'state':'upaxeSa'})
        SabxarUpa.replace(replText,aN)
        SabxarUpa.properties['waxXiwaprawyaya'] = aN
        SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
        for i in range(len(SabxarUpa.properties['words'])):
            if replText in SabxarUpa.properties['words'][i].objs2text():
                SabxarUpa.properties['words'][i] = aN
                SabxarUpa.activesamFa.append('upaxeSa')


class IVone84c(IVone83c):

    def __init__(self):
        super(IVone84c, self).__init__()
        self.specificity = ['semantic','morphological']
        self.ider = 41084


    def check(self, SabxarUpa, rule =0):
        print 'IVone84 Check'
        sensePresent = 1
        self.candidateList = []
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                if item.objs2text() in self.senses:
                    sensePresent = 1
        if sensePresent ==1:
            for item in SabxarUpa.properties['words']:
                if 'stem' in item.properties.keys():
                    if item.objs2text() in gaNapATa.aSvapawi:
                        self.parent.candidateList.extend(self.candidateList)
        self.candidateList = []


    def execute(self,SabxarUpa):
        print 'IVone84 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                super(IVone84c,self).execute(SabxarUpa,item.objs2text())



class IVone85c(IVone83c):

    def __init__(self):
        super(IVone85c, self).__init__()
        self.specificity = ['semantic','morphological']
        self.ider = 41085


    def check(self, SabxarUpa, rule =0):
        print 'IVone85 Check'
        sensePresent = 1
        self.candidateList = []
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                if item.objs2text() in self.senses:
                    sensePresent = 1
        if sensePresent ==1:
            for item in SabxarUpa.properties['words']:
                if 'stem' in item.properties.keys():
                    if item.objs2text() in ['xiwi','axiwi','Axiwya'] or 'pawi' == item.objs2text()[-4:]:
                        self.parent.candidateList.extend(self.candidateList)
        self.candidateList = []


    def execute(self,SabxarUpa):
        print 'IVone85 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()

                aN = SabxaCollection('Nya',{'state':'upaxeSa'})
                SabxarUpa.replace(replText,aN)
                SabxarUpa.properties['waxXiwaprawyaya'] = aN
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if replText in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = aN
                        SabxarUpa.activesamFa.append('upaxeSa')




class IVone86c(IVone83c):

    def __init__(self):
        super(IVone86c, self).__init__()
        self.specificity = ['semantic','morphological']
        self.ider = 41086


    def check(self, SabxarUpa, rule =0):
        print 'IVone86 Check'
        sensePresent = 1
        self.candidateList = []
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                if item.objs2text() in self.senses:
                    sensePresent = 1
        if sensePresent ==1:
            for item in SabxarUpa.properties['words']:
                if 'stem' in item.properties.keys():
                    if item.objs2text() in gaNapATa.uwsa:
                        self.parent.candidateList.extend(self.candidateList)


    def execute(self,SabxarUpa):
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()

                aN = SabxaCollection('aF',{'state':'upaxeSa'})
                SabxarUpa.replace(replText,aN)
                SabxarUpa.properties['waxXiwaprawyaya'] = aN
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if replText in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = aN
                        SabxarUpa.activesamFa.append('upaxeSa')


class IVone92c(IVone83c):

    def __init__(self):
        self.apawyam=['apawyam', 'gowra', 'yuvAM']
        super(IVone92c, self).__init__()
        self.ider = 41092


    def check(self, SabxarUpa, rule =0):
        print 'IVone92 Check'
        self.candidateList = []
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                if item.objs2text() in self.apawyam:
                    self.broadcast(SabxarUpa)
                    if len(self.candidateList) == 1:
                        self.parent.candidateList.extend(self.candidateList)
                    elif len(self.candidateList) == 0:
                        self.candidateList = [self]
                        self.parent.candidateList.extend(self.candidateList)
                    if len(self.candidateList) > 1:
                        self.resolve(SabxarUpa, self.candidateList)
                    if rule == 1:
                        generalsUwra.candidateList.extend(self.candidateList)
                    self.candidateList = []

    def execute(self,SabxarUpa):
        print 'IVone92 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                super(IVone92c,self).execute(SabxarUpa,item.objs2text())

"""
    def resolve(self, SabxarUpa, candiList):
        for item in candiList:
                for stuff in candiList:
                    try:
                        if stuff in item.optionalTo:
                            candiList.remove(stuff)
                            print candiList
                    except:
                        pass
        print candiList
        if len(candiList) == 1:
            self.parent.candidateList.extend(candiList)
        else:
            print 'more resolve needed'
            sys.exit()
"""
class IVone95c(IVone92c):

    def __init__(self):
        super(IVone95c, self).__init__()
        self.specificity = ['semantic','phonological']
        self.ider = 41095

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        if self.apawyam[0] in SabxarUpa.objs2text() or self.apawyam[1] in SabxarUpa.objs2text() or self.apawyam[2] in SabxarUpa.objs2text()  :
            for item in SabxarUpa.properties['words']:
                if 'stem' in item.properties.keys() and 'a' in item.objs2text()[-1]:
                    self.candidateList = [IVone95]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []

    def execute(self,SabxarUpa, replText='apawyam'):
        print 'IVone95 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                iF = SabxaCollection('i~F',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(),iF)
                SabxarUpa.properties['waxXiwaprawyaya'] = iF
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if SabxarUpa.properties['semanticSense'] in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = iF
                        SabxarUpa.activesamFa.append('upaxeSa')


class IVone96c(IVone92c):

    def __init__(self):
        super(IVone96c, self).__init__()
        self.ider = 41096

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        if self.apawyam[0] in SabxarUpa.objs2text() or self.apawyam[1] in SabxarUpa.objs2text() or self.apawyam[2] in SabxarUpa.objs2text()  :
            for item in SabxarUpa.properties['words']:
                if 'stem' in item.properties.keys() and item.objs2text() in gaNapATa.bAhu:
                    self.candidateList = [IVone96]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break
    def execute(self,SabxarUpa, replText='apawyam'):
        print 'IVone96 Execute'
        IVone95.execute(SabxarUpa)




class IVone97c(IVone92c):

    def __init__(self):
        super(IVone97c, self).__init__()
        self.ider = 41097

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone 97 check'
        if self.apawyam[0] in SabxarUpa.objs2text() or self.apawyam[1] in SabxarUpa.objs2text() or self.apawyam[2] in SabxarUpa.objs2text()  :
            for item in SabxarUpa.properties['words']:
                if 'stem' in item.properties.keys() and item.objs2text() in 'suXAwq':
                    self.candidateList = [IVone97]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []

    def execute(self,SabxarUpa, replText='apawyam'):
        print 'IVone96 Execute'
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                SabxarUpa.replace('q','akaf',SabxarUpa.items.index(item.items[-1]))
            break
        IVone95.execute(SabxarUpa)

class IVone98c(IVone92c):

    def __init__(self):
        super(IVone98c, self).__init__()
        self.ider = 41098

    def check(self, SabxarUpa, rule =0):
        print 'IVone98 check'
        self.candidateList = []
        if 'gowra' in SabxarUpa.objs2text() or 'yuvAM' in SabxarUpa.objs2text():
            self.broadcast(SabxarUpa)
            if len(self.candidateList) == 1:
                self.parent.candidateList.extend(self.candidateList)
            if len(self.candidateList) == 0:
                for item in SabxarUpa.properties['words']:
                    if item.objs2text() in gaNapATa.kuFja:
                        self.candidateList = [self]
                        self.parent.candidateList.extend(self.candidateList)
                        break
            if len(self.candidateList) > 1:
                self.resolve(SabxarUpa, self.candidateList)
            if rule == 1:
                generalsUwra.candidateList.extend(self.candidateList)
            self.candidateList = []


    def execute(self,SabxarUpa, replText='gowra'):
        print 'IVone98 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
        cPaF = SabxaCollection('cPa~F',{'state':'upaxeSa'})
        SabxarUpa.replace(replText,cPaF)
        SabxarUpa.properties['waxXiwaprawyaya'] = cPaF
        SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
        for i in range(len(SabxarUpa.properties['words'])):
            if SabxarUpa.properties['semanticSense'] in SabxarUpa.properties['words'][i].objs2text():
                SabxarUpa.properties['words'][i] = cPaF
                SabxarUpa.activesamFa.append('upaxeSa')

class IVone99c(IVone98c):

    def __init__(self):
        super(IVone99c, self).__init__()
        self.ider = 41099

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone99 check'
        for item in SabxarUpa.properties['words']:
            if item.objs2text() in gaNapATa.nada:
                self.candidateList = [IVone99]
                self.parent.candidateList.extend(self.candidateList)
                self.candidateList = []

    def execute(self, SabxarUpa, replText='gowra'):
        print 'IVone99 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()

        Pak = SabxaCollection('Pa~k',{'state':'upaxeSa'})
        SabxarUpa.replace(replText,Pak)
        SabxarUpa.properties['waxXiwaprawyaya'] = Pak
        SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
        for i in range(len(SabxarUpa.properties['words'])):
            if SabxarUpa.properties['semanticSense'] in SabxarUpa.properties['words'][i].objs2text():
                SabxarUpa.properties['words'][i] = Pak
                SabxarUpa.activesamFa.append('upaxeSa')



class IVone100c(IVone92c):

    def __init__(self):
        super(IVone100c, self).__init__()
        self.ider = 41100


    def check(self, SabxarUpa, rule = 0):
        self.candidateList = []
        print 'IVone100 check'
        aFlabel = 0
        for item in SabxarUpa.properties['words']:
            if 'otherAffix' in item.properties.keys():
                if 'aF' in item.objs2text():
                    aFlabel = 1

        if 'yuvAM' in SabxarUpa.objs2text():
            for item in SabxarUpa.properties['words']:
                if 'stem' in item.properties.keys():
                    if item.objs2text() in gaNapATa.bixa:
                        if gaNapATa.bixa.index(item.objs2text()) >= gaNapATa.bixa.index('hariwa'):
                            if aFlabel == 1:
                                self.candidateList = [IVone100]
                                self.parent.candidateList.extend(self.candidateList)
                                self.candidateList = []

    def execute(self,SabxarUpa, replText='yuvAM'):
        print 'IVone100 Execute'
        IVone99.execute(SabxarUpa, replText='yuvAM')



class IVone101c(IVone98c):

    def __init__(self):
        super(IVone101c, self).__init__()
        self.ider = 41101

    def check(self, SabxarUpa, rule = 0):
        self.candidateList = []
        print 'IVone101 check'
        aFlabel = 0
        for item in SabxarUpa.properties['words']:
            if 'otherAffix' in item.properties.keys():
                if 'yaF' in item.objs2text() or 'iF' in item.objs2text():
                    aFlabel = 1

        if 'yuvAM' in SabxarUpa.objs2text():
            if aFlabel == 1:
                self.candidateList = [IVone101]
                self.parent.candidateList.extend(self.candidateList)
                self.candidateList = []

    def execute(self,SabxarUpa, replText='yuvAM'):
        print 'IVone101 Execute'
        IVone99.execute(SabxarUpa, replText='yuvAM')





class IVone102c(IVone98c):

    def __init__(self):
        super(IVone102c, self).__init__()
        self.ider = 41102

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone102 check'
        if 'gowra' in SabxarUpa.objs2text():
            for item in SabxarUpa.properties['words']:
                if 'stem' in item.properties.keys():
                    if item.objs2text() in ['Saraxvaw', 'Sunaka', 'xarBa']:
                        y = raw_input('Are you using this in terms lineage of Bqgu,vawsa or AgrAyana: (y/n):')
                        if y == 'y':
                            self.candidateList = [IVone102]
                            self.parent.candidateList.extend(self.candidateList)
                            self.candidateList = []
                            y = ''
                            break

    def execute(self,SabxarUpa, replText='gowra'):
        print 'IVone102 Execute'
        IVone99.execute(SabxarUpa, replText='gowra')


class IVone103c(IVone98c):

    def __init__(self):
        super(IVone103c, self).__init__()
        self.ider = 41103
        self.optionalTo = [IVone95]

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone103 check'
        if 'gowra' in SabxarUpa.objs2text():
            for item in SabxarUpa.properties['words']:
                if 'stem' in item.properties.keys():
                    if item.objs2text() in ['xroNa', 'paqvawa', 'jIvanwa']:
                            self.candidateList = [IVone103]
                            self.parent.candidateList.extend(self.candidateList)
                            self.candidateList = []
                            break

    def execute(self,SabxarUpa, replText='gowra'):
        print 'IVone103 Execute'
        SabxarUpa.properties['alternate'] = deepcopy(SabxarUpa)
        SabxarUpa.appliedRules.append(IVone95)
        IVone99.execute(SabxarUpa.properties['alternate'], replText='gowra')
        IVone95.execute(SabxarUpa, replText = 'gowra')




class IVone104c(IVone98c):

    def __init__(self):
        super(IVone104c, self).__init__()
        self.ider = 41104


    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone104 check'
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                print 'inside 104'
                if item.objs2text() in gaNapATa.bixa:
                    y = raw_input('Are you using the same in indicating in lineage of a sage: (y/n)')
                    if y == 'n':
                        self.candidateList = [IVone104]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []

    def execute(self, SabxarUpa, replText='gowra'):
        print 'IVone104 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()

        aF = SabxaCollection('a~F',{'state':'upaxeSa'})
        SabxarUpa.replace(replText,aF)
        SabxarUpa.properties['waxXiwaprawyaya'] = aF
        SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
        for i in range(len(SabxarUpa.properties['words'])):
            if SabxarUpa.properties['semanticSense'] in SabxarUpa.properties['words'][i].objs2text():
                SabxarUpa.properties['words'][i] = aF
                SabxarUpa.activesamFa.append('upaxeSa')


class IVone105c(IVone98c):

    def __init__(self):
        super(IVone105c, self).__init__()
        self.ider = 41105


    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone105 check'
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in gaNapATa.garga:
                    self.candidateList = [IVone105]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []

    def execute(self, SabxarUpa, replText='gowra'):
        print 'IVone105 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()

        yaF = SabxaCollection('ya~F', {'state':'upaxeSa'} )
        SabxarUpa.replace(replText,yaF)
        SabxarUpa.properties['waxXiwaprawyaya'] = yaF
        SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
        for i in range(len(SabxarUpa.properties['words'])):
            if SabxarUpa.properties['semanticSense'] in SabxarUpa.properties['words'][i].objs2text():
                SabxarUpa.properties['words'][i] = yaF
                SabxarUpa.activesamFa.append('upaxeSa')


class IVone106c(IVone98c):

    def __init__(self):
        super(IVone106c, self).__init__()
        self.ider = 41106


    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone106 check'
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['maXu','baBru']:
                    y = raw_input('Do you indent to mean descendant of brAhmaNa or kOSika: (y/n)')
                    if y == 'y':
                        self.candidateList = [IVone106]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []

    def execute(self, SabxarUpa, replText='gowra'):
        print 'IVone106 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                IVone105.execute(SabxarUpa, replText=item.objs2text())
                break

class IVone107c(IVone98c):

    def __init__(self):
        super(IVone107c, self).__init__()
        self.ider = 41107


    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone107 check'
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['kapi','boXa']:
                    y = raw_input('Do you indent to mean descendant in lineage of afgirasa: (y/n)')
                    if y == 'y':
                        self.candidateList = [IVone107]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []

    def execute(self, SabxarUpa, replText='gowra'):
        print 'IVone107 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                IVone105.execute(SabxarUpa, replText=item.objs2text())
                break


class IVone108c(IVone98c):

    def __init__(self):
        super(IVone108c, self).__init__()
        self.ider = 41108


    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone108 check'
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['vawaNda']:
                    y = raw_input('Do you indent to mean descendant in lineage of afgirasa: (y/n)')
                    if y == 'y':
                        self.candidateList = [IVone108]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []

    def execute(self, SabxarUpa, replText='gowra'):
        print 'IVone108 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                IVone105.execute(SabxarUpa, replText=item.objs2text())
                break


class IVone110c(IVone98c):

    def __init__(self):
        super(IVone110c, self).__init__()
        self.ider = 41110



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone110 check'
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in gaNapATa.aSva:
                    self.candidateList = [IVone110]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []

    def execute(self, SabxarUpa, replText='gowra'):
        print 'IVone110 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                break
        PaF = SabxaCollection('Pa~F',{'state':'upaxeSa'})
        SabxarUpa.replace(replText,PaF)
        SabxarUpa.properties['waxXiwaprawyaya'] = PaF
        SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
        for i in range(len(SabxarUpa.properties['words'])):
            if 'gowra' in SabxarUpa.properties['words'][i].objs2text():
                SabxarUpa.properties['words'][i] = PaF
                SabxarUpa.activesamFa.append('upaxeSa')



class IVone111c(IVone98c):

    def __init__(self):
        super(IVone111c, self).__init__()
        self.ider = 41111



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone111 check'
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['Baqga']:
                    y = raw_input('Are you talking about some one in the country of wrigAqwa: (y/n)')
                    if y == 'y':
                        self.candidateList = [IVone111]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []

    def execute(self, SabxarUpa, replText='gowra'):
        print 'IVone111 Execute'
        IVone110.execute(SabxarUpa, replText='gowra')

#Implement Later
#class IVone109c(IVone98c):


class IVone112c(IVone92c):

    def __init__(self):
        super(IVone112c, self).__init__()
        self.ider = 41112



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone111 check'
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in gaNapATa.Siva:
                    self.candidateList = [IVone112]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone112 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                IVone83.execute(SabxarUpa,item.objs2text())


class IVone113c(IVone92c):

    def __init__(self):
        super(IVone113c, self).__init__()
        self.ider = 41113



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone113 check'
        vrddham = 100

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                for chars in item.items:
                    if chars.properties['value'] in prawyAhAra('a','c'):
                        if chars.properties['value'] in ['A','O','E']:
                            vrddham = 1
                        else:
                            vrddham = 0
                        break

            if vrddham <= 1:
                break

        if vrddham == 0:
            y = raw_input('Does your stem signify river or woman and want to mention it as name not as an adjective?')
            if y == 'y':
                self.candidateList = [IVone113]
                self.parent.candidateList.extend(self.candidateList)
                self.candidateList = []

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone113 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                IVone83.execute(SabxarUpa,item.objs2text())
                break

class IVone114c(IVone92c):

    def __init__(self):
        super(IVone114c, self).__init__()
        self.ider = 41114



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone114, check'

        y = raw_input('Did you intend to use qRi,anXaka,vqRNi,kuru? (y/n)')

        if y=='y':
            self.candidateList = [IVone114]
            self.parent.candidateList.extend(self.candidateList)
            self.candidateList = []

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone113 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                IVone83.execute(SabxarUpa,item.objs2text())


class IVone115c(IVone92c):

    def __init__(self):
        self.ider = 41115
        super(IVone115c, self).__init__()



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone115 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in attributes.saMKya:
                    del item.properties['stem']
                    item.properties['saMKya'] = 1
                    break

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if 'mAwq' in item.objs2text():
                    if 'sam'in item.objs2text() or 'Baxr' in item.objs2text():
                        self.candidateList = [IVone115]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []
                        break
                    for stuff in attributes.saMKya:
                        if stuff in item.objs2text():
                            self.candidateList = [IVone115]
                            self.parent.candidateList.extend(self.candidateList)
                            self.candidateList = []
                            break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone115 Execute'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                SabxarUpa.replace('q','u')
                break

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                IVone83.execute(SabxarUpa,item.objs2text())



class IVone116c(IVone92c):

    def __init__(self):
        super(IVone116c, self).__init__()
        self.ider = 41116



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone115 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['kanyA']:
                    self.candidateList = [IVone116]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone116 Execute'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                SabxarUpa.replace('kanyA','kanIna')
                break

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                IVone83.execute(SabxarUpa,item.objs2text())






class IVone117c(IVone92c):

    def __init__(self):
        super(IVone117c, self).__init__()
        self.ider = 41117



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone117 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['vikarNa','Sufga','Cagala']:
                    y = raw_input('Do you indent to mean descendant in lineage of vawsa,BaraxvAja,awri: (y/n)')
                    if y == 'y':
                        self.candidateList = [IVone117]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone117 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                IVone83.execute(SabxarUpa,item.objs2text())








class IVone118c(IVone92c):

    def __init__(self):
        super(IVone118c, self).__init__()
        self.ider = 41118
        self.optionalTo = [IVone95]



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone118 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['pIlA']:
                    self.candidateList = [IVone118]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []



    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone118 Execute'
        SabxarUpa.properties['alternate'] = deepcopy(SabxarUpa)
        SabxarUpa.appliedRules.append(IVone121)

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                SabxarUpa.properties['alternate'].properties['semanticSense'] = item.objs2text()
                IVone83.execute(SabxarUpa.properties['alternate'], replText=item.objs2text())
                IVone121.execute(SabxarUpa, replText = item.objs2text())


class IVone119c(IVone92c):

    def __init__(self):
        super(IVone119c, self).__init__()
        self.ider = 41119
        self.optionalTo = [IVone95]


    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone119 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['maNdUka']:
                    self.candidateList = [IVone119]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []



    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone119 Execute'
        SabxarUpa.properties['alternate'] = deepcopy(SabxarUpa)
        SabxarUpa.properties['alternate2'] = deepcopy(SabxarUpa)

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                SabxarUpa.properties['alternate'].properties['semanticSense'] = item.objs2text()
                SabxarUpa.properties['alternate2'].properties['semanticSense'] = item.objs2text()

                Dak = SabxaCollection('Da~k',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(),Dak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Dak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']

                aN = SabxaCollection('a~N',{'state':'upaxeSa'})
                SabxarUpa.properties['alternate'].replace(item.objs2text(),aN)
                SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya'] = aN
                SabxarUpa.properties['alternate'].properties['prawyaya'] = SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya']



                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Dak
                        SabxarUpa.activesamFa.append('upaxeSa')
        SabxarUpa.appliedRules.append(IVone95)
        IVone95.execute(SabxarUpa.properties['alternate2'])



class IVone120c(IVone92c):

    def __init__(self):
        super(IVone120c, self).__init__()
        self.ider = 41120



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone120 check'

        for item in SabxarUpa.properties['words']:
            self.candidateList = [IVone120]
            if 'tAp' in item.properties.keys():
                self.parent.candidateList.extend(self.candidateList)
                self.candidateList = []



    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone120 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Dak = SabxaCollection('Da~k',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Dak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Dak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if 'apawyam' in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Dak
                        SabxarUpa.activesamFa.append('upaxeSa')


class IVone121c(IVone92c):

    def __init__(self):
        super(IVone121c, self).__init__()
        self.ider = 41121



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone121 check'
        tApkey = 100
        vowCount = 0

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                for chars in item.items:
                    if chars.properties['value'] in prawyAhAra('a','c'):
                        vowCount = vowCount + 1
                if vowCount == 2:
                    self.broadcast(SabxarUpa)
                    if len(self.candidateList) == 1:
                        self.parent.candidateList.extend(self.candidateList)


                    if len(self.candidateList) == 0:
                        for item in SabxarUpa.properties['words']:
                            if 'tAp' in item.properties.keys():
                                tApkey = 1
                                break
                        if tApkey == 1:
                            self.candidateList = [IVone121]
                            self.parent.candidateList.extend(self.candidateList)
                            self.candidateList = []
                            break



    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone121 Execute'
        IVone120.execute(SabxarUpa,replText=='apawyam')


class IVone122c(IVone121c):

    def __init__(self):
        super(IVone122c, self).__init__()
        self.ider = 41122
        self.specificity = ['semantic','phonological']



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone122     check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if 'i' in item.items[-1].properties['value']:
                    if item.objs2text() not in attributes.iFstems:
                            self.candidateList = [IVone122]
                            self.parent.candidateList.extend(self.candidateList)
                            self.candidateList = []
                            break



    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone122 Execute'
        IVone120.execute(SabxarUpa,replText=='apawyam')




class IVone123c(IVone92c):

    def __init__(self):
        super(IVone123c, self).__init__()
        self.ider = 41123



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone123 check'


        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in gaNapATa.SuBra:
                    self.candidateList = [IVone123]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break



    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone123 Execute'
        IVone120.execute(SabxarUpa)


class IVone124c(IVone92c):

    def __init__(self):
        super(IVone124c, self).__init__()
        self.ider = 41124



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone123 check'


        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['vikarNa','kuRiwaka']:
                    y = raw_input('Do you mean to talk about descendant of kaSyapa: (y/n)')
                    if y == 'y':
                        self.candidateList = [IVone124]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []
                        break



    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone124 Execute'
        IVone120.execute(SabxarUpa)


class IVone125c(IVone92c):

    def __init__(self):
        super(IVone125c, self).__init__()
        self.ider = 41125



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone125 check'


        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['BrU']:
                    self.candidateList = [IVone125]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break



    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone125 Execute'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                #check the augment function, spacing thinghy not understood
                SabxarUpa.augment(item,'vuk',{'augment':'1'})
        IVone120.execute(SabxarUpa)


class IVone126c(IVone92c):

    def __init__(self):
        super(IVone126c, self).__init__()
        self.ider = 41126



    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone125 check'


        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in gaNapATa.kalyANI:
                    self.candidateList = [IVone126]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break



    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone126 Execute'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                SabxarUpa.replace(item.items[-1].properties['value'],'inaf')
                break
        IVone120.execute(SabxarUpa)


class IVone127c(IVone92c):

    def __init__(self):
        super(IVone127c, self).__init__()
        self.optionalTo= [IVone120]
        self.ider = 41127


    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone127 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['kulatA']:
                    self.candidateList = [IVone127]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone127 Execute'
        SabxarUpa.properties['alternate'] = deepcopy(SabxarUpa)
        IVone120.execute(SabxarUpa)
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                SabxarUpa.properties['alternate'].replace(item.items[-1].properties['value'],'inaf')
                break
        IVone120.execute(SabxarUpa.properties['alternate'])


class IVone128c(IVone92c):

    def __init__(self):
        super(IVone128c, self).__init__()
        self.ider = 41128

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone128 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['catakA']:
                    self.candidateList = [IVone128]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone128 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Erak = SabxaCollection('Era~k',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Erak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Erak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Erak
                        SabxarUpa.activesamFa.append('upaxeSa')


class IVone129c(IVone92c):

    def __init__(self):
        super(IVone129c, self).__init__()
        self.ider = 41129

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone129 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['goXA']:
                    if SabxarUpa.properties['tradition'] != 'northern':
                        self.candidateList = [IVone129]
                    else:
                        self.candidateList = [IVone130]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone129 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('Dra~k',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if 'apawyam' in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')



class IVone130c(IVone129c):

    def __init__(self):
        super(IVone130c, self).__init__()
        self.ider = 41130


    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone130 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Arak = SabxaCollection('Ara~k',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Arak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Arak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Arak
                        SabxarUpa.activesamFa.append('upaxeSa')


class IVone131c(IVone92c):

    def __init__(self):
        super(IVone131c, self).__init__()
        self.ider = 41131
        self.optionalTo = [IVone120]

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone131 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['kRuxrA']:

                    self.candidateList = [IVone131]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone131 Execute'
        SabxarUpa.properties['alternate'] = deepcopy(SabxarUpa)

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                SabxarUpa.properties['alternate'].properties['semanticSense'] = item.objs2text()

                aN = SabxaCollection('Drak',{'state':'upaxeSa'})
                SabxarUpa.properties['alternate'].replace(item.objs2text(),aN)
                SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya'] = aN
                SabxarUpa.properties['alternate'].properties['prawyaya'] = SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya']



                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['alternate'].properties['words'][i].objs2text():
                        SabxarUpa.properties['alternate'].properties['words'][i] = aN
                        SabxarUpa.properties['alternate'].activesamFa.append('upaxeSa')
        SabxarUpa.appliedRules.append(IVone120)
        IVone120.execute(SabxarUpa)



class IVone132c(IVone92c):

    def __init__(self):
        super(IVone132c, self).__init__()
        self.ider = 41132

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone132 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['piwqRvasq']:

                    self.candidateList = [IVone132]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone132 Execute'
        SabxarUpa.properties['alternate'] = deepcopy(SabxarUpa)
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('CaN',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')

        IVone133.execute(SabxarUpa.properties['alternate'])


class IVone133c(IVone132c):

    def __init__(self):
        super(IVone133c, self).__init__()
        self.ider = 41133


    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone133 Execute'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                SabxarUpa.elide(item.items[-1])


            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('Dak',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')
                SabxarUpa.appliedRules.append(IVone133)



class IVone134c(IVone92c):

    def __init__(self):
        super(IVone134c, self).__init__()
        self.ider = 41134

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone134 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['mAwqRvsq']:

                    self.candidateList = [IVone134]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone134 Execute'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                SabxarUpa.elide(item.items[-1])


            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('Dak',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')










class IVone135c(IVone92c):

    def __init__(self):
        super(IVone135c, self).__init__()
        self.ider = 41135
        self.fourLegged = ['kamaNdalu','SunwibAhu']

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone132 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in self.fourLegged:

                    self.candidateList = [IVone135]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone135 Execute'
        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('Da~F',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')




class IVone136c(IVone92c):

    def __init__(self):
        super(IVone136c, self).__init__()
        self.ider = 41136

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone136 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in gaNapATa.gqRti:

                    self.candidateList = [IVone136]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone136 Execute'

        IVone135.execute(SabxarUpa)


class IVone137c(IVone92c):

    def __init__(self):
        self.ider = 41137
        super(IVone137c, self).__init__()

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone137 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['rAjan','Svasura']:

                    self.candidateList = [IVone137]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone137 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('yaw',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')


class IVone138c(IVone92c):

    def __init__(self):

        super(IVone138c, self).__init__()
        self.ider = 41138

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone138 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['kRawra']:

                    self.candidateList = [IVone138]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone138 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('GaH',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')




class IVone139c(IVone92c):

    def __init__(self):
        super(IVone139c, self).__init__()
        self.ider = 41139

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone139 check'
        stemCount = 0
        immediateStem = 0
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                stemCount = stemCount +1
                if item.objs2text() in ['kula']:

                    self.candidateList = [IVone139]
                    if stemCount == 1 or immediateStem == 1:
                        self.candidateList = [IVone140]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break
                elif 'kula' in item.objs2text()[-4:]:
                    y = raw_input('Is the stem a samasa? (y/n)')
                    if y == 'y':
                        self.candidateList = [IVone139]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []
                        break
                elif 'kula' in item.objs2text():
                    if 'kula' not in item.objs2text()[-4:]:
                        self.candidateList = [IVone140]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []
                        break
            if 'stem' in item.properties.keys():
                immediateStem = 1
            else:

                immediateStem = 0

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone138 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('KaH',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')


class IVone140c(IVone139c):

    def __init__(self):
        self.ider = 41140
        super(IVone140c, self).__init__()




    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone140 Execute'
        SabxarUpa.properties['alternate'] = deepcopy(SabxarUpa)
        SabxarUpa.properties['alternate2'] = deepcopy(SabxarUpa)
        SabxarUpa.appliedRules.append(IVone139)

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                SabxarUpa.properties['alternate'].properties['semanticSense'] = item.objs2text()
                SabxarUpa.properties['alternate2'].properties['semanticSense'] = item.objs2text()

                Drak = SabxaCollection('ya~w',{'state':'upaxeSa'})
                DakaF = SabxaCollection('Daka~F',{'state':'upaxeSa'})

                SabxarUpa.properties['alternate'].replace(item.objs2text(), Drak)
                SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['alternate'].properties['prawyaya'] = SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['alternate'].properties['words'])):
                    if 'apawyam' in SabxarUpa.properties['alternate'].properties['words'][i].objs2text():
                        SabxarUpa.properties['alternate'].properties['words'][i] = Drak
                        SabxarUpa.properties['alternate'].activesamFa.append('upaxeSa')

                SabxarUpa.properties['alternate2'].replace(item.objs2text(), DakaF)
                SabxarUpa.properties['alternate2'].properties['waxXiwaprawyaya'] = DakaF
                SabxarUpa.properties['alternate2'].properties['prawyaya'] = SabxarUpa.properties['alternate2'].properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['alternate2'].properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['alternate2'].properties['words'][i].objs2text():
                        SabxarUpa.properties['alternate2'].properties['words'][i] = DakaF
                        SabxarUpa.properties['alternate2'].activesamFa.append('upaxeSa')
                IVone139.execute(SabxarUpa)


class IVone141c(IVone92c):

    def __init__(self):
        super(IVone141c, self).__init__()
        self.ider = 41141
        self.optionalTo = [IVone139]


    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone141 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['mahAkula']:

                    self.candidateList = [IVone141]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break


    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone141 Execute'
        SabxarUpa.properties['alternate'] = deepcopy(SabxarUpa)
        SabxarUpa.properties['alternate2'] = deepcopy(SabxarUpa)
        SabxarUpa.appliedRules.append(IVone139)

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                SabxarUpa.properties['alternate'].properties['semanticSense'] = item.objs2text()
                SabxarUpa.properties['alternate2'].properties['semanticSense'] = item.objs2text()

                Drak = SabxaCollection('a~F',{'state':'upaxeSa'})
                DakaF = SabxaCollection('Ka~F',{'state':'upaxeSa'})

                SabxarUpa.properties['alternate'].replace(item.objs2text(), Drak)
                SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['alternate'].properties['prawyaya'] = SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['alternate'].properties['words'])):
                    if 'apawyam' in SabxarUpa.properties['alternate'].properties['words'][i].objs2text():
                        SabxarUpa.properties['alternate'].properties['words'][i] = Drak
                        SabxarUpa.properties['alternate'].activesamFa.append('upaxeSa')

                SabxarUpa.properties['alternate2'].replace(item.objs2text(), DakaF)
                SabxarUpa.properties['alternate2'].properties['waxXiwaprawyaya'] = DakaF
                SabxarUpa.properties['alternate2'].properties['prawyaya'] = SabxarUpa.properties['alternate2'].properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['alternate2'].properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['alternate2'].properties['words'][i].objs2text():
                        SabxarUpa.properties['alternate2'].properties['words'][i] = DakaF
                        SabxarUpa.properties['alternate2'].activesamFa.append('upaxeSa')
                IVone139.execute(SabxarUpa)

class IVone142c(IVone92c):

    def __init__(self):
        super(IVone142c, self).__init__()
        self.ider = 41142
        self.optionalTo = [IVone139]


    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone142 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['duRkula']:

                    self.candidateList = [IVone142]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break


    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone142 Execute'
        SabxarUpa.properties['alternate'] = deepcopy(SabxarUpa)
        SabxarUpa.appliedRules.append(IVone139)

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                SabxarUpa.properties['alternate'].properties['semanticSense'] = item.objs2text()

                Drak = SabxaCollection('Da~F',{'state':'upaxeSa'})

                SabxarUpa.properties['alternate'].replace(item.objs2text(), Drak)
                SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['alternate'].properties['prawyaya'] = SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['alternate'].properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['alternate'].properties['words'][i].objs2text():
                        SabxarUpa.properties['alternate'].properties['words'][i] = Drak
                        SabxarUpa.properties['alternate'].activesamFa.append('upaxeSa')

                IVone139.execute(SabxarUpa)









class IVone143c(IVone92c):

    def __init__(self):
        super(IVone143c, self).__init__()
        self.ider = 41143

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone143 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['svasq']:

                    self.candidateList = [IVone143]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone143 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('CaH',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')



class IVone144c(IVone92c):

    def __init__(self):
        super(IVone144c, self).__init__()
        self.ider = 41144

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone144 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['BrAwq']:
                    y = raw_input('Do you intend sapatna here? (y/n):')
                    if y == 'n':
                        self.candidateList = [IVone144]
                    elif y == 'y':
                        self.candidateList = [IVone145]

                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone144 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('vyaw',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if 'apawyam' in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')

class IVone145c(IVone144c):

    def __init__(self):
        super(IVone145c, self).__init__()
        self.ider = 41145


    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone145 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('vyan',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if 'apawyam' in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')


class IVone146c(IVone92c):

    def __init__(self):
        super(IVone146c, self).__init__()
        self.ider = 41146

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone146 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in gaNapATa.revawI:
                    self.candidateList = [IVone146]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone146 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('Ta~k',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')


class IVone147c(IVone92c):

    def __init__(self):
        super(IVone147c, self).__init__()
        self.ider = 41147

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone147 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if 'gowra' in SabxarUpa.objs2text() or 'yuvAM' in SabxarUpa.objs2text():
                    y = raw_input('Do you intend a female of gotra derivate with a signifying reproach ?')
                    if y == 'y':
                        self.candidateList = [IVone147]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []
                        break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone147 Execute'
        SabxarUpa.properties['alternate'] = deepcopy(SabxarUpa)

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                SabxarUpa.properties['alternate'].properties['semanticSense'] = item.objs2text()

                Drak = SabxaCollection('Na',{'state':'upaxeSa'})

                SabxarUpa.properties['alternate'].replace(item.objs2text(), Drak)
                SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['alternate'].properties['prawyaya'] = SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['alternate'].properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['alternate'].properties['words'][i].objs2text():
                        SabxarUpa.properties['alternate'].properties['words'][i] = Drak
                        SabxarUpa.properties['alternate'].activesamFa.append('upaxeSa')

                IVone146.execute(SabxarUpa)




class IVone148c(IVone92c):

    def __init__(self):
        super(IVone148c, self).__init__()
        self.ider = 41148

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        vqxXam = 100
        print 'IVone148 check'
        PiFflag = 0


        for item in SabxarUpa.properties['words']:
            if 'otherAffix' in item.properties.keys():
                if 'PiF' in item.objs2text():
                    PiFflag = 1


        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                for chars in item.items:
                    if chars.properties['value'] in prawyAhAra('a','c'):
                        if chars.properties['value'] in ['A','E','O']:
                            vqxXam = 1
                        else:
                            vqxXam = 0
                        break
                if 'gowra' in SabxarUpa.objs2text() or 'yuvAM' in SabxarUpa.objs2text():
                    if item.objs2text() in ['PANtAhqwi','mimawa']:
                        y3 = raw_input('Do you intend a sOvIra gowra: (y/n)')
                        if y3 == 'y':
                            self.candidateList = [IVone150]
                            self.parent.candidateList.extend(self.candidateList)
                            self.candidateList = []
                            break

                    y = raw_input('Do you intend a sOvIra gowra with an intention of reproach who is an apatya of kutsana: (y/n)')
                    if y == 'y' and vqxXam == 1:
                        if PiFflag == 1:
                            self.candidateList = [IVone149]
                        elif PiFflag == 0:
                            self.candidateList = [IVone148]

                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []
                        break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone148 Execute'

        IVone146.execute(SabxarUpa)



class IVone149c(IVone148c):

    def __init__(self):
        super(IVone149c, self).__init__()
        self.ider = 41149


    def execute(self, SabxarUpa, replText='apawyam'):
            print 'IVone149 Execute'
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('Ca',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')


class IVone150c(IVone148c):

    def __init__(self):
        super(IVone150c, self).__init__()
        self.ider = 41150


    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone150 Execute'
        SabxarUpa.properties['alternate'] = deepcopy(SabxarUpa)

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                SabxarUpa.properties['alternate'].properties['semanticSense'] = item.objs2text()

                Drak = SabxaCollection('Na',{'state':'upaxeSa'})

                SabxarUpa.properties['alternate'].replace(item.objs2text(), Drak)
                SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['alternate'].properties['prawyaya'] = SabxarUpa.properties['alternate'].properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['alternate'].properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['alternate'].properties['words'][i].objs2text():
                        SabxarUpa.properties['alternate'].properties['words'][i] = Drak
                        SabxarUpa.properties['alternate'].activesamFa.append('upaxeSa')
                IVone149.execute(SabxarUpa)

	#add for Pif


class IVone151c(IVone92c):

    def __init__(self):
        super(IVone151c, self).__init__()
        self.ider = 41151

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone151 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in gaNapATa.kuru:
                    self.candidateList = [IVone151]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone151 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('NyaH',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')








class IVone152c(IVone92c):

    def __init__(self):
        super(IVone152c, self).__init__()
        self.ider = 41152

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone152 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if 'sena' in item.objs2text()[-4:] or 'lakRaNa' in item.objs2text():

                    if SabxarUpa.properties['tradition'] == 'northern':
                        self.candidateList = [IVone153]
                    else:
                        self.candidateList = [IVone152]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break
                else:
                    y = raw_input('Do you intend an artisan? (y/n)')
                    if y == 'y':

                        if SabxarUpa.properties['tradition'] == 'northern':
                            self.candidateList = [IVone153]
                        else:
                            self.candidateList = [IVone152]
                        self.parent.candidateList.extend(self.candidateList)
                        self.candidateList = []
                        break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone151 Execute'
        IVone151.execute(SabxarUpa)




class IVone153c(IVone152c):

    def __init__(self):
        super(IVone153c, self).__init__()
        self.ider = 41153


    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone153 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('iF',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')



class IVone154c(IVone92c):

    def __init__(self):
        super(IVone154c, self).__init__()
        self.ider = 41154

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone154 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in gaNapATa.wika:
                    self.candidateList = [IVone154]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone154 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('Pi~F',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')



class IVone155c(IVone92c):

    def __init__(self):
        super(IVone155c, self).__init__()
        self.ider = 41155

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []

        print 'IVone155 check'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                if item.objs2text() in ['kOSalya','kArmArya']:
                    self.candidateList = [IVone155]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone155 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                IVone154.execute(SabxarUpa)





class IVone156c(IVone92c):

    def __init__(self):
        super(IVone156c, self).__init__()
        self.ider = 41156

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        setLabel = 0
        print 'IVone156 check'
        ac = prawyAhAra('a','c')
        acCounter = 0
        for item in SabxarUpa.properties['words']:
            if 'otherAffix' in item.properties.keys():
                if 'aN' in item.objs2text():
                    setLabel = 1
                    break
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                for chars in item.items:
                    if chars.properties['value'] in ac:
                        acCounter = acCounter + 1
                if acCounter == 2 and setLabel == 1:
                    self.candidateList = [IVone156]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone156 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                IVone155.execute(SabxarUpa)



class IVone159c(IVone92c):

    def __init__(self):
        super(IVone159c, self).__init__()
        self.ider = 41159

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone159 check'
        ac = prawyAhAra('a','c')
        acCounter = 0
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                for chars in item.items:
                    if chars.properties['value'] in ac:
                        if chars.properties['value'] in ['A','E','O']:
                            acCounter = 1
                        break
                if acCounter == 1 and 'puwra' == item.objs2text()[-5:] and SabxarUpa.properties['tradition'] == 'northern':
                    self.candidateList = [IVone159]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone156 Execute'

        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                SabxarUpa.augment(item,'kuk',{'augment':1})

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                IVone154.execute(SabxarUpa)

class IVone160c(IVone92c):

    def __init__(self):
        super(IVone160c, self).__init__()
        self.ider = 41160

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        print 'IVone159 check'
        ac = prawyAhAra('a','c')
        acCounter = 0
        for item in SabxarUpa.properties['words']:
            if 'stem' in item.properties.keys():
                for chars in item.items:
                    if chars.properties['value'] in ac:
                        if chars.properties['value'] not in ['A','E','O']:
                            acCounter = 1
                        break
                if acCounter == 1 and SabxarUpa.properties['tradition'] == 'eastern':
                    self.candidateList = [IVone160]
                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone160 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('Pi~n',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')





class IVone166c(IVone92c):

    def __init__(self):
        super(IVone166c, self).__init__()
        self.ider = 41166

    def check(self, SabxarUpa, rule=0):
        self.candidateList = []
        setLabel = 0
        print 'IVone166 check'
        acCounter = 0
        vqxXaC = 0
        for item in SabxarUpa.properties['words']:

            if 'stem' in item.properties.keys():
                y = raw_input('Do you intend a region with Kshatriya signifcation? (y/n):')
                if y == 'y':
                    self.candidateList = [IVone166]
                    if item.objs2text() in ['sAlveya','gAnXAri']:
                        self.candidateList = [IVone167]
                    elif 'magaXa' in item.objs2text() or 'kalifga' in item.objs2text() or 'sUramasa' in item.objs2text():
                        self.candidateList = [IVone168]
                    elif 'kosala' in item.objs2text() or 'ajAxa' in item.objs2text() or 'i' in item.objs2text()[-1]:
                        self.candidateList[IVone169]
                    elif 'kuru' in item.objs2text() or 'n' in item.objs2text()[0]:
                        self.candidateList[IVone170]
                    elif 'prawyagraWa' in item.objs2text() or 'kAlakUta' in item.objs2text() or 'aSmaka' in item.objs2text():
                        self.candidateList[IVone171]
                    else:
                        ac = prawyAhAra('a','c')
                        for chars in item.items:
                            if chars.properties['value'] in ac:
                                acCounter = acCounter + 1
                                if chars.properties['value'] in ['A','E','O']:
                                    vqxXaC = 1
                                    break

                        if acCounter == 1 and vqxXaC == 1:
                            self.candidateList= [IVone169]
                        elif acCounter == 2:
                            self.candidateList= [IVone168]

                    self.parent.candidateList.extend(self.candidateList)
                    self.candidateList = []
                    break

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone146 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('a~F',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')


class IVone167c(IVone166c):

    def __init__(self):
        super(IVone167c, self).__init__()
        self.ider = 41167

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone167 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('a~F',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')

class IVone168c(IVone166c):

    def __init__(self):
        super(IVone168c, self).__init__()
        self.ider = 41168

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone168 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('a~N',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')



class IVone169c(IVone166c):

    def __init__(self):
        super(IVone169c, self).__init__()
        self.ider = 41169

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone169 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('Fya~f',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')




class IVone170c(IVone166c):

    def __init__(self):
        super(IVone170c, self).__init__()
        self.ider = 41170

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone170 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('Nya',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')



class IVone171c(IVone166c):

    def __init__(self):
        super(IVone171c, self).__init__()
        self.ider = 41171

    def execute(self, SabxarUpa, replText='apawyam'):
        print 'IVone171 Execute'

        for item in SabxarUpa.properties['words']:
            if 'semanticSense' in item.properties.keys():
                SabxarUpa.properties['semanticSense'] = item.objs2text()
                Drak = SabxaCollection('iF',{'state':'upaxeSa'})
                SabxarUpa.replace(item.objs2text(), Drak)
                SabxarUpa.properties['waxXiwaprawyaya'] = Drak
                SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
                for i in range(len(SabxarUpa.properties['words'])):
                    if item.objs2text() in SabxarUpa.properties['words'][i].objs2text():
                        SabxarUpa.properties['words'][i] = Drak
                        SabxarUpa.activesamFa.append('upaxeSa')


generalsUwra = sUwra()
IIIone1 = IIIone1c()
IVone76 = IVone76c()
IVone82 = IVone82c()
IVone83 = IVone83c()
IVone92 = IVone92c()
IVone95 = IVone95c()
IVone96 = IVone96c()
IVone97 = IVone97c()
IVone98 = IVone98c()
IVone99 = IVone99c()
IVone100 = IVone100c()

IVone102 = IVone102c()
IVone103 = IVone103c()
IVone104 = IVone104c()
IVone105 = IVone105c()
IVone106 = IVone106c()
IVone107 = IVone107c()
IVone108 = IVone108c()
IVone110 = IVone110c()
IVone111 = IVone111c()
IVone112 = IVone112c()
IVone113 = IVone113c()
IVone114 = IVone114c()
IVone115 = IVone115c()
IVone116 = IVone116c()
IVone117 = IVone117c()
IVone118 = IVone118c()
IVone119 = IVone119c()
IVone120 = IVone120c()
IVone121 = IVone121c()
IVone122 = IVone122c()
IVone123 = IVone123c()
IVone124 = IVone124c()
IVone125 = IVone125c()
IVone126 = IVone126c()
IVone127 = IVone127c()
IVone128 = IVone128c()
IVone129 = IVone129c()
IVone130 = IVone130c()
IVone131 = IVone131c()
IVone132 = IVone132c()
IVone133 = IVone133c()
IVone134 = IVone134c()
IVone135 = IVone135c()
IVone136 = IVone136c()
IVone137 = IVone137c()
IVone138 = IVone138c()
IVone139 = IVone139c()
IVone140 = IVone140c()
IVone141 = IVone141c()
IVone142 = IVone142c()
IVone143 = IVone143c()
IVone144 = IVone144c()
IVone145 = IVone145c()
IVone146 = IVone146c()
IVone147 = IVone147c()
IVone148 = IVone148c()
IVone149 = IVone149c()
IVone150 = IVone150c()
IVone151 = IVone151c()
IVone152 = IVone152c()
IVone153 = IVone153c()
IVone154 = IVone154c()
IVone155 = IVone155c()
IVone156 = IVone156c()
IVone159 = IVone159c()
IVone160 = IVone160c()

"""
IVone157 = IVone157c()
IVone158 = IVone158c()
IVone161 = IVone161c()
IVone162 = IVone162c()
IVone163 = IVone163c()
IVone164 = IVone164c()
IVone165 = IVone165c()
"""
IVone166 = IVone166c()
IVone167 = IVone167c()
IVone168 = IVone168c()
IVone169 = IVone169c()
IVone170 = IVone170c()
IVone171 = IVone171c()

"""
IVone172 = IVone172c()
IVone173 = IVone173c()
IVone174 = IVone174c()
"""


generalsUwra.register(IIIone1)

IIIone1.register(IVone76)
IVone76.register(IVone82)
IVone82.register(IVone83)
IVone83.register(IVone92)
IVone92.register(IVone98)
IVone92.register(IVone95)
IVone92.register(IVone96)
IVone92.register(IVone97)
IVone92.register(IVone100)
IVone98.register(IVone99)
IVone98.register(IVone102)
IVone98.register(IVone103)
IVone98.register(IVone104)
IVone98.register(IVone105)
IVone98.register(IVone106)
IVone98.register(IVone107)
IVone98.register(IVone108)
IVone98.register(IVone110)
IVone98.register(IVone111)
#IVone98.register(IVone109)
IVone92.register(IVone112)
IVone92.register(IVone113)
IVone92.register(IVone114)
IVone92.register(IVone115)
IVone92.register(IVone116)
IVone92.register(IVone117)
IVone92.register(IVone118)
IVone92.register(IVone119)
IVone92.register(IVone120)
IVone92.register(IVone121)
IVone121.register(IVone122)
IVone92.register(IVone123)
IVone92.register(IVone124)
IVone92.register(IVone125)
IVone92.register(IVone126)
IVone92.register(IVone127)
IVone92.register(IVone128)
IVone92.register(IVone129)
IVone92.register(IVone131)
IVone92.register(IVone132)
IVone92.register(IVone134)
IVone92.register(IVone135)
IVone92.register(IVone136)
IVone92.register(IVone137)
IVone92.register(IVone138)
IVone92.register(IVone139)
IVone139.register(IVone140)
IVone92.register(IVone141)
IVone92.register(IVone142)
IVone92.register(IVone143)
IVone92.register(IVone144)
IVone92.register(IVone146)
IVone92.register(IVone147)
IVone92.register(IVone148)
IVone148.register(IVone149)
IVone148.register(IVone150)
IVone92.register(IVone151)
IVone92.register(IVone152)
IVone92.register(IVone154)
IVone92.register(IVone155)
IVone92.register(IVone156)

IVone92.register(IVone159)
IVone92.register(IVone160)

IVone92.register(IVone166)
IVone166.register(IVone167)
IVone166.register(IVone168)
IVone166.register(IVone169)
IVone166.register(IVone170)
IVone166.register(IVone171)

print 'Welcome by Panini'
SabxarUpa = SabxaCollection('mimawa fas! gowra')
tradition = raw_input('Do you want to follow Paninian (p),  northern (n), or eastern (e) grammarian tradition?')

if tradition == 'n':
    SabxarUpa.properties['tradition'] = 'northern'
elif tradition == 'e':
    SabxarUpa.properties['tradition'] = 'eastern'
else:
    SabxarUpa.properties['tradition'] = 'pANini'




print SabxarUpa.items

for item in SabxarUpa.properties['words']:
    print item.items


generalsUwra.superCheck(SabxarUpa,IVone76)






print SabxarUpa.properties.keys()
print SabxarUpa.properties['words']

for item in SabxarUpa.properties['words']:
    print item.properties
print SabxarUpa.appliedRules
print SabxarUpa.objs2text()

for item in SabxarUpa.properties.keys():
    if 'alternate' in item:
        try:
            print SabxarUpa.properties[item].objs2text()
        except:
            pass

