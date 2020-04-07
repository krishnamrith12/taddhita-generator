# -*- coding: utf-8 -*-
import re
from abc import ABCMeta, abstractmethod
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

    def register(self,regObj=None):
        self.regiRules.append(regObj)

    def check(self,SabxarUpa, rule=None):
            self.flag = 0
            if rule is not None:
                print 'goint to call partuclar rule check', rule
                self.flag = rule.check(SabxarUpa)
                self.flag =1
            else:
                print 'Broadcast inside check',self
                self.flag = self.broadcast(SabxarUpa)
            return self.flag

    def execute(self, SabxarUpa, candiList=None):
        self.candidateList = candiList

    def broadcast(self, SabxarUpa):
        self.flag = 0
        for item in self.regiRules:
            self.flag = item.check(SabxarUpa)
            if self.flag == 1:
                break
        if self.flag == 0:
            print 'Zerof flag after broadcasr'
        return self.flag

    def resolve(self, SabxarUpa,candiList):
        self.candidateList.extend(candiList)
        print 'resolve for generalsuwra'
        print self.candidateList
        for item in self.candidateList:
            if item in SabxarUpa.appliedRules:
                self.candidateList.remove(item)
        if len(self.candidateList) == 1:
            SabxarUpa.appliedRules.append(self.candidateList[0])
            self.candidateList[0].execute(SabxarUpa)
        if len(self.candidateList) ==0:
            print 'zero candidateList for generalsuwra resolve'
        self.candidateList= list()


class Itwo46c(sUwra):

    def check(self,SabxarUpa):
        self.flag = 0
        print 'Itwo46 Check'
        if 'waxXiwaprawyaya' in SabxarUpa.properties.keys():
            if Itwo46 not in SabxarUpa.appliedRules:
                self.candidateList = [Itwo46]
                generalsUwra.resolve(SabxarUpa,self.candidateList)
                self.flag = 1
        return self.flag

    def execute(self, SabxarUpa):
        print 'Itwo46 Execute'

        SabxarUpa.properties['prAwipaxikaM'] = 1
        SabxarUpa.activesamFa.append('prAwipaxikaM')

class Ithree2c(sUwra):

    def check(self, SabxarUpa, rule = None):
        self.flag = self.broadcast(SabxarUpa)
        print 'Ithree2 Check'
        if self.flag == 0:
            ac = prawyAhAra('a','c')
            for item in SabxarUpa.properties['words']:
                if 'state' in item.properties.keys() and 'upaxeSa' in item.properties['state']:
                    for stuff in item.items:
                        if 'anunAsikaM' in stuff.properties.keys() and stuff.properties['value'] in ac:
                            self.candidateList = [Ithree2]
                            self.properties['itItem'] = stuff
                            self.resolve(SabxarUpa,self.candidateList)
        return self.flag

    def resolve(self, SabxarUpa, candiList):
        print 'Conf in 132'
        self.candidateList.extend(candiList)
        if len(self.candidateList) == 1:
            generalsUwra.resolve(SabxarUpa, self.candidateList)
        self.candidateList = list()



    def execute(self,SabxarUpa):
        Ithree9.execute(SabxarUpa,self.properties['itItem'])
        print 'Ithree2 Execute'
        del self.properties['itItem']


class Ithree3c(Ithree2c):



    def check(self, SabxarUpa, rule = None):
        self.flag = 0
        if Ithree3 in SabxarUpa.appliedRules:
            return 2
        hl = prawyAhAra('h','l')
        print 'Ithree3 check'
        for item in SabxarUpa.properties['words']:
            if 'state' in item.properties.keys() and 'upaxeSa' in item.properties['state']:
                if item.items[-1].properties['value'] in hl:
                    if Ithree3 not in SabxarUpa.appliedRules:
                        self.candidateList = [Ithree3]
                        self.properties['itItem'] = item.items[-1]
                        Ithree2.resolve(SabxarUpa, self.candidateList)
                        self.flag =1
        print 'self Flag', self.flag
        return self.flag

class Ithree9c(Ithree2c):



    def check(self, SabxarUpa, rule = None):
        print 'just checking out'


    def execute(self,SabxarUpa,itVal = None):
        print 'Ithree9 Execute'
        for item in SabxarUpa.properties['words']:
            if itVal in item.items and itVal is not None:
                item.properties['itMarker'] = itVal
                item.properties['state'] = 'processed'

        SabxarUpa.items.remove(itVal)


class Ifour13c(sUwra):

    def check(self, SabxarUpa):
        #done only for taddhitas now, is easily expandable
        print 'Ifour13 check'
        self.flag = 0
        if 'waxXiwaprawyaya' in SabxarUpa.properties.keys():
            if Ifour13 not in SabxarUpa.appliedRules:
                self.candidateList = [Ifour13]
                generalsUwra.resolve(SabxarUpa,self.candidateList)
                self.flag = 1
        return self.flag

    def execute(self, SabxarUpa):
        print 'Ifour13 execute'
        for i in range(len(SabxarUpa.properties['waxXiwaprawyaya'].items)):
            try:
                SabxarUpa.properties['afga'] = SabxarUpa.items[0:(SabxarUpa.items.index(SabxarUpa.properties['waxXiwaprawyaya'].items[-1*i])+1)]
                SabxarUpa.activesamFa.append('afga')
                break
            except:
                pass

class Ifour17c(sUwra):


    def check(self,SabxarUpa):
        self.flag = 0
        print 'Ifour17 check'
        if 'prawyaya' in SabxarUpa.properties.keys():
            if SabxarUpa.properties['prawyaya'].objs2text() in attributes.svAxi:
                if SabxarUpa.properties['prawyaya'].objs2text() not in attributes.sarvanAmasWAna:
                    self.flag = self.broadcast(SabxarUpa)
                if self.flag == 0:
                    self.candidateList = [Ifour17]
                    generalsUwra.resolve(SabxarUpa,self.candidateList)
        return self.flag


    def resolve(self, SabxarUpa, candiList):
        print 'Conf in 1417'
        self.candidateList.extend(candiList)
        for item in self.candidateList:
            if item in SabxarUpa.appliedRules:
                self.candidateList.remove(item)
        if len(self.candidateList) == 1:
            generalsUwra.resolve(SabxarUpa, self.candidateList)
        self.candidateList = list()

class Ifour18c(Ifour17c):

    def check(self, SabxarUpa):
        if Ifour18 in SabxarUpa.appliedRules:
            return 2
        self.flag = 0
        print 'Ifour18 Check'
        if SabxarUpa.properties['prawyaya'].objs2text()[0] == 'y' or SabxarUpa.properties['prawyaya'].objs2text()[0] in prawyAhAra('a','c'):
            self.candidateList = [Ifour18]
            if Ifour18 not in SabxarUpa.appliedRules:
                Ifour17.resolve(SabxarUpa,self.candidateList)
                self.flag = 1
        return self.flag

    def execute(self, SabxarUpa):
        print 'Ifour18 Execute'
        for stuff in SabxarUpa.properties['prawyaya'].items:
            for item in SabxarUpa.items:
                if item == stuff:
                    if 'virAmaH' not in SabxarUpa.items[SabxarUpa.items.index(stuff) -1].properties.keys():
                        print 'I am here in 18'
                        SabxarUpa.properties['Ba'] = SabxarUpa.items[:SabxarUpa.items.index(stuff)]
                    elif 'virAmaH' in SabxarUpa.items[SabxarUpa.items.index(stuff) - 1].properties.keys():
                        print 'I am here in 18a'
                        SabxarUpa.properties['Ba'] = SabxarUpa.items[:SabxarUpa.items.index(stuff)-1]
                    SabxarUpa.activesamFa.append('Ba')
                    return


class Ifour109c(sUwra):

    def check(self, SabxarUpa):
        print 'Ifour109 check'
        for i in range(1,len(SabxarUpa.items)):
            if 'virAmaH' in SabxarUpa.items[i].properties.keys():
                if SabxarUpa.items[i-1].properties['value'] in attributes.saMhiwa.keys():
                    if SabxarUpa.items[i+1].properties['value'] in attributes.saMhiwa[SabxarUpa.items[i-1].properties['value']]:
                        self.candidateList = [Ifour109]
                        SabxarUpa.properties['tempsaMhiwa'] = SabxarUpa.items[i-1:i+2]
                        generalsUwra.resolve(SabxarUpa,self.candidateList)

    def execute(self, SabxarUpa):
        print 'Ifour 109 execute'
        SabxarUpa.properties['saMhiwa'] = SabxarUpa.properties['tempsaMhiwa']
        SabxarUpa.activesamFa.append('saMhiwa')


class IIfour71c(sUwra):

    def check(self, SabxarUpa):
        objVal = SabxarUpa
        print 'IIfour71 Check'
        self.flag = 0
        if 'prAwipaxikaM' in objVal.properties.keys() or 'Xawu' in objVal.properties.keys():
            for item in objVal.properties['words']:
                for sups in attributes.sup:
                    if item.objs2text() in sups:
                        if IIfour71 not in SabxarUpa.appliedRules:
                            self.candidateList = [IIfour71]
                            objVal.properties['supTemp'] = item
                            generalsUwra.resolve(SabxarUpa,self.candidateList)
                            self.flag = 1
        return self.flag

    def execute(self, SabxarUpa):
        print 'IIfour71 execute'
        SabxarUpa.elide(SabxarUpa.properties['supTemp'],space=1,word=1)


class IIIone1c(sUwra):


    def resolve(self, SabxarUpa, candiList):
        print 'Conf in 311'
        self.candidateList.extend(candiList)
        if len(self.candidateList) == 1:
            generalsUwra.resolve(SabxarUpa, self.candidateList)
        self.candidateList = list()


class IVone76c(IIIone1c):


    def resolve(self, SabxarUpa, candiList):
        print 'Conf in IVone76'
        self.candidateList.extend(candiList)
        if len(self.candidateList) == 1:
            IIIone1.resolve(SabxarUpa, self.candidateList)
        self.candidateList = list()



class IVone82c(IVone76c):


    def resolve(self, SabxarUpa, candiList):
        print 'Conf in IVone82'

        self.candidateList.extend(candiList)
        if len(self.candidateList) == 1:
            IVone76.resolve(SabxarUpa, self.candidateList)
        self.candidateList = list()




class IVone83c(IVone82c):


    def check(self,SabxarUpa, rule=None):
        print 'iVone83 check'
        if 'apawyam' in SabxarUpa.objs2text():
            for item in self.regiRules:
                self.flag = item.check(SabxarUpa)

#                if self.flag == 1:
#                    self.candidateList.append()
            return 1

    def resolve(self, SabxarUpa, candiList):
        print 'Conf in 83'
        self.candidateList.extend(candiList)
        candiList = self.candidateList
        if len(self.candidateList) == 1:
            IVone82.resolve(SabxarUpa, candiList)
        self.candidateList = list()


    def execute(self,SabxarUpa,replText="apawyam"):
        aN = SabxaCollection('a~N',{'state':'upaxeSa'})
        SabxarUpa.replace(replText,aN)
        SabxarUpa.properties['waxXiwaprawyaya'] = aN
        SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
        for i in range(len(SabxarUpa.properties['words'])):
            if 'apawyam' in SabxarUpa.properties['words'][i].objs2text():
                SabxarUpa.properties['words'][i] = aN
                SabxarUpa.activesamFa.append('upaxeSa')



class IVone92c(IVone83c):


    def check(self,SabxarUpa, rule=None):
        print 'IVone92 Check'
        if 'apawyam' in SabxarUpa.objs2text() or 'gowra' in SabxarUpa.objs2text():
            for item in self.regiRules:
                self.flag = item.check(SabxarUpa)
                if self.flag == 1:
                    break

            if self.flag == 0:
                self.candidateList = [IVone92]
                IVone83.resolve(SabxarUpa, self.candidateList)
                self.candidateList = list()

            return self.flag



    def execute(self,SabxarUpa):
        print 'IVone92 Execute'
        SabxarUpa.properties['semanticSense'] = 'apawyam'
        super(IVone92c,self).execute(SabxarUpa,'apawyam')


class IVone98c(IVone92c):

    def check(self, SabxarUpa):
        self.flag = 0
        print 'IVone98 check'
        if 'gowra' in SabxarUpa.objs2text():
            self.flag = self.broadcast(SabxarUpa)
        if self.flag == 0:
            self.candidateList = [IVone98]
            IVone92.resolve(SabxarUpa,self.candidateList)
            self.flag = 1

        return self.flag

    def resolve(self, SabxarUpa, candiList):
        print 'Conf in IVone98'
        self.candidateList.extend(candiList)
        candiList = self.candidateList
        if len(self.candidateList) == 1:
            IVone92.resolve(SabxarUpa, candiList)
        self.candidateList = list()



class IVone99c(IVone98c):


    def check(self, SabxarUpa):
        self.flag = 0
        print 'IVone99 check'
        for item in SabxarUpa.properties['words']:
            if item.objs2text() in gaNapATa.nada:
                self.flag = 1
                self.candidateList = [IVone99]
                IVone98.resolve(SabxarUpa,self.candidateList)

        return self.flag

    def execute(self,SabxarUpa, replText='apawyam,gowra'):
        print 'IVone99 Execute'
        SabxarUpa.properties['semanticSense'] = 'apawyam,gowra'
        Pak = SabxaCollection('Pa~k',{'state':'upaxeSa'})
        SabxarUpa.replace(replText,Pak)
        SabxarUpa.properties['waxXiwaprawyaya'] = Pak
        SabxarUpa.properties['prawyaya'] = SabxarUpa.properties['waxXiwaprawyaya']
        for i in range(len(SabxarUpa.properties['words'])):
            if 'gowra' in SabxarUpa.properties['words'][i].objs2text():
                SabxarUpa.properties['words'][i] = Pak
                SabxarUpa.activesamFa.append('upaxeSa')



class VIone72c(sUwra):

    def check(self, SabxarUpa):
        print 'Vione72 check'
        self.flag = 0
        if 'saMhiwa' in SabxarUpa.properties.keys():
            self.flag = self.broadcast(SabxarUpa)
        return self.flag

    def resolve(self, SabxarUpa, candiList):
        print 'Conf in 6172'
        self.candidateList.extend(candiList)
        candiList = self.candidateList
        if len(self.candidateList) == 1:
            generalsUwra.resolve(SabxarUpa, candiList)
        self.candidateList = list()

class VIone78c(VIone72c):

    def check(self, SabxarUpa):
        ec= prawyAhAra('e','c')
        if SabxarUpa.properties['saMhiwa'][0].properties['value'] in ec:
            self.candidateList = [VIone78]
            VIone72.resolve(SabxarUpa,self.candidateList)

    def execute(self,SabxarUpa):
        eyav = {'e':'ey','o':'av','E':'Ay','O':'Av'}
        SabxarUpa.replace(SabxarUpa.properties['saMhiwa'][0].properties['value'], eyav[SabxarUpa.properties['saMhiwa'][0].properties['value']])


class VIfour1c(sUwra):

    def check(self, SabxarUpa):
        print 'VIfour1 check'
        self.flag = 0
        if 'afga' in SabxarUpa.properties.keys():
            self.flag = self.broadcast(SabxarUpa)
        return self.flag

    def resolve(self, SabxarUpa, candiList):
        print 'Conf in 641'
        self.candidateList.extend(candiList)
        candiList = self.candidateList
        if len(self.candidateList) == 1:
            generalsUwra.resolve(SabxarUpa, candiList)
        self.candidateList = list()


class VIfour129c(VIfour1c):
    def check(self, SabxarUpa):
        print 'VIfour129 check'

        self.flag = 0
        if 'Ba' in SabxarUpa.properties.keys():
            self.flag = self.broadcast(SabxarUpa)
        return self.flag

    def resolve(self, SabxarUpa, candiList):
        print 'Conf in 64129'
        self.candidateList.extend(candiList)
        candiList = self.candidateList
        if len(self.candidateList) == 1:
            VIfour1.resolve(SabxarUpa, candiList)
        self.candidateList = list()

class VIfour144c(VIfour129c):

    def check(self, SabxarUpa):
        self.flag = 0
        if 'waxXiwaprawyaya' in SabxarUpa.properties.keys():
            self.flag = self.broadcast(SabxarUpa)
        return self.flag


    def resolve(self, SabxarUpa, candiList):
        print 'Conf in 64144'
        self.candidateList.extend(candiList)
        candiList = self.candidateList
        if len(self.candidateList) == 1:
            VIfour129.resolve(SabxarUpa, candiList)
        self.candidateList = list()

class VIfour146c(VIfour144c):

    def check(self, SabxarUpa):
        self.flag = 0
        if 'u' in SabxarUpa.properties['Ba'][-1].properties['value']:
            self.flag = 1
            self.candidateList = [VIfour146]
            VIfour144.resolve(SabxarUpa,self.candidateList)

    def execute(self, SabxarUpa):
        SabxarUpa.properties['Ba'][-1].properties['value'] = guNa('u')



class VIfour148c(VIfour144c):

    def check(self, SabxarUpa):
        self.flag = 0
        print 'VIfour148 Check', '!'+SabxarUpa.properties['Ba'][-1].properties['value']+'!'
        if 'i' in SabxarUpa.properties['Ba'][-1].properties['value'] or 'a' in SabxarUpa.properties['Ba'][-1].properties['value']:
            self.flag = 1
            self.candidateList = [VIfour148]
            VIfour144.resolve(SabxarUpa,self.candidateList)
        return self.flag

    def execute(self, SabxarUpa):
        SabxarUpa.properties['Ba'][-1].properties['value'] = ''


class VIIone2c(VIfour1c):

    def check(self, SabxarUpa):
        if VIIone2 in SabxarUpa.appliedRules:
            return 2
        print 'VIIone2 Check'
        self.flag = 0
        self.repDict = {'Pa':'Ayana'}
        for item in self.repDict.keys():
            if item in SabxarUpa.properties['prawyaya'].objs2text():
                self.candidateList = [VIIone2]
                SabxarUpa.properties['repTemp'] = item
                VIfour1.resolve(SabxarUpa,self.candidateList)
                self.flag =1
        return self.flag

    def execute(self, SabxarUpa):
        print "VIIone2 execute"
        SabxarUpa.properties['prawyaya'] = SabxaCollection(self.repDict[SabxarUpa.properties['repTemp']])
        SabxarUpa.replace(SabxarUpa.properties['repTemp'],SabxarUpa.properties['prawyaya'])

        del SabxarUpa.properties['repTemp']

class VIItwo115c(VIfour1c):

    def check(self, SabxarUpa):
        print 'VIItwo115 Check'

        self.flag = 0
#        if 'N' in SabxarUpa.properties['prawyaya'].objs2text() or 'F' in SabxarUpa.properties['prawyaya'].objs2text():
        self.flag = self.broadcast(SabxarUpa)


        if self.flag == 0:
            self.candidateList = [VIItwo115]
            VIfour1.resolve(SabxarUpa,self.candidateList)

        return self.flag
    def resolve(self, SabxarUpa, candiList):
        print 'Conf in 72115'
        self.candidateList.extend(candiList)
        candiList = self.candidateList
        if len(self.candidateList) == 1:
            VIfour1.resolve(SabxarUpa, candiList)
        self.candidateList = list()


        return self.flag



class VIItwo117c(VIItwo115c):

    def check(self, SabxarUpa):
        self.flag = 0
        print 'VIItwo117 check'
        self.flag = self.broadcast(SabxarUpa)
        if self.flag == 0:
            if 'N' in SabxarUpa.properties['waxXiwaprawyaya'].objs2text() or 'F' in SabxarUpa.properties['waxXiwaprawyaya'].objs2text():

                self.flag = 1
                self.candidateList = [VIItwo117]
                VIItwo115.resolve(SabxarUpa,self.candidateList)


    def resolve(self, SabxarUpa, candiList):
        print 'Conf in 72117'
        self.candidateList.extend(candiList)
        candiList = self.candidateList
        if len(self.candidateList) == 1:
            VIItwo115.resolve(SabxarUpa, candiList)
        self.candidateList = list()



    def execute(self, SabxarUpa):
        print 'VIItwo117 execute'
        for item in SabxarUpa.properties['afga']:
            if item.properties['value'] in prawyAhAra('a','c'):
                item.properties['value'] = vrixXiH(item.properties['value'])
                break


class VIItwo118c(VIItwo117c):

    def check(self, SabxarUpa):
        self.flag = 0
        print 'VIItwo118 check'

        if 'k' in SabxarUpa.properties['waxXiwaprawyaya'].objs2text():
            self.flag = 1
            self.candidateList = [VIItwo118]
            VIItwo117.resolve(SabxarUpa,self.candidateList)

        return self.flag

    def execute(self, SabxarUpa):
        print 'VIItwo118 execute'
        for item in SabxarUpa.properties['afga']:
            if item.properties['value'] in prawyAhAra('a','c'):
                item.properties['value'] = vrixXiH(item.properties['value'])
                break



generalsUwra = sUwra()
Itwo46 = Itwo46c()
Ithree2 = Ithree2c()
Ithree3 = Ithree3c()
Ithree9 = Ithree9c()
Ifour13 = Ifour13c()
Ifour17 = Ifour17c()
Ifour18 = Ifour18c()
Ifour109 = Ifour109c()

IIfour71 = IIfour71c()

IIIone1 = IIIone1c()

IVone76 = IVone76c()
IVone82 = IVone82c()
IVone83 = IVone83c()
IVone92 = IVone92c()
IVone98 = IVone98c()
IVone99 = IVone99c()


VIone72 = VIone72c()
VIone78 = VIone78c()
VIfour1 = VIfour1c()
VIfour129 = VIfour129c()
VIfour144 = VIfour144c()
VIfour146 = VIfour146c()
VIfour148 = VIfour148c()


VIIone2 = VIIone2c()
VIItwo115 = VIItwo115c()
VIItwo117 = VIItwo117c()
VIItwo118 = VIItwo118c()

generalsUwra.register(Itwo46)

generalsUwra.register(Ithree2)

generalsUwra.register(Ifour13)

generalsUwra.register(Ifour17)
generalsUwra.register(Ifour109)

generalsUwra.register(IIfour71)
generalsUwra.register(IIIone1)
generalsUwra.register(VIfour1)
generalsUwra.register(VIone72)



IIIone1.register(IVone76)
Ithree2.register(Ithree3)
#Ithree2.register(Ithree9)
Ifour17.register(Ifour18)
IVone76.register(IVone82)
IVone82.register(IVone83)
IVone83.register(IVone92)
IVone92.register(IVone98)
IVone98.register(IVone99)
VIfour1.register(VIItwo115)
VIfour1.register(VIfour129)
VIfour1.register(VIIone2)
VIfour129.register(VIfour144)
VIfour144.register(VIfour146)
VIfour144.register(VIfour148)

VIone72.register(VIone78)


VIItwo115.register(VIItwo117)
VIItwo117.register(VIItwo118)
print 'Welcome by Panini'
SabxarUpa = SabxaCollection('upagu fas! apawya~m')


generalsUwra.check(SabxarUpa,IVone76)




counter = 0

while(1):



    print SabxarUpa.objs2text()
    print SabxarUpa.properties.keys()
    print SabxarUpa.appliedRules
    ak = raw_input('Enter val')
    print SabxarUpa.activesamFa

    val = 0
    counter = counter +1
    if len(SabxarUpa.activesamFa) >= 1 :

        if SabxarUpa.activesamFa[0] == 'upaxeSa':
            print 'inside main upaxEsa'
            generalsUwra.check(SabxarUpa,Ithree2)
            del SabxarUpa.activesamFa[0]
        elif SabxarUpa.activesamFa[0] == 'prAwipaxikaM':
            print 'inside main Pratipatikam'
            generalsUwra.check(SabxarUpa, IIfour71)
            del SabxarUpa.activesamFa[0]
        elif SabxarUpa.activesamFa[0] == 'afga':
            print 'inside main afga'
            generalsUwra.check(SabxarUpa, VIfour1)
            del SabxarUpa.activesamFa[0]
        elif SabxarUpa.activesamFa[0] == 'Ba':
            print 'inside main Ba'
            generalsUwra.check(SabxarUpa, VIfour129)
            del SabxarUpa.activesamFa[0]
        elif SabxarUpa.activesamFa[0] == 'saMhiwa':
            print 'inside main saMhiwa'
            generalsUwra.check(SabxarUpa, VIone72)
            del SabxarUpa.activesamFa[0]


    else:
        val = generalsUwra.broadcast(SabxarUpa)



    if counter == 9:
        print SabxarUpa.objs2text()
        print SabxarUpa.appliedRules
        sys.exit()


"""
class sUwra(object):

    def __init__(self):
        self.anuvriwwi = ""
        self.sUwraText = ""
        self.regiRules = list()
        #self.candidateList = list()


    def check(self, SabxarUpa, Myapawyam=None,checkaXikAra = '',obj=None,par=None):
        if checkaXikAra == 'IVone76':
            IIIone1.check(SabxarUpa,self)
            print self.candidateList, 'geninside'
            self.execute(SabxarUpa)

        if checkaXikAra == 'upaxeSa':
            Ithree2.check(SabxarUpa,self)


    def execute(self,SabxarUpa):
        print self.candidateList[-1][1],'gencandi'
        myObj = self.candidateList[-1][1]
        myObj.execute(SabxarUpa)

    def register(self, observer):
        self.regiRules.append(observer)


class Ithree2c(sUwra):

    def __init__(self):
        super(Ithree2c, self).__init__()


    def check(self, SabxarUpa, Myapawyam):
        if 'upaxeSa' in Sabxa.SabxaStuffProperties.keys():
            hl = prawyAhAra('h','l').split('|')
            if



class IIIone1c(sUwra):

    def __init__(self):
        self.anuvriwwi = "prawyayaH parasca prAwipaxikAw waxXiwaH samaqWAnAm praWamAw vA"
        self.sUwraText = "prAg xIvyato aN"
        self.regiRules = list()
        #self.candidateList = list()



    def check(self, SabxarUpa, Myapawyam):
        if 'semanticSense' in SabxarUpa.SabxaStuffProperties.keys():
            print '311'
            self.regiRules[0].check(SabxarUpa, self)
            print self.candidateList,'311 isnide'
        Myapawyam.candidateList.append(self.candidateList[-1])

    def execute(self, SabxarUpa):
        #SabxarUpa.SabxaStuffProperties['prawyaya'] = 1
        print self.candidateList,'311'

        #self.candidateList = list()





class IVone76c(IIIone1c):

    def __init__(self):
        self.anuvriwwi = "prawyayaH parasca prAwipaxikAw waxXiwaH samaqWAnAm praWamAw vA"
        self.sUwraText = "prAg xIvyato aN"
        self.regiRules = list()
        #self.candidateList = list()


    def check(self, SabxarUpa=None, Myapawyam=None):
        if 'semanticSense' in SabxarUpa.SabxaStuffProperties.keys():
            print '76'
            self.regiRules[0].check(SabxarUpa,self)
            print self.candidateList,'76inside'
        Myapawyam.candidateList.append(self.candidateList[-1])

    def execute(self, SabxarUpa):
        print self.candidateList,'76'

        SabxarUpa.SabxaStuffPropertiesDone['semanticSense'] = SabxarUpa.SabxaStuffProperties.pop('semanticSense')
        SabxarUpa.SabxaStuffProperties['waxXiwa'] = 1
        super(IVone76c, self).execute(SabxarUpa)
        #self.candidateList = list()





class IVone83c(IVone76c):

    def __init__(self):
        self.anuvriwwi = "prawyayaH parasca prAwipaxikAw waxXiwaH samaqWAnAm praWamAw vA"
        self.sUwraText = "prAg xIvyato aN"
        self.regiRules = list()
        #self.candidateList = list()


    def check(self, SabxarUpa=None, Myapawyam=None):
        if SabxarUpa.SabxaStuffProperties['semanticSense'] == 'apawyam':
            print '83'
            self.regiRules[0].check(SabxarUpa,self)
            print self.candidateList,'83inside'
        Myapawyam.candidateList.append(self.candidateList[-1])

    def execute(self, SabxarUpa):
        print self.candidateList,'83'

        if hasattr(SabxarUpa, 'waxXiwaprawyaya'):
            super(IVone83c, self).execute(SabxarUpa)
        else:
            SabxarUpa.initiatewaxXiwaprawyaya("aN")
            super(IVone83c, self).execute(SabxarUpa)
        #self.candidateList = list()





class IVone92c(IVone83c):

    def __init__(self):
        self.anuvriwwi = "prawyayaH parasca prAwipaxikAw waxXiwaH samaqWAnAm praWamAw vA prAg xIvyato aN"  # lint:ok
        self.sUwraText = ""
        self.regiRules = list()
        #self.candidateList = list()



    def check(self, SabxarUpa, Myapawyam):
        if SabxarUpa.SabxaStuffProperties['semanticSense'] == 'apawyam' and SabxarUpa.stem.SabxaStuffProperties['sup'].SabxaText == 'fas':
            print '92'
            for item in self.regiRules:
                item.check(SabxarUpa,self)
            print len(self.candidateList)
            if len(self.candidateList) > 0:
                Myapawyam.candidateList.append(self.candidateList[-1])
            elif len(self.candidateList) == 0:
                Myapawyam.candidateList.append([41092,self,SabxarUpa,Myapawyam])




    def execute(self, SabxarUpa):

        print self.candidateList,'92'
        super(IVone92c, self).execute(SabxarUpa)




class IVone99c(object):

    def __init__(self):
        self.sUwraText = ""
        self.anuvriwwi = ""

    def check(self, SabxarUpa, Myapawyam):
        if SabxarUpa.stem.SabxaText in gaNapATa.nada:
            Myapawyam.candidateList.append([41099,self,SabxarUpa,Myapawyam])


    def execute(self,SabxarUpa):
        SabxarUpa.waxXiwaprawyaya = SabxaStuff("PhaK")



class IVone112c(IVone92c):

    def __init__(self):
        self.sUwraText = ""
        self.anuvriwwi = ""
        self.regiRules = list()
        #self.candidateList = list()


    def check(self, SabxarUpa, Myapawyam):
        print '112'
        if SabxarUpa.stem.SabxaText in gaNapATa.Siva:
            Myapawyam.candidateList.append([41112,self,SabxarUpa,Myapawyam])

    def execute(self,SabxarUpa):
        SabxarUpa.initiatewaxXiwaprawyaya("aN")
        super(IVone112c, self).execute(SabxarUpa)
        #self.candidateList = list()





generalsUwra = sUwra()
IIIone1 = IIIone1c()
IVone76 = IVone76c()
IVone83 = IVone83c()
IVone92 = IVone92c()
IVone99 = IVone99c()
IVone112 = IVone112c()

generalsUwra.register(IIIone1)
IIIone1.register(IVone76)
IVone83.register(IVone92)
IVone92.register(IVone112)
IVone76.register(IVone83)
"""