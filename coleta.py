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

            else:
        
        if id_coleta_para_finalizar in sistema_coletas["finalizadas"]:
            print(f"ℹ️ Coleta {id_coleta_para_finalizar} já consta como finalizada.")
        elif id_coleta_para_finalizar in sistema_coletas["canceladas"]:
            print(f"ℹ️ Coleta {id_coleta_para_finalizar} consta como cancelada e não pode ser finalizada.")
        else:
            print(f" Coleta ativa com ID '{id_coleta_para_finalizar}' não encontrada para finalizar.")
        return False

    def cancelar_coleta(id_coleta_para_cancelar):
    
    print(f"\n--- 🚫 Tentando Cancelar Coleta ID: {id_coleta_para_cancelar} ---")
    
    if id_coleta_para_cancelar in sistema_coletas["ativas"]:
        coleta_obj = sistema_coletas["ativas"][id_coleta_para_cancelar]

del sistema_coletas["ativas"][id_coleta_para_cancelar]

  print(f" Coleta {id_coleta_para_cancelar} cancelada com sucesso.")
        return True
    else:
        if id_coleta_para_cancelar in sistema_coletas["finalizadas"]:
            print(f"ℹ️ Coleta {id_coleta_para_cancelar} consta como finalizada e não pode ser cancelada.")
        elif id_coleta_para_cancelar in sistema_coletas["canceladas"]:
            print(f"ℹ️ Coleta {id_coleta_para_cancelar} já consta como cancelada.")
        else:
            print(f"❌ Coleta ativa com ID '{id_coleta_para_cancelar}' não encontrada para cancelar.")
        return False

def listar_coletas_por_barbeiro(solicitante_id_filtro):

if solicitante_id_filtro not in barbeiros_cadastrados:
        print(f"\n Barbeiro com ID '{solicitante_id_filtro}' não encontrado no sistema.")
        return

    nome_barbeiro = barbeiros_cadastrados[solicitante_id_filtro]["nome"]
    print(f"\n--- Histórico de Coletas para o Barbeiro: {nome_barbeiro} (ID: {solicitante_id_filtro}) ---")
    coletas_encontradas = False

    for categoria in sistema_coletas:
        for id_coleta, coleta_obj in sistema_coletas[categoria].items():
            if coleta_obj.solicitante == solicitante_id_filtro:
                if not coletas_encontradas:
                    print(f"Coletas encontradas para o barbeiro '{nome_barbeiro}':")
                coletas_encontradas = True
                print(f"ID: {id_coleta} | Status: {coleta_obj.status} | Data Solicitação: {coleta_obj.data_solicitacao.strftime('%d/%m/%Y %H:%M')} | Data Prevista: {coleta_obj.data_prevista.strftime('%d/%m/%Y %H:%M')}")

                while idx < len(coletas_do_barbeiro_nesta_categoria):
                coleta_atual = coletas_do_barbeiro_nesta_categoria[idx]
                print(f"    ID: {coleta_atual.id_coleta}, Status: {coleta_atual.status}, "
                      f"Data Prevista: {coleta_atual.data_prevista.strftime('%d/%m/%Y')}, "
                      f"Resíduos: {coleta_atual.tipo_residuos}")
                idx += 1

                if not encontrou_alguma_coleta:
        print(f"  ⚪ Nenhuma coleta encontrada para o barbeiro {nome_barbeiro}.")

def relatorio_status_coletas():
print("\n--- Relatório Geral de Status das Coletas ---")
    total_geral_coletas = 0

    for categoria_nome, dict_coletas_na_categoria in sistema_coletas.items():
        num_coletas_categoria = len(dict_coletas_na_categoria)
        print(f" Coletas {categoria_nome.capitalize()}: {num_coletas_categoria}")
        total_geral_coletas += num_coletas_categoria

        if total_geral_coletas == 0:
        print(" Nenhuma coleta registrada no sistema ainda.")
    else:
        print(f"  ------------------------------------------")
        print(f"  Total de coletas registradas: {total_geral_coletas}")

def executar_simulacao_sistema():
    """Função para demonstrar o uso das funcionalidades implementadas."""
    print("🚀 --- Iniciando Simulação do Sistema de Coleta de Lâminas --- 🚀")

print("\n--- Passo 1: Solicitação de Coletas ---")
    coleta_barbeiro1_a = solicitar_coleta("barbeiro_XPTO_001", "Lâminas de barbear usadas", "1 caixa pequena", dias_para_agendar_padrao=2)
    coleta_barbeiro2_a = solicitar_coleta("barbeiro_ABC_007", "Lâminas e navalhas descartadas", "Aproximadamente 200g", dias_para_agendar_padrao=4)
    coleta_barbeiro1_b = solicitar_coleta("barbeiro_XPTO_001", "Material perfurocortante (agulhas de tattoo)", "1 recipiente rígido", dias_para_agendar_padrao=1)
    solicitar_coleta("barbeiro_inexistente_000", "Lixo comum", "1 saco") # Teste de barbeiro não cadastrado

    print("\n--- Passo 2: Acompanhamento de Coletas ---")
    if coleta_barbeiro1_a: 
        acompanhar_coleta(coleta_barbeiro1_a.id_coleta)

      acompanhar_coleta("COLETA-IDQUE NAOEXISTE")

      print("\n--- Passo 3: Atualização de Status (Ex: Agendamento) ---")
    if coleta_barbeiro2_a:
        coleta_para_agendar = sistema_coletas["ativas"].get(coleta_barbeiro2_a.id_coleta)
        if coleta_para_agendar and coleta_para_agendar.status == "solicitada":
            nova_data_agendada = datetime.datetime.now() + datetime.timedelta(days=2, hours=4) # Agendar para D+2 às +4h de agora
            coleta_para_agendar.data_prevista = nova_data_agendada
            coleta_para_agendar.atualizar_status("agendada", f"Agendado pela central para {nova_data_agendada.strftime('%d/%m/%Y %H:%M')}.")
            print(f"   Coleta {coleta_para_agendar.id_coleta} atualizada para 'agendada'.")

            print("\n--- Passo 4: Listar Coletas por Barbeiro ---")
    listar_coletas_por_barbeiro("barbeiro_XPTO_001")

    print("\n--- Passo 5: Finalizar Coletas ---")
    if coleta_barbeiro1_a:
        finalizar_coleta(coleta_barbeiro1_a.id_coleta, "Material recolhido pelo coletor Equipe Alpha.")

print("\n--- Passo 6: Cancelar Coletas ---")
    if coleta_barbeiro1_b:
    cancelar_coleta(coleta_barbeiro1_b.id_coleta, "Motivo: Cliente não estava presente no local.")

    if coleta_barbeiro1_b:
        cancelar_coleta(coleta_barbeiro1_b.id_coleta) # Já cancelada
    if coleta_barbeiro1_a: # coleta_barbeiro1_a foi finalizada
        cancelar_coleta(coleta_barbeiro1_a.id_coleta)

print("\n--- Passo 7: Relatório Geral de Status ---")
    relatorio_status_coletas()
 print("\n--- Passo 8: Histórico Completo por Barbeiro ---")

 for id_barbeiro in barbeiros_cadastrados:
        listar_coletas_por_barbeiro(id_barbeiro)

        print("\n🏁 --- Simulação Concluída --- 🏁")

if __name__ == "__main__":
    executar_simulacao_sistema()
