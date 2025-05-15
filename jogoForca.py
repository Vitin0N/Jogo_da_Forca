import json
import random
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def digita_letra(): #Função que pede uma letra, so aceita apenas 1 letra por vez
    while True:
        letra = input('Digite uma letra: ').lower()
        
        if len(letra) != 1 or not letra.isalpha(): #Aceita apenas 1 caracter e tem que ser uma letra
            print('Digite apenas uma letra.\n')
            continue

        clear()
        return letra

def verifica_palavras(palavra_certa, palavra_digitada):
    clear()

    if '*' in palavra_digitada: #Palavra ainda não completa - Jogo Continua
        return False

    if palavra_digitada.strip() == palavra_certa.strip():
        print('Você ACERTOU ~(￣▽￣)~\n'
              f'Palavra Correta: {palavra_certa.title()}') #Deixa a palavra com as primeiras letras maiusculas
        return True
    
    else:
        print('Você PERDEU (┬┬﹏┬┬)\n'
             f'Palavra Correta: {palavra_certa.title()}') #Deixa a palavra com as primeiras letras maiusculas
        return False
        

def mostra_palavra_digitada(letras, palavra_correta): #Mostra a quantidade de letras e/ou a palavra digitada pelo usuário
    palavra_oculta = ''
    
    for letra in palavra_correta:
        if letra in letras:
            palavra_oculta += letra #Caso letra existir

        else:
            palavra_oculta += '*'
   
    return palavra_oculta

def digita_opcao(max_digitado): #Função para escolher um numero entre 0 e o máximo permitido
    while True:
        opcao = input('Digite uma das opções: ')

        if opcao.isnumeric() and (int(opcao) > 0 and max_digitado >= int(opcao)): #verifica se o opcao é numero e só
            return int(opcao)                                                     #aceita valores (0 < opcao <=max_permitido)
                                                                                  #(0, max_permitido]
        else:
            print('Digite uma opção VÁLIDA!')

def sorteia_palavra(tema, base_dados): #Escolhe uma palavra aleátoria dependendo do tema
    palavra = random.choice(base_dados[tema])
    
    return palavra

def mostra_categoria(categorias):
    print('Todas as categorias!')
    for i, categoria in enumerate(categorias):
       
        print(f'[{i+1:2}] {categoria}') #Mostra as possiveis categorias com seus devidos valores
    
def verifica_letra(letra_digitada, letras, palavra_correta):
    if letra_digitada in letras:
        print('Letra já digitada!') #Letra ja está no conjuto, não perde vida
        return 0
    
    if letra_digitada not in palavra_correta: #Letra não pertence a palavra, perde uma vida
        return -1    
    
    else: # Acontece nada
        return 0
    
def mostra_opcoes(): #Mostra as opções para o jogo da forca
    print('[1] Tentar Letra\n'
          '[2] Tentar Palavra\n'
          '[3] Desistir')

def forca(tema, palavra): # Função que realiza o jogo
    vidas = '❤️'
    qnt_vidas = 5
    letras_digitadas = set()
    letras_digitadas.add(' ') #Adiciona o espaço, para caso tenha uma palavra composta

    while True:
        print(f'Tema: {tema}')

        mostra_opcoes()
        palavra_digitada = mostra_palavra_digitada(letras_digitadas, palavra) #Serve para saber a quantidade de letras, caso nenhuma letra digitada
        print('Vidas:', f'{vidas} '*qnt_vidas) #Multiplica o emoji pela quantidade de vidas restantes                               
        print(palavra_digitada) #Mostra a palavra

        if qnt_vidas == 0:
            verifica_palavras(palavra_certa=palavra, palavra_digitada='_palavra_errada_') #Perde o jogo caso as vidas zerem
            break

        op_forca = digita_opcao(3)
        match op_forca:
            case 1:
                letra_digitada = digita_letra()
                qnt_vidas += verifica_letra(letra_digitada, letras_digitadas, palavra)
                letras_digitadas.add(letra_digitada)
                palavra_digitada = mostra_palavra_digitada(letras_digitadas, palavra)

                if verifica_palavras(palavra, palavra_digitada):
                    break
                clear()

            case 2:
                palavra_digitada = input('Escreva a palavra correta: ').lower() #Chute para a palavra
                verifica_palavras(palavra, palavra_digitada)  
                break      
            
            case 3:
                verifica_palavras(palavra, palavra_digitada='_palavra_errada_') #Se desistir verifica uma palavra propositalmente 
                break                                                           #errada, para fazer o usuário perder         

with open('palavras.json', 'r', encoding='utf-8') as f: #Abre o banco de dados e tranfere para uma variável
    base_de_dados = json.load(f)

categorias = list(base_de_dados.keys()) #Pega apenas as categorias da base de dados

#menu principal

print('-==Bem-Vindo==-\n',
      'JOGO DA FORCA!')

while True:
    print(f'Digite uma opção:\n'
        '[1] Sortear Palavra\n'
        '[2] Escolher Tema\n'
        '[3] Sair')

    op = digita_opcao(3)

    match op:
        case 1:
            tema = random.choice(categorias) # Sorteia um tema aleátorio
            palavra = sorteia_palavra(tema, base_de_dados) #Sorteia uma palavra aleatória
            clear()

            forca(tema, palavra) #Chama a função do jogo

        case 2:
            mostra_categoria(categorias)
            op_categoria = digita_opcao(len(categorias))-1
            palavra_tema = sorteia_palavra(categorias[op_categoria], base_de_dados) #Escolhe uma palavra para aquele tema
            clear()

            forca(categorias[op_categoria],palavra_tema) #Chama a função do jogo passado o tema escolhido
        
        case 3:
            clear()
            print('Obrigado por jogar ヾ(￣▽￣) Bye~Bye~...')
            sys.exit() #Encerra o programa

        case _:
            print('Como você entrou aqui?')
            sys.exit() 

    print('Deseja continuar?\n'
          '[1] Sim\n'
          '[2] Não')
    
    op_continua = digita_opcao(2)
    clear()
    if(op_continua == 2):
        clear()
        print('Obrigado por jogar ヾ(￣▽￣) Bye~Bye~...')
        sys.exit() #Encerra o programa