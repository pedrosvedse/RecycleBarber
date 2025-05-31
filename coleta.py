# A FAZER:

# criar classe de solicitação de coleta
#- ID da solicitação
#- barbearia que solicitou
#- id do parceiro
#- data da solictiação
#- tipos de resíduo
#- status da coleta
#- data prevista para a colete

# funções para solicitação:
#- solicitar coleta (cria um novo objeto de solicitação de coleta)
#- acompanhar coleta
#- finalizar coleta
#- cancelar coleta
import string
import random

def gerador_id(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))