from genericentity import GenericEntity as GEntity
import random as ran

class GenericBreeder(object):
    """description of class: its a classy class"""
   


    def __init__(self,nlifesize,nparentsize,nlowestscore):
       self.Reset(nlifesize,nparentsize,nlowestscore)

    def Reset(self,nlifesize,nparentsize,nlowestscore):
        self.life=[self.CreateLife() for i in range(0,nlifesize)]
        self.lifesize=nlifesize
        self.parentsize=nparentsize
        self.parents = self.life[0:self.parentsize]
        self.lastscore = nlowestscore
        self.hardtimebuffer = 0
    
    def CopulateALot(self,parents,howmuch,list=[]):
        if(len(list) == 0):
            list = ([0] * howmuch)
        for index in range(0,howmuch):
            par1 = int(ran.random() * len(parents))
            par2 = int(ran.random() * len(parents))

            ob= list[index] if(index < len(list)) else 0 

            tmpent = self.Copulate(parents[par1],parents[par2],obj=ob)
            list[index] = tmpent
            
        return list

    def Copulate(self,mom,dad,obj=0):
        
        finfac=(mom.GetScore() + dad.GetScore()) / 2
        if(obj != 0):
            nextadn= self.CopulateSub(obj.adn,mom,dad)
            obj.reset(nextadn,finfac)
            return obj
        else:
            nextadn= self.CopulateSub([0]*GEntity.adnsize,mom,dad)
            return self.MakeNewborn(nextadn,finfac)
   
    def MakeNewborn(self,nadn,mutsmo):
        raise NotImplementedError("MakeNewborn()")

    def CopulateSub(self,nextadn,mom,dad):     
        raise NotImplementedError("CopulateSub()")

    @staticmethod
    def CreateLife():
        raise NotImplementedError("CreateLife()")

    def IsMaximal(self):
        raise NotImplementedError("IsMaximal()")

    def LetTimeFlow(self):
        
        gencount = 0
        while(True):
            gencount+=1
            self.life = self.CopulateALot(self.parents,self.lifesize)
            self.life.sort(key=SortByFitness)
            score = life[0].GetScore()
            print("\r[running] score: ",score,"\t size: ",self.lifesize,"\t gen: ",gencount,end="")
            self.PrintInfo(life[0])
            print("      ",end="")
            self.parents = self.life[0:self.parentsize]

            if(self.lastscore <= score):
                self.hardtimebuffer+=1
            else:
                self.hardtimebuffer-=1

            if(self.hardtimebuffer < 0):
                self.hardtimebuffer = 0
            elif(self.hardtimebuffer > 3):
                self.lifesize = int(self.lifesize * 1.1)
                self.Struggle()

            lastperfactor = perfactor
            if(self.IsMaximal()):
                break

        print("\n[ended] score: ",score,"\t size: ",self.lifesize,"\t gen: ",gencount,end="")
        self.PrintInfo(life[0])

    def PrintInfo(self,best):
        raise NotImplementedError("PrintInfo()")

    def Struggle(self):
        raise NotImplementedError("Struggle()") 