from .apiAlliex import *
from .apiRodonaves import *
from .apiDirecional import *
from .apiTransreis import *
from .apiMid import *
from .apiCep import *


        
        
class GerarCotacao:
    def __init__(self,cep,peso_total,valorTotal,quantidade_total,cubagem,produto):
        peso_total= float(peso_total)
        valorTotal= float(valorTotal)
        quantidade_total= float(quantidade_total)
        cubagem= float(cubagem)
        
        rte = API_Rodonaves(cep,peso_total,valorTotal,quantidade_total,cubagem,produto)
        alliex = API_Alliex(cep,valorTotal,quantidade_total,peso_total,cubagem)
        transreis = API_Transreis(cep,valorTotal,quantidade_total,peso_total,cubagem)
        mid = API_Mid(cep,valorTotal,quantidade_total,peso_total,cubagem)
        direcional = API_Direcional(cep,valorTotal,quantidade_total,peso_total,cubagem)
        direcional = API_Direcional(cep,valorTotal,quantidade_total,peso_total,cubagem)
        cep = API_CEP(cep)
        
        
        self.rte = rte.COTACAO
        self.alliex = alliex.COTACAO
        self.transreis = transreis.COTACAO
        self.mid = mid.COTACAO
        self.direcional = direcional.COTACAO
        self.cep = cep.CEP
        



     
    
