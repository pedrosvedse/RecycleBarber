# A FAZER:

# funções para solicitação:
#- solicitar coleta (cria um novo objeto de solicitação de coleta)
#- acompanhar coleta
#- finalizar coleta
#- cancelar coleta
import string
import random
import datetime 

class Coleta:
    def __init__(self,id,solicitante,data_solicitacao,data_prevista,residuos,status)
        self.id = id
        self.solicitante = solicitante
        self.data_solicitacao = data_solicitacao
        self.data_prevista = data_prevista
        self.residuos = residuos
        self.status = status
        

def gerador_id(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def solicitar_coleta(solicitante):
    id = gerador_id()
    barbeiro = solicitante 
    data_solicitacao = datetime.datetime.now()
    data_prevista = datetime.datetime.now()
    coleta = Coleta(id,barbeiro,data_solicitacao,data_prevista)    
    return coleta   
    
id_nova_coleta + "COLETA-" + gerador_id()
while id_nova_coleta in id_coletas ["ativo"] or
      id_nova_nova_coleta in sistema_coletas["finalizado"]:
      id _nova_coleta in sistema_coletas["cancelado"]:
    id_nova_coleta = "COLETA-" + gerador_id()

   data_solicitacao_atual = datetime.datetime.now()

nova_coleta_obj = Coleta(
        id_coleta=id_nova_coleta,
        solicitante_id=solicitante_id,
        data_solicitacao=data_solicitacao_atual,
        data_prevista=data_prevista_coleta,
        tipo_residuos=tipo_residuos,
        quantidade_residuos=quantidade_residuos,
        status_inicial="solicitada" 
