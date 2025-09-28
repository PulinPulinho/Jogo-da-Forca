import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

#lista de palavras
palavras = [
    'computador', 'garrafa', 'janela', 'elefante', 'aventura',
    'biblioteca', 'chocolate', 'universo', 'guitarra', 'felicidade',
    'montanha', 'orquestra', 'lanterna', 'diamante', 'primavera',
    'carrossel', 'horizonte', 'floresta', 'teclado', 'viagem',
    'pinguim', 'galaxia', 'castelo', 'dinossauro', 'fotografia',
    'cachorro', 'navio', 'estrela', 'planeta', 'foguete',
    'magica', 'tesouro', 'pirata', 'segredo', 'memoria',
    'sonho', 'tempo', 'amor', 'amigo', 'chuva',
    'vento', 'fogo', 'terra', 'lua', 'sol',
    'ponte', 'rio', 'mar', 'luz', 'noite', 'abelha', 'borboleta', 'caminho', 'desenho', 'escola',
    'fantasma', 'girafa', 'historia', 'igreja', 'jardim',
    'laranja', 'morango', 'natureza', 'oculos', 'pintura',
    'queijo', 'relogio', 'silencio', 'trabalho', 'vizinho',
    'xadrez', 'zebra', 'amizade', 'barco', 'coragem',
    'dinheiro', 'espelho', 'familia', 'guerra', 'heroi',
    'ilha', 'jogo', 'letra', 'mundo', 'nuvem',
    'ouro', 'prata', 'quadro', 'risada', 'sapato',
    'tatuagem', 'unha', 'vidro', 'biscoito', 'ceu',
    'dente', 'forca', 'gelo', 'harpa', 'ideia'
]

#a palavra que foi escolhida da lista, separada em letras da palavra em uma lista
escolhida = list(random.choice(palavras))
#lista de letras que o jogador bota
player_word = []
#número de tentativas
tentativas = 6
#lista de letras erradas
erradas=[]

#criar uma lista com '_' para todos os algarismos da palavra
for i in range(len(escolhida)):
    player_word.append('_')


#O jogo
while True:
    print('------------------------------')

    #printar a forca em si
    if tentativas == 6:
        print('------')
        print(f'|    |     {(f'Letras erradas: {', '.join(str(num) for num in erradas)}')}')
        print('|   ')
        print('|   ')
        print('|           ', end='', flush=True)
    elif tentativas == 5:
        print('------')
        print(f'|    |     {(f'Letras erradas: {', '.join(str(num) for num in erradas)}')}')
        print('|    O')
        print('|   ')
        print('|           ', end='', flush=True)
    elif tentativas == 4:
        print('------')
        print(f'|    |     {(f'Letras erradas: {', '.join(str(num) for num in erradas)}')}')
        print('|    O')
        print('|    |')
        print('|           ', end='', flush=True)
    elif tentativas == 3:
        print('------')
        print(f'|    |     {(f'Letras erradas: {', '.join(str(num) for num in erradas)}')}')
        print('|    O')
        print('|   /|')
        print('|           ', end='', flush=True)
    elif tentativas == 2:
        print('------')
        print(f'|    |     {(f'Letras erradas: {', '.join(str(num) for num in erradas)}')}')
        print('|    O')
        print(f'|   /|{chr(92)}')
        print('|           ', end='', flush=True)
    elif tentativas == 1:
        print('------')
        print(f'|    |     {(f'Letras erradas: {', '.join(str(num) for num in erradas)}')}')
        print('|    O')
        print(f'|   /|{chr(92)}')
        print('|   /       ', end='', flush=True)

    #O status atual do jogo
    print(f'{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}{' '.join(map(str, player_word))}{Style.RESET_ALL}')
    #pegar o input do jogador, podendo ser uma letra ou a palavra inteira
    player_input = input('Escreva uma letra ou a palavra em si: ')

    #Se o input do jogador for uma letra
    if len(list(player_input)) == 1:
        #variavel para checar se a letra não combina com nenhuma letra da palavra
        contador = 0

        #iterar por todas as letras da palavra
        for i in range(len(escolhida)):
            #se a letra do jogador for igual a letra da iteração da palavra
            if player_input == escolhida[i]:
                #trocamos o "_" da lista de letras do jogador pela letra certa
                player_word[i] = escolhida[i]
            #se a letra do jogador não for igual a letra da iteração da palavra
            else:
                contador = contador+1
        #se a letra do jogador não for igual a nenhuma letra da palavra, damos a letra como um erro
        if contador >= len(escolhida):
            print('------------------------------')
            tentativas = tentativas-1
            erradas.append(player_input)
            
            print(f'{Fore.RED}{Style.BRIGHT}VOCÊ ERROU{Style.RESET_ALL}')
            print(f'Tentativas restantes: {tentativas}')

    #se o jogador tentar acertar a palavra
    elif len(list(player_input)) > 1:
        #se acertar
        if list(player_input) == escolhida:
            print('------------------------------')
            print(f'{Fore.GREEN}{Style.BRIGHT}VOCE ACERTOU A PALAVRA!!!!!{Style.RESET_ALL}')
            print(f'{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}{' '.join(map(str, escolhida))}{Style.RESET_ALL}')
            break
        #se errar
        else:
            print('------------------------------')
            tentativas = tentativas-1
            print(f'{Fore.RED}{Style.BRIGHT}VOCÊ ERROU{Style.RESET_ALL}')
            print(f'Tentativas restantes: {tentativas}')
    
    #se todas as letras estiverem preenchidas
    if player_word == escolhida:
            print('------------------------------')
            print(f'{Fore.GREEN}{Style.BRIGHT}VOCE ACERTOU A PALAVRA!!!!!{Style.RESET_ALL}')
            print(f'{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}{' '.join(map(str, escolhida))}{Style.RESET_ALL}')
            break
    if tentativas <= 0:
        print('------------------------------')
        print('------')
        print(f'|    |     {(f'Letras erradas: {', '.join(str(num) for num in erradas)}')}')
        print('|    O')
        print(f'|   /|{chr(92)}')
        print(f'|   / {chr(92)}    ', end='', flush=True)
        print(f'{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}{' '.join(map(str, player_word))}{Style.RESET_ALL}')
        print(' ')
        print(f'a palavra certa era: {' '.join(map(str, escolhida))}{Style.RESET_ALL}')
        print(f'{Fore.RED}{Style.BRIGHT}VOCE PERDEU{Style.RESET_ALL}')
        break
