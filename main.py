import login

registrado = False

while not registrado:
    print("Seja bem-vindo ao Recycle Barber.")
    print("------------------")
    print("Selecione uma opção:")
    print("1 - Entrar com sua conta.")
    print("2 - Não tem conta? Cadastre-se.")
    print("3 - Sair.")
    print("------------------")
    
    opt = input("")

    #try:
    if opt == "1":
        pass
    elif opt == "2":
        try:
            registrado = login.cadastrar()
        except:
            print("Ocorreu um erro inesperado, tente se cadastrar novamente.")
    else:
        break
    #except:
        #print("Ocorreu um erro inesperado. Tente novamente!\n")