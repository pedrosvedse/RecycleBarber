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
        data_solicitacao=data_solicitacao_atual
        data_prevista=data_prevista_coleta,
        tipo_residuos=tipo_residuos,
        quantidade_residuos=quantidade_residuos,
        status_inicial="solicitada" 

sistema_coletas["ativas"][id_nova_coleta] = nova_coleta_obj
    barbeiro_nome = barbeiros_cadastrados[solicitante_id]["nome"]
    print(f"\n Coleta {id_nova_coleta} solicitada com sucesso para '{barbeiro_nome}' (ID: {solicitante_id}).")
    print(f"   Data prevista para coleta: {data_prevista_coleta.strftime('%d/%m/%Y %H:%M')}.")
    return nova_coleta_obj

    def acompanhar_coleta(id_coleta_para_buscar):
     print(f"\n--- Acompanhando Coleta ID: {id_coleta_para_buscar} ---")
    coleta_encontrada = None
    categoria_encontrada = None

    for categoria in sistema_coletas:
    
    if id_coleta_para_buscar in sistema_coletas[categoria]:
            coleta_encontrada = sistema_coletas[categoria][id_coleta_para_buscar]
            categoria_encontrada = categoria
            break
            if coleta_encontrada:
            
        print(f"Coleta encontrada na categoria: '{categoria_encontrada.capitalize()}'")
        print(coleta_encontrada)

        if coleta_encontrada.status == "solicitada":
            print("   ℹ️  Ação: Aguardando agendamento e designação de um coletor.")
        elif coleta_encontrada.status == "agendada":
            print("   ℹ️  Ação: Coleta agendada. Aguarde o dia e horário previstos.")
        elif coleta_encontrada.status == "em_andamento":
            print("   ℹ️  Ação: A equipe de coleta está a caminho ou realizando a coleta.")
        elif coleta_encontrada.status == "concluida":
            print("   ℹ️  Esta coleta já foi concluída com sucesso.")
        elif coleta_encontrada.status == "cancelada":
            print("   ℹ️  Esta coleta foi cancelada.")
        return coleta_encontrada
    else:
        print(f" Coleta com ID '{id_coleta_para_buscar}' não encontrada no sistema.")
        return None
    def finalizar_coleta(id_coleta_para_finalizar): 
    print(f"\n--- Finalizando Coleta ID: {id_coleta_para_finalizar} ---")
    coleta_encontrada = acompanhar_coleta(id_coleta_para_finalizar)
    if coleta_encontrada is None:
        print(" Coleta não encontrada. Verifique o ID e tente novamente.")
        return None
    if coleta_encontrada.status == "concluida":
        print(" Esta coleta já foi finalizada anteriormente.")
        return None

    if coleta_obj.status in ["solicitada", "agendada", "em_andamento"]:
            coleta_obj.atualizar_status("concluida", observacao_final)
            coleta_obj.data_finalizacao = datetime.datetime.now()

            del sistema_coletas["ativas"][id_coleta_para_finalizar]

            print(f"✅ Coleta {id_coleta_para_finalizar} finalizada com sucesso.")
            return True
        else:
            print(f" Não foi possível finalizar a coleta {id_coleta_para_finalizar}. Status atual: '{coleta_obj.status}'.")
            print(f" A coleta precisa estar em status 'solicitada', 'agendada' ou 'em_andamento' para ser finalizada.")
            return  False