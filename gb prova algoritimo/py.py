artes = []

def menu():
    try:
        while True:
            print("""
                1- visitante
                2-funcionario
                """)
            escolha= int(input("digite a opçao desejada:"))
            if escolha == 1:
                menu3()
            elif escolha == 2:
                menu2()
            else:
                print("opçao invalida")
    except ValueError:
        print("apenas numeros por favor")

def menu3():
    try:
        while True:
            print("""bem vindo, 
                  1- visualizar artes
                  2- buscar artes
                  3-voltar
                  """)
            escolha= int(input("digite a opçao desejada:"))
            if escolha == 1:
                visualizar_artes(artes) 
            elif escolha == 2:
                busca()
            elif escolha == 3:
                menu()
            else:
                print("opçao invalida")    
    except ValueError:
        print("apenas numeros por favor")

def menu2():
    try:
        while True:
            print("""   SEJA BEM VINDO
        1- adicionar arte
        2- visualizar artes
        3- ordenar obras
        4- buscar obra
        5- sair
            """)
            escolha = int(input('digite qual opçao deseja:'))
            if escolha == 1:
                adicionar_arte()
            elif escolha == 2:
                visualizar_artes(artes)

            elif escolha == 3:
                ordenar_artes(artes)
            
            elif escolha == 5:
                menu()
            
            elif escolha ==4:
                busca()

            else:
                print("opçao invalida")
    except ValueError:
        print("apenas numeros por favor")


def adicionar_arte():
    try:
        arte = {
            "titulo":"",
            "data de criaçao": 0,
            "tema":"",
            "estilo artistico": "",
            "descriçao":"",
            "tecnica utilizada": "",
            "autor":"",
            "localizaçao":"",
        }
        arte["titulo"] = input("qual o titulo?")
        arte["data de criaçao"] = int(input("ano da data de criaçao?"))
        arte["tema"] = input("tema?")
        arte["estilo artistico"]= input("estilo artistico?")
        arte["descriçao"]= input("descriçao?") 
        arte["tecnica utilizada"] = input("tecnica utilizada?")
        arte["autor"] = input("autor")
        arte["localizaçao"] = input("localizaçao")
        artes.append(arte)
        print(arte)
    except ValueError:
        print("por favor, digite corretamente")

def visualizar_artes(artes):
    
    with open("artes.txt", "w") as arquivo:
        for arte in artes:
            arquivo.write(f"Título {arte['titulo']}\n")
            arquivo.write(f"Data de Criação {arte['data de criaçao']}\n")
            arquivo.write(f"Tema {arte['tema']}\n")
            arquivo.write(f"Estilo Artístico{arte['estilo artistico']}\n")
            arquivo.write(f"Descrição {arte['descriçao']}\n")
            arquivo.write(f"Técnica Utilizada: {arte['tecnica utilizada']}\n")
            arquivo.write(f"Autor: {arte['autor']}\n")
            arquivo.write(f"Localização: {arte['localizaçao']}\n")
            arquivo.write(f"----------------------------------------------------\n")
    print("artes adicionadas a arquivo artes.txt")

def ordenar_artes(artes):
    ordenado = sorted(artes, key=lambda artes: artes["data de criaçao"])
    print(ordenado)
     
    #n = len(artes)
    #for arte in artes:
       # for i in range(n-1):
           # for j in range(n-1):
                #if arte["data de criaçao"][i] > arte["data de criaçao"][i+1]:
                    #arte["data de criaçao"][i], arte["data de criaçao"][i+1] = arte["data de criaçao"][i+1], arte["data de criaçao"][i]
        #print(artes)

def busca():
    try:
        for arte in artes:
            escolha = input("digite o tema da arte que procura")
            if escolha == arte["tema"]:
                print(arte)
            else:
                print("nao encontramos artes com esse tema")
    except Exception as e:
        print("ainda nao possui artes")
                

menu()
