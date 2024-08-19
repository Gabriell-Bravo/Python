normal = 10
picanha = 15
artesanal = 20

queijo =2
bacon = 3
ovo = 1
salada = 3
total = 0


escolha = input("digite o tipo de carne:")
if escolha == "normal":
  total = total + normal
elif escolha =="picanha":
    total = total + picanha
elif escolha == "artesanal":
    total = total + artesanal


add_ovo = input("deseja adicionar ovo? (s/n)")
if add_ovo == "s":
    total = total + ovo

add_bacon = input("deseja adicionar bacon? (s/n)")    
if add_bacon == "s":
    total = total + bacon

add_salada = input("deseja adicionar salada? (s/n)") 
if add_salada == "s":
    total = total + salada

add_queijo = input("deseja adicionar queijo? (s/n)") 
if add_queijo == "s":
    total = total + queijo
    
print(f'o valor total foi de R$:{total}')