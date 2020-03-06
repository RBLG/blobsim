from genericbreeder import GenericBreeder as GBreeder
from genericentity import GenericEntity as GEntity
from blob import Blob
from misc import Misc as mi
import random as ran

class BlobBreeder(GBreeder):

    def __init__(self,nlifesize,nparentsize,nlowestscore):
        self.Reset(nlifesize,nparentsize,nlowestscore)

    def CopulateSub(self,nextadn,mom,dad):
        for index in range(0,len(nextadn)):
            if(ran.getrandbits(1)==0):
                nextent = mom
            else:
                nextent = dad
            nextadn[index]=nextent.adn[index]
    
    @staticmethod
    def CreateLife():
        return Blob([int((ran.random() * 1000) + 32) for i in range(0,Blob.adnsize)],100)

    def IsMaximal(self):
        return (self.life[0].GetScore()==0)
    
    def PrintInfo(self,best):
        print(" adn; '",best.GetGoal(),"'",end="")

    def Struggle(self):
        pass

    def MakeNewborn(self,nadn,mutsmo):
        return Blob(nadn,mutsmo)