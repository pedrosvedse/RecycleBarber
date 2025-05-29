import random
import string

usuarios_cadastrados = {} # lista de usuários cadastrados

# objeto do usuário
class User:
    def __init__(self, cpf, nome_empresa, username, email, password, endereco):
        self.cpf = cpf
        self.nome_empresa = nome_empresa
        self.username = username
        self.email = email
        self.password = password
        self.endereco = endereco

# gerador de id única
def gerador_id(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def login(user, password): # a fazer
    pass

# cadastro
def cadastrar():
    efetuado = False
    while efetuado != True:
        try:
            cpf = int(input("Insira seu CPF. Não utilize números."))
        except:
            print("Erro: CPF inválido. Por favor, tente novamente.")
        else:
            if str(cpf) in usuarios_cadastrados:
                print("CPF já cadastrado. Retornando...")
                break # se o CPF já estiver cadastrado, quebra o loop e cancela o cadastro
            
            nome_empresa = input("Nome da empresa: ")
            username = input("Nome do empresário: ")
            email = input("E-mail da empresa: ").lower()
            password = input("Insira a sua senha.")
            
            confirm_password = "" # confirmação de senha
            while confirm_password != password:
                confirm_password = input("Confirme sua senha: ")
                if confirm_password != password: print("A senha entrada foi diferente.")
            
            endereco = {
                "UF": input("Estado: "),
                "cidade": input("Cidade: "),
                "bairro": input("Bairro: "),
                "CEP": input("CEP: "),
                "rua": input("Rua: "),
                "numero": input("Número: "),
                "complemento": input("Complemento:")
            }
            
            new_user = User(cpf, nome_empresa, username, email, password, endereco)
            usuarios_cadastrados[str(cpf)] = new_user
            
            print("Cadastro efetuado com sucesso! Efetuando login.")
            efetuado = True
            return efetuado # retorna valor booleano para já funcionar com a lógica do main

