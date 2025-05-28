import random
import string

class User:
    def __init__(self, cpf, nome_empresa, username, email, password, endereco):
        self.cpf = cpf
        self.nome_empresa = nome_empresa
        self.username = username
        self.email = email
        self.password = password
        self.endereco = endereco

#def gerador_id(size=6, chars=string.ascii_uppercase + string.digits):
    #return ''.join(random.choice(chars) for _ in range(size))

def login(user, password):
    pass

def cadastrar(cpf,nome_empresa,email,password,endereco):
    new_user = User(cpf,nome_empresa, email, password,endereco)
    return new_user

