class Misc(object):
    """regroupement de fonction ne correspondant a aucune autre classe"""

    @staticmethod
    def AskValidInput(msg,check=lambda val: True): 
        """
        demande une saisie tant qu'une saisie valide n'a pas été rentrée
        """
        print(msg)
        while(True):
            try:
                val = input(">")
                if(check(val)):
                    print("saisie acceptée: ",val)
                    return val
            except:
                print("saisie incorrecte")
    
    @staticmethod
    def CheckIfInt(val,mymin,mymax):
        val = int(val)
        if(isinstance(val,int)):
            if(val >= mymin and val <= mymax):
                return True
            else:
                print("valeur non comprise entre ",mymin," et ",mymax)
        else:
            print("saisie incorrecte, un entier est attendu")
        return False
