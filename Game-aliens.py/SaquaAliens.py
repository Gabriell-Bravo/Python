import time

def introducao():
    print(f'Logo após um longo dia de trabalho, {nome} chega em casa e faz suas coisas rotinerias...')
    time.sleep(3)
    print('Até o momento em que você se deita para enfim descansar após um longo dia.')
    time.sleep(3)
    print('Você adormece...\n')
    time.sleep(2)
    print('Na manhã do dia seguinte, você acorda com uma estranha sensação...')
    time.sleep(3)
    print('Um mal pressentimento de que algo irá acontecer...')
    time.sleep(2.5)
    print('Então você se levanta e percebe que tem um ar estranho, desce as escadas de sua casa...')
    time.sleep(3)
    print('Aparentemente tudo está em ordem, você bebe sua água e abre sua janela, logo de imediato...')
    time.sleep(3)
    print('Você repara que a cidade está um caos, fogo para todo lado e pessoas correndo desesperadamente...')
    time.sleep(3)
    print('Você até pode sentir um pouco de alívio de não ser uma dessas casas em chamas, mas seria um pouco arrogante não?')
    time.sleep(3)
    print('Você continua olhando ao redor e agora repara nos ceús, você vê naves estranhas voando de um lado a outro...')
    time.sleep(3)
    print('Estranhamente você tem a sensação de ter visto um flash de luz, como se algo piscasse para você...')
    time.sleep(3)
    print('Depois disso voce torna a voltar para dentro de casa e se vê tendo que decidir entre se abrigar em casa...')
    time.sleep(3)
    print('Onde aparentemente é seguro, ou buscar uma chance de sobrevivência lá fora.')
    time.sleep(3)
    escolha_1 = input('Oque você decide fazer? (sair/ficar)')
    if escolha_1 == 'sair':
        rua_do_beco()
    elif escolha_1 == 'ficar':
        casa()

def casa():
    print(f'{nome} tenta se abrigar em casa e se esconder o máximo possível, mas como já deva imaginar...')
    time.sleep(3)
    print('Seu fim era inevitável...')
    time.sleep(1.5)
    print('Você escuta um forte som de explosão, que te derruba no chão...')
    time.sleep(3)
    print('Atordoado, você se levante e olha para o local de onde veio a explosão...')
    time.sleep(3)
    print('E você se depara com 5 criaturas estranhas, que te encaram com um olhar frio...')
    time.sleep(3)
    print('Em suas mãos há armas de aparência esquisita...')
    time.sleep(2)
    print('E as criaturas parecem quer te dizer algo, que soa como: \n')
    time.sleep(3)
    frase_alien = '𝒈ℴ𝓊𝓇𝒾𝓈𝒽 ℳ𝒶𝒾𝒻𝓁𝒶𝓃 𝒹ℯ𝓈𝓉𝒾𝓃𝒶𝒹ℴ ℯ𝓇ℯ𝓂𝒶𝓈 𝒹ℯ 𝒮𝓅𝒶𝒾𝓃\n'
    for letra in frase_alien: 
        print(letra, end='', flush=True)
        time.sleep(0.07)
    print('\n')
    time.sleep(1)
    print('Você fica perplexo por não ter entendido nada, e quando vai dizer algo...')
    time.sleep(3)
    print('Tudo se escurece...')
    time.sleep(2)
    print('Você sente um ar frio percorrer sua espinha...')
    time.sleep(2)
    morte()

def rua_do_beco():
    print(f'Com muita coragem, {nome} decide sair para tentar a sorte nesse ambiente caótico...')
    time.sleep(3)
    print('Logo tenta pensar em locais onde poderia ir...')
    time.sleep(2)
    print(f'{nome}: uma delegacia? tão óbvio...')
    time.sleep(2)
    print(f'{nome}: um hospital? eu nem me machuquei...') 
    time.sleep(2)
    print(f'{nome}: que tal uma escola? com certeza não, todos os filmes acabam mal lá...')
    time.sleep(3)
    print(f'{nome}: melhor só andar sem rumo mesmo, e que a sorte esteja comigo...\n')
    time.sleep(3)
    print('Dito isso, você sai andando e sem demorar muito se depara com um beco...')
    time.sleep(2)
    print('Onde você se vê tendo que decidir se vai pelo beco ou continua pela rua...')
    time.sleep(3)
    escolha_2 = input('Oque decide fazer? (beco/rua)')
    if escolha_2 == 'beco':
        beco_da_nave()
    elif escolha_2 == 'rua':
        rua_da_nave()

def beco_da_nave():
    print('Você vai se esgueirando com cautela pelo beco, onde você se depara com algo inesperado...')
    time.sleep(3)
    print('Um pedaço de ferro, que seria ótimo para se defender...')
    time.sleep(3)
    barra_de_ferro = input('Você quer pegar a barra de ferro? (sim/nao)')
    if barra_de_ferro == 'sim':
        barra_de_ferro == True
    elif barra_de_ferro == 'nao':
        barra_de_ferro == False
    print('Você continua seu caminho e se depara em uma rua, ao fundo você vê uma das naves pousada...')
    time.sleep(3)
    print('Chegando próximo a ela, você vê uma escotilha aberta...')
    time.sleep(2)
    escolha_3 = input('Você deseja entrar na nave ou dar a volta nela? (entrar/rodear)')
    if escolha_3 == 'rodear':
        volta_da_nave()
    elif escolha_3 == 'entrar':
        dentro_nave()

def rua_da_nave():
    print('Você continua pela rua analisando as casas, quando de repente você tropeça em algo...')
    time.sleep(3)
    print('Quando você olha pra baixo, se depara com um pedaço de madeira...')
    time.sleep(2.5)
    pedaco_madeira = input('Você quer pegar o pedaço de madeira? (sim/nao)')
    if pedaco_madeira == 'sim':
        pedaco_madeira == True
    elif pedaco_madeira == 'nao':
        pedaco_madeira == False
    print('Logo após, você vira algumas esquinas e se depara com uma nave pousada...')
    time.sleep(2.5)
    print('Quando se aproxima, você repara em uma escotilha aberta...')
    time.sleep(2.5)
    escolha_4 = input('Você deseja entrar na nave ou dar a volta nela? (entrar/rodear)')
    if escolha_4 == 'rodear':
        volta_da_nave()
    elif escolha_4 == 'entrar':
        dentro_nave()

def volta_da_nave():
    print('Com receio de entrar na nave, você decide contorna-lá com cautela...')
    time.sleep(2.7)
    print('Você acaba se deparando com 2 seres estranhos que parecem estar conversando...')
    time.sleep(3)
    print('Você não compreende uma única palavra que eles dizem...')
    time.sleep(2.5)
    print('E de repente, você sente um calor no peito, no mesmo instante que as criaturas te olham...')
    time.sleep(3)
    print('Mas elas não parecem olhar pra você, e sim para trás de você...')
    time.sleep(2.5)
    print('Ao se virar, você repara uma terceira criatura te olhando, mas esta estava com uma espécie de arma...')
    time.sleep(3.5)
    print('Logo você vai perdendo forças e cai no chão...')
    time.sleep(2.5)
    morte()

def dentro_nave():
    print('Entrando na nave, voce repara que ela é repleta de tecnologia avançada, cores cinza e ciano translucido...')
    time.sleep(3)
    print('Caminhando pelos corredores você encontra um painel de controle com vários botões ciano...')
    time.sleep(3)
    print('Mas chamando total atenção entre os botões, havia um botão maior e vermelho')
    time.sleep(3)
    print(f'{nome}: Logo um botão vermelho? Até parece que eu nunca vi os filmes...')
    time.sleep(2)
    escolha_5 = input('Você decide apertar o botão? (sim/nao)')
    if escolha_5 == 'sim':
        print('Com receio, você aperta o botão...')
        time.sleep(1.5)
        print('Se passam alguns segundos até que você percebe...')
        time.sleep(1.5)
        print('Era somente um detalhe do painel...')
        time.sleep(1.5)
    print('Agora que sua atenção saiu do botão, você repara uma pequena alavanca...')
    time.sleep(2.5)
    print('Ao se aproximar, ela automaticamente se abaixa...')
    time.sleep(2)
    print('O painel emite um som, para você desconhecido, que se parece com:')
    time.sleep(2.3)
    print('\n')
    frase_alien_2 = '𝒶𝓁𝓀ℴ𝒽ℴ𝓁ℯ𝓈 𝒹ℯ ℯ𝓇ℯ𝓂𝒶𝓈 𝒹ℯ 𝒮𝓅𝒶𝒾𝓃\n'
    for letra in frase_alien_2: 
        print(letra, end='', flush=True)
        time.sleep(0.04)
    print('\n')
    print('Você se espanta com o som, e logo após ouve 3 beeps...')
    time.sleep(2)
    print('E no mesmo instane, tudo fica extremamente claro e barulhento....')
    time.sleep(2.3)
    print('Infelizmente pra você, era um comando de auto-destruição...')
    time.sleep(2)
    morte()

def morte():
    
    preludio = 'Este é o fim da sua história'
    for letras in preludio:
        print(letras, end='', flush=True)
        time.sleep(0.04)
    print('\n')


    fim = 'Você Morreu!!'
    for letras in fim:
        print(letras, end='', flush=True)
        time.sleep(0.04)


import pygame
pygame.mixer.init()
pygame.init()
musica_de_fundo = pygame.mixer.music.load('Trilha sonora de ação (320).mp3')
pygame.mixer.music.play(-1)
logo = 'SAQUAALIENS'
txt_iniciaL = 'Bem vindo ao nosso jogo (SaquaAliens)'
print('-'*len(txt_iniciaL))
print(txt_iniciaL)
print('-'*len(txt_iniciaL))

print(""""
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⠶⠿⠿⠿⠿⢶⣶⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⢸⣅⠉⠙⠓⠒⠤⡍⠛⠛⠿⣶⣤⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⢀⢼⡦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣈⣭⣿⣶⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡴⠶⣶⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡆⢸⠀⠙⢮⡢⠀⠀⠀⠀⠀⣴⡟⠋⠁⠀⠀⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠟⢋⣡⣄⣰⡿⠀⠀⠀⠀⠀⢀⣀⣀⣤⣴⣶⣿⣿⡿⢶⡶⠶⣶⣶⣤⣄⡀⠀⠀⠀⠀⣿⠇⠸⠇⠀⠀⠙⢦⡀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⠾⠛⠁⠒⠁⠀⢀⡞⠙⣧⠀⠀⢀⣴⠞⠛⣽⣿⣿⣧⠀⠀⠀⠙⣧⡙⡄⠀⠀⠀⠙⠛⠿⣦⣄⢰⡿⣰⠀⠀⠀⠀⠀⠀⠙⢦⠀⠘⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠾⠋⠁⠀⠀⠀⠀⠀⢠⡎⠰⡔⣽⣷⣴⣿⣅⡤⣶⣿⣿⣿⡿⠀⢦⠀⠀⠸⡇⢹⡄⠀⠀⠀⠀⠀⠀⢙⣿⢧⠏⠀⠀⣀⣀⣤⣤⣄⣀⣳⠀⢻⣇⠀⠀⠀⠀⠀⠀
⠀⣠⠞⣡⠴⠖⠛⠉⠛⠒⠶⣦⡀⠀⡀⠀⢀⣿⣿⣿⣿⣷⣿⣿⣿⣿⠇⠀⠈⠃⢀⢀⡇⠘⠇⠀⠀⠀⠀⠀⢠⡾⣧⠏⠀⣴⡾⠟⠉⠉⠉⠉⠙⠻⢷⣌⣿⡆⠀⠀⠀⠀⠀
⢸⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⣿⢠⡾⢶⣦⣾⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠟⣼⠁⠀⠀⠀⠀⣠⠞⡿⡛⠚⠁⢀⡾⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠏⠀⠀⣾⣿⣿⣿⣿⠿⣿⣿⡿⠃⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠋⢀⣧⡤⠤⢤⡼⠀⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⣿⠛⠿⣿⡷⠾⠟⠉⠀⠀⠀⠀⠀⡀⣰⠏⢀⡀⠀⠀⠀⠀⠀⠈⠉⡀⣠⣼⠃⢀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⢊⡴⠋⣠⡿⠀⠀⠀⠀⠀⠀⠀⠀⣾⣝⡅⠀⣿⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⣧⠀⠀⡀⠀⠀⠠⠔⠚⣀⡴⠋⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⣽⡯⠂⢠⠇⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠓⠬⣷⣤⣁⣀⣀⣤⠴⠟⣋⠴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠂⠀⡼⢰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠈⠉⢉⡁⠀⠀⠀⠀⠀⢀⣴⣶⣶⣦⣀⢦⡀⠀⠀⠀⠐⠉⠀⣠⣾⠃⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⢀⣾⣷⣶⣤⣀⣰⣿⣿⣿⣿⣿⣿⣷⡙⣦⠀⠀⠀⢀⡾⣱⠃⣸⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⣾⡿⢷⣦⣼⠟⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠐⣭⠚⠃⢰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⢀⣤⣶⠶⠶⠶⢦⣤⣀⣹⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠴⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⡿⠃⠀⠀⠀⢴⣇⠀⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣠⣤⣤⣄⣀⣠⣾⡿⠋⣠⠞⠃⠀⠀⢾⠇⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡇⠀⢿⣄⠈⠉⠙⠩⠥⠒⠋⠀⠀⠀⠀⠀⠛⠀⣄⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢶⣿⠟⠓⠒⠺⠛⠋⠀⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣄⡀⠀⠀⠀⠀⠀⣀⣤⠖⠀⠀⠈⠻⣿⣦⣀⣀⣀⣠⣤⡤⠤⠤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠷⠂⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡼⠋⠈⠙⠀⢀⡤⠖⠋⠁⠀⠀⡀⡀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠉⠳⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣀⣠⣴⠶⠾⠛⠋⠁⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⡻⢻⢻⡇⣰⠀⠀⠀⠀⠀⡀⠀⢀⣀⣀⡀⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⠋⠁⠀⠀⠀⣀⠀⣠⠆⠀⠀⢰⠏⣴⠀⠀⠀⠀⠀⠃⠇⣁⡵⠃⠀⠀⢃⣉⣠⡶⠾⠟⠋⠉⠙⠷⣦⣀⠀⠹⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⡤⣒⣋⣭⣤⣤⣤⣤⣤⣾⢀⠇⠀⠀⢰⡄⣴⠾⠋⠉⠉⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡆⠀⢹⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⡼⠋⣹⡏⠀⠀⠀⠀⠀⠀⢸⣼⡀⠀⠀⣘⠇⢿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠃⢠⣼⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⡀⠀⢳⡄⢻⣇⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠈⠳⠬⠿⠷⠶⢦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡆⢲⡟⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠁⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠙⢦⣀⡀⠀⠀⠀⣀⣀⡀⠀⠉⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠘⡷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢦⣄⠉⠳⣦⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⢻⣷⠃⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠺⣿⣡⣾⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠛⠁⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⠞⠋⣁⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣀⢀⣀⣀⣴⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠶⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀





 """)
print('-'*len(logo))
print(logo)
print('-'*len(logo))
play = input('Deseja Iniciar o Jogo?')
if play == 'Sim'or play == "sim":
    print('Bem vindo ao jogo SaquaAliens!!\n')
    time.sleep(1.5)
    print('Realizado pelo grupo de alunos, João Marcos, Gabriel Bravo, Bruno Geraldo, Marcos Vinicius!')
    time.sleep(2)
    print('Que com muito esforço porporcionaram essa aventura para vocês!')
    time.sleep(1.5)
    print('Agradecemos desde já o seu tempo, e desejamos uma boa experiência')
    time.sleep(1.5)
    print('------------------------------------------------------------------\n')
    time.sleep(1)
    nome = input('Qual o seu Nome?')
    introducao()

else:
    print('Digite "Sim" para continuar')