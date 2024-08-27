def adicionar_cliente (nome,email,telefone,endereco):
    clientes.append(cliente)
    return

def exibir_clientes():
    print(clientes)
    return    

def buscar_cliente(email):
    for i in clientes:
        if i == email:
            print(i)
            
            
clientes = []
cliente = []
pergunta1 = input('digite seu nome:')
pergunta2 = input('digite seu email:')
pergunta3 = input('digite seu telefone:')
pergunta4 = input('digite seu endereco:')
cliente.append(pergunta1)
cliente.append(pergunta2)
cliente.append(pergunta3)
cliente.append(pergunta4)
resultado = adicionar_cliente('nome','email','telefone','endereco')
print(clientes)

resultado2 = exibir_clientes()

resultado3 = buscar_cliente(clientes)
print(resultado3)