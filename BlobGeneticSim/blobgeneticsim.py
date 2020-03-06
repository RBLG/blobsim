from genericbreeder import GenericBreeder as gbred
from genericentity import GenericEntity as gent
from blob import Blob
from blobbreeder import BlobBreeder
from misc import Misc as mi
import random as ran
#########################################################
#
#                  METHODES
#
#########################################################
def SortByFitness(blob):
    return blob.perfactor







#########################################################
#
#                  CODE PRINCIPAL
#
#########################################################
ran.seed(1)
#Blob.mutationfactor = int(mi.AskValidInput("entrez le facteur de mutation",lambda val: mi.CheckIfInt(val,0,100)))
#lifesize = int(mi.AskValidInput("entrez la taille des génération",lambda val: mi.CheckIfInt(val,100,10000)))
#parentsize = int(mi.AskValidInput("entrez la taille de la population reproductive",lambda val: mi.CheckIfInt(val,2,lifesize)))
#Blob.SetPerfectAdn(mi.AskValidInput("entrez la phrase de l'adn parfait"))

Blob.mutationfactor =10
lifesize =100
parentsize =10
Blob.SetPerfectAdn('je hais python')

breeder= BlobBreeder(lifesize,parentsize,9999999999)
breeder.LetTimeFlow()