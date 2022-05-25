import os
import time
import random

# Criando Arquivo de Pergunta " Pergunta.txt "

def cria_aquivos():
    arquivo = open("pergunta.txt", "w")

    arquivo.write("Japão\n")
    arquivo.write("Portugal\n")
    arquivo.write("Espanha\n")
    arquivo.write("China\n")
    arquivo.write("Brasil\n")
    arquivo.write("Peru\n")
    arquivo.write("Afeganistão\n")
    arquivo.write("Africa do Sul\n")
    arquivo.write("Albânia\n")
    arquivo.write("Alemanha\n")
    arquivo.write("Andorra\n")
    arquivo.write("Angola\n")

    arquivo.close()
    # Criando Arquivo de Resposta " Resposta.txt "
    arquivo_r = open("resposta.txt", "w" )
    
    arquivo_r.write("Toquio\n".lower())
    arquivo_r.write("Lisboa\n".lower())
    arquivo_r.write("Madri\n".lower())
    arquivo_r.write("Pequim\n".lower())
    arquivo_r.write("Brasilia\n".lower())
    arquivo_r.write("Lima\n".lower())
    arquivo_r.write("Cabul\n".lower())
    arquivo_r.write("pretoria\n".lower())
    arquivo_r.write("tirana\n".lower())
    arquivo_r.write("berlim\n".lower())
    arquivo_r.write("andorra-a-velha\n".lower())
    arquivo_r.write("luanda\n".lower())
    arquivo_r.close()

    arquivo_alt = open("alternativas.txt", "w" )

    arquivo_alt.write("Brasilia Toquio Lima f\n".lower())
    arquivo_alt.write("Lisboa Roma Guatemala f\n".lower())
    arquivo_alt.write("Daca Madri Viena f\n".lower())
    arquivo_alt.write("Pequim Luanda Bacu m\n".lower())
    arquivo_alt.write("Argel Brasilia minsque m\n".lower())
    arquivo_alt.write("Lima Bogota Santiago m\n".lower())
    arquivo_alt.write("viena cabul bacu d\n".lower())
    arquivo_alt.write("daca argel pretoria d\n".lower())
    arquivo_alt.write("camberra tirana Viena d\n".lower())
    arquivo_alt.write("moscou saraievo Berlim f\n".lower())
    arquivo_alt.write("Argel andorra-a-velha doa d\n".lower())
    arquivo_alt.write("Luanda laundé jamena d\n".lower())

    arquivo_alt.close()

cria_aquivos()

def menu():
    print("="*100)
    print("Escolha uma das opções")
    print("1 - iniciar jogo")
    print("2 - adicionar paises")
    print("4 - sair")
    opcao = int(input('Digite sua opção:  '))
    if opcao == 1:
        iniciar_jogo()
    elif opcao == 2:
        add_paises()
    else:
        exit(1)


#ADD PAISES
def add_paises():
    print('ADD PAISES')
    add=input('Você deseja adicionar algum pais ao jogo? ( S / N) ').lower()
    if add == 's':
      print('Vamos lá')
      qt=int(input('Qantos paises você deseja adicionar: '))
      with open('pergunta.txt', 'r') as arq:
          lista = arq.readlines()
      for linha in lista:
          print(linha)
      for i in range(1, (qt+1)):
            p=input('Digite um pais que não esteja na lista:')
            linha=('{}\n'.format(p))
            with open('pergunta.txt', 'a') as arq:
             arq.write(linha)
            
            print()
            print('Agora digite as três alternativas para a\nresposta com duas erradas e a correta\ne o grau de dificudade\nF: facil\nM: medio\nD: dificio')
            alt1=input('digite a primeira alternativa: ')
            alt2=input('digite a segunda alternativa: ')
            alt3=input('digite a terceira alternativa: ')
            g=input('Digite o grau de dificuldade: ')
            linha2=('{} {} {} {}\n'.format(alt1,alt2,alt3,g))
            with open('alternativas.txt', 'a') as arq2:
                arq2.write(linha2)
            c=input('Agora digite a alternativa correta: ')
            linha1=('{}\n'.format(c))
            with open('resposta.txt', 'a') as arq1:
                arq1.write(linha1)
    
    input("aperte qualquer tecla para voltar ao menu")
    menu()


def add_escore(contador):
    print()
    nome = input('Digite seu nome: ')
    print('Parabens ',nome, 'esta foi sua pontuação ',contador)

    jogador=('Nome:{}    Pontos:{}\n'.format(nome,contador))
    with open('escore.txt' ,'a', encoding="utf-8") as arq:
        
        arq.write(jogador)
    with open('escore.txt','r') as arq:
        linhas = arq.readlines()
    for linha in linhas:
        print(linha)
    
   # exibir_pontuacao()

# COMEÇA A JOGAR NESTE PONTO:
def iniciar_jogo():
    contador = 0
    r=[]
    perguntas = []
    
    while r !=['sair']:
        #contar linhas do arquivo
        file = open("pergunta.txt", "r")
        Counter = 0

        Content = file.read()
        CoList = Content.split("\n")

        for i in CoList:
            if i:
                Counter += 1

        k=Counter 

        # Numero Aleatorio 
        while True:
            s= random.randrange(1,k)
            if(not s in perguntas):
                perguntas.append(s)
                break

        # Abrir Linha Especifica arquivo " pergunta.txt "
        with open("pergunta.txt") as f:
            data = f.readlines()[ s]
            line = data.rstrip('\n')
            dados=[]
            dados.append(line)


        # Abrir Linha Especifica Aquivo " Resposta.txt "
        with open("resposta.txt") as r:
            data1 = r.readlines()[ s]
            line1 = data1.rstrip('\n')
            line_1 = line1.split(' ')
            dados1=[]
            dados1.append(line_1)


        # Abrir Linha Especifica Arquivo " Alternativas "
        with open("alternativas.txt") as a:
            data2 = a.readlines()[s]
            line2 = data2.rstrip('\n')
            line3 = line2.split(' ')
            dados2 = [line3]


        # Pergunta ao Jogador
        print()
        print('Digite a Capital do Pais Relacionado: ')
        print()
        print('Qual a capital  (da ou do): ',*dados)
        print()
        print('Alternativas: \na) {}\nb) {}\nc) {}'.format(dados2[0][0],dados2[0][1],dados2[0][2]))
        #print('Resposta: ',dados1[0])# linha para controle funcional

        r = [input('Digite a alternativa correta\nCaso queira terminar o jogo digite sair: ').strip()]

        if r == dados1[0] and dados2[0][3] == 'f':
            print('----- Parabens voce acertou ! -----')
            contador += 10
        if r == dados1[0] and dados2[0][3] == 'm':
            print('----- Parabens voce acertou ! -----')
            contador += 15
        if r == dados1[0] and dados2[0][3] == 'd':
            print('----- Parabens voce acertou ! -----')
            contador += 20
        

        time.sleep(1)
        print("="*100)
        #finaliza após 5 perguntas
        if(len(perguntas) > 4):
           break
    add_escore(contador)
    input("aperte qualquer tecla para voltar ao menu")
    menu()
    
    
    
menu()