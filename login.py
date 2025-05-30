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


def login(): # a fazer
    efetuado = False
    while not efetuado:
        cpf = input("Insira seu CPF.")
        if cpf in usuarios_cadastrados:
            usuario = usuarios_cadastrados[cpf]
            senha = input("Insira sua senha.")
            if senha == usuario.password:
                efetuado = True
            else:
                pass

def login(): # a fazer
    efetuado = False
    while not efetuado:
        cpf = input("Insira seu CPF. Não utilize pontos e traços.")
        if cpf in usuarios_cadastrados:
            usuario = usuarios_cadastrados[cpf]
            senha = input("Insira sua senha.")
            if senha == usuario.password:
                efetuado = True
            else:
                pass

# cadastro
def cadastrar():
    efetuado = False
    while efetuado != True:
        try:
            cpf = input("Insira seu CPF: ")
            cpf = cpf.replace(".","") # retira pontos da string, caso o usuário colocar
            cpf = cpf.replace("-","") # retira traços da string, caso o usuário colocar
            if len(cpf) != 11: raise Exception # um CPF tem 11 digitos, se não tiver, levanta uma exceção
            cpf = int(cpf) # para verificar se o CPF não tem letras ou nada a mais estranho
        except:
            print("Erro: CPF inválido. Por favor, tente novamente.")
        else:
            if str(cpf) in usuarios_cadastrados: # transforma o CPF em string temporariamente para 
                print("CPF já cadastrado. Retornando...")
                break # se o CPF já estiver cadastrado, quebra o loop e cancela o cadastro
            
            nome_empresa = input("Nome da empresa: ")
            username = input("Nome do empresário: ")
            email = input("E-mail da empresa: ").lower() # converte o e-mail em letras minúsculas
            password = input("Insira a sua senha: ")

            confirm_password = "" # confirmação de senha
            while confirm_password != password:
                confirm_password = input("Confirme sua senha: ")
                if confirm_password != password: print("A senha entrada foi diferente.")
            
            endereco = {} # cria um dicionário vazio para guardar todas as informações do endereço
            endereco["UF"] = input("Estado: ")
            endereco["cidade"] = input("Cidade: ")
            endereco["bairro"] = input("Bairro: ")
            
            while True:
                try:
                    endereco["CEP"] = input("CEP: ") # mesma lógica de verificação do CPF
                    endereco["CEP"] = endereco["CEP"].replace("-","")
                    if len(endereco["CEP"]) != 8: raise Exception
                    endereco["CEP"] = int(endereco["CEP"])
                except: 
                    print("CEP inválido.")
                else: 
                    break
            
            endereco["rua"] = input("Rua: ")
            endereco["numero"] = input("Número: ")
            endereco["complemento"] = input("(Opcional) Complemento: ")
            
            new_user = User(cpf, nome_empresa, username, email, password, endereco) # cria objeto de usuário
            usuarios_cadastrados[str(cpf)] = new_user
            
            print("Cadastro efetuado com sucesso! Efetuando login...")
            
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

