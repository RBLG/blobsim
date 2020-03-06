import random as ran
from genericentity import GenericEntity as GEntity

class Blob(GEntity):
    perfectadn = "perfection"
    adnsize = len(perfectadn)

    def __init__(self,nadn,mutsmo):
        self.reset(nadn,mutsmo)

    def Mutate(self,nadn,mutsmoother):
        varmutfac = Blob.mutationfactor * (int(mutsmoother / 100) + 1)
        #rands=ran.getrandbits(3*Blob.adnsize)
        for index in range(0,Blob.adnsize):
            if(ran.getrandbits(3)==0):
                randnum = int(ran.random() * varmutfac * 2 - varmutfac)
                value = nadn[index] + randnum
                if(value < 32):
                    value = 32
                elif(value > 112956):
                    value = 112956 # valeur max d'un caractère unicode??????
                nadn[index] = value
        return nadn

    @staticmethod
    def SetPerfectAdn(npadn):
        npadn=list(npadn)
        for ind in range(0,len(npadn)):
            npadn[ind]=ord(npadn[ind])
        Blob.perfectadn=npadn
        GEntity.adnsize = len(Blob.perfectadn)
        Blob.adnsize = len(Blob.perfectadn)

    
    def GetScore(self): #calcule le "fitness" du blob
        count = 0
        for index in range(0,Blob.adnsize):
            count += abs(self.adn[index] - Blob.perfectadn[index])
        return count 

    def GetGoal(self):
        rtn = self.adn.copy()
        for i in range(0,len(rtn)):
            rtn[i] = chr(rtn[i])

            if(rtn[i] == chr(92) or rtn[i] == "\n" or rtn[i] == "\t" or rtn[i] == "\r"):
                rtn[i] = " "


        return "".join(rtn)

    @staticmethod
    def is1bunset(val,index):
        return val & 1 << index == 0
    
    @staticmethod
    def is2bunset(val,index):
        return val & 3 << index == 0

    @staticmethod
    def is3bunset(val,index):
        return val & 7 << index == 0