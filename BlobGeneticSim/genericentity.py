class GenericEntity(object):
    adnsize = 10
    mutationfactor = 10

    def __init__(self,ngoal,mutsmoother):
        self.reset(ngoal,mutsmoother)

    def reset(self,nadn,mutsmoother):
        self.adn=self.Mutate(nadn,mutsmoother)
        self.score=self.GetScore()

    def Mutate(self,nadn,mutsmo):
         raise NotImplementedError("Mutate()")

    def GetScore(self):
        raise NotImplementedError("GetFitness()")

    def GetGoal(self):
        raise NotImplementedError("GetAdn()")
