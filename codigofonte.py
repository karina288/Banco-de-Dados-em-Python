def criar_tabela(nomearquivo1):
    arquivo = open(nomearquivo1, 'w')
    arquivo.write(str('============ BANCO DE DADOS DE DORAMAS ============ \n'))
    arquivo.write(str("Nome\tTipo\tGênero\tNº episódios\tTerminado[S/N]\tEpisódio de parada \n"))
    arquivo.close()


def gravar_tabela(nomearquivo2):
    arquivo = open(nomearquivo2, 'r+')
    for linha in arquivo:
        print(linha)
    print("Adicione informações na sua tabela")
    nome = arquivo.write(str(input('Digite o nome do dorama: ')+ ('\t')))
    tipo = arquivo.write(str(input('Digite o tipo do dorama: ')+('\t')))
    genero = arquivo.write(str(input('Digite o gênero do dorama: ')+('\t')))
    n_episodios = arquivo.write(str(input('Digite o número de episódios: ')+('\t')))
    terminado = arquivo.write(str(input('Você terminou de assistir? Digite S para sim ou N para Não: ')+('\t')))
    episodiodeparada = arquivo.write(str(input("Digite o episódio em que você parou. Caso já tenha terminado de assistir ao dorama preencha o campo com '--' dorameira(o): ")+('\n')))
    arquivo.close()


def ler_tabela(nomearquivo3):
    arquivo = open(nomearquivo3, 'r')
    for linha in arquivo:
        print(linha)
    arquivo.close()


import os


def apagar_tabela(nomearquivo4):
    print("Digite [ 1 ] para apagar apenas a tabela")
    print("Digite [ 2 ] para apagar o arquivo")
    escolha = int(input("Digite a sua escolha Dorameira(o): "))
    if escolha == 1:
        arquivo = open(nomearquivo4, 'w')
        arquivo.close()
        criar_tabela(nomearquivo4)
        print()
        print("Tabela apagada com sucesso Dorameira(o)!")

    if escolha == 2:
        arquivo = nomearquivo4
        os.remove(arquivo)
        print()
        print("Arquivo apagado com sucesso Dorameira(o)!")


from functools import cmp_to_key


def cmp_nomes(linha1, linha2):
    if linha1[0] < linha2[0]:
        return -1
    elif linha1[0] == linha2[0]:
        return 0
    else:
        return 1


def cmp_episodios(linha1, linha2):
    if int(linha1[3]) < int(linha2[3]):
        return -1
    elif int(linha1[3]) == int(linha2[3]):
        return 0
    else:
        return 1


def listardados_tabela(nomearquivo5):
    print("Como deseja ordenar seus doramas?")
    print("Digite [ 1 ] para ordenar por ordem alfabética")
    print("Digite [ 2 ] para ordenar por número de episódios")
    escolha = int(input("Digite a sua escolha:  "))
    print()
    aux = []
    arquivo = open(nomearquivo5, 'r')
    arquivo.readline()
    for linha in arquivo:
        linha.rstrip('\n')
        aux.append(linha.split('\t'))
    aux2 = (aux[0])
    aux = (aux[1:])

    if escolha == 1:
        aux.sort(key=cmp_to_key(cmp_nomes))
        print('   '.join(aux2))
        for i in aux:
            print('   '.join(i))

    if escolha == 2:
        aux.sort(key=cmp_to_key(cmp_episodios))
        print('   '.join(aux2))
        for i in aux:
            print('   '.join(i))


def consultar_registro(nomearquivo6):
    nome = str(input("Digite o nome do dorama que você deseja consultar o registro: "))
    print()
    arquivo = open(nomearquivo6, 'r')
    arquivo.readline()
    aux = []
    for linha in arquivo:
            linha.rstrip('\n')
            aux.append(linha.split('\t'))
    aux2 = (aux[0])
    aux3 = (aux[1:])

    def encontrar(nome):
        filtro = []
        pos = 0
        for i in aux3:
            for j in i:
                if nome in j:
                    pos = i
                    filtro.append(pos)
        return filtro

    print(' '.join(aux2))
    x = encontrar(nome)
    for i in x:
        print(' '.join(i))


def inserir_novoregistro(nomearquivo7):
    gravar_tabela(nomearquivo7)


def apagar_registro(nomearquivo8):
    nome = str(input("Digite o nome do dorama que você deseja apagar o registro: "))
    print()
    arquivo = open(nomearquivo8, 'r')
    arquivo.readline()
    aux = []
    for linha in arquivo:
            linha.rstrip('\n')
            aux.append(linha.split('\t'))
    aux2 = (aux[0])
    aux3 = (aux[1:])

    def encontrar(nome):
        filtro = []
        pos = 0
        for i in aux3:
            for j in i:
                if nome in j:
                    pos = i
                    filtro.append(pos)
                    aux3.remove(pos)
        return filtro


    x = encontrar(nome)
    arquivo.close()
    lista = []

    for i in aux3:
        lista.append('t'.join(i))

    #Pra apagar a tabela
    arquivo = open(nomearquivo8, 'r')
    arquivo.close()

    arquivo = open(nomearquivo8, 'w')
    arquivo.write(str('============ BANCO DE DADOS DE DORAMAS ============ \n'))
    arquivo.write(str("Nome\tTipo\tGênero\tNº episódios\tTerminado[S/N]\tEpisódio de parada \n"))
    for i in lista:
        arquivo.write(i)
    arquivo.close()

    ler_tabela(nomearquivo8)


def listagem_total_friltada(nomearquivo9):
    print("Como deseja listar sua tabela? ")
    print("Digite [ 1 ] listagem total de seus doramas")
    print("Digite [ 2 ] para listagem filtrada com base no tipo do Dorama")
    escolha = int(input("Digite a sua escolha: "))
    if escolha == 1:
        ler_tabela(nomearquivo9)

    if escolha == 2:
        print("Digite [ 1 ] para K-dramas")
        print("Digite [ 2 ] para J-Dramas")
        print("Digite [ 3 ] para C-Dramas")
        print("Digite [ 4 ] para Thai-Dramas ")
        op = int(input("Digite a sua escolha: "))
        print()
        arquivo = open(nomearquivo9, 'r')
        arquivo.readline()
        aux = []
        for linha in arquivo:
            linha.rstrip('\n')
            aux.append(linha.split('\t'))
        aux2 = (aux[0])
        aux3 = (aux[1:])

        def encontrar(tipo):
            filtro = []
            pos = 0
            for i in aux3:
                for j in i:
                    if tipo in j:
                        pos = i
                        filtro.append(pos)
            return filtro

        if op == 1:
            tipo = 'K-drama'
            print(' '.join(aux2))
            x = encontrar(tipo)
            for i in x:
                print(' '.join(i))

        elif op == 2:
            tipo = 'J-drama'
            print(' '.join(aux2))
            x = encontrar(tipo)
            for i in x:
                print(' '.join(i))

        elif op == 3:
            tipo = 'C-drama'
            print(' '.join(aux2))
            x = encontrar(tipo)
            for i in x:
                print(' '.join(i))

        elif op == 4:
            tipo = 'C-drama'
            print(' '.join(aux2))
            x = encontrar(tipo)
            for i in x:
                print(' '.join(i))


def sair_programa():
    exit()


#Programa Principal
op = 1
nome = str(input("Digite o seu nome Dorameira(o): "))
print("** BEM-VINDA(O) AO SEU BANCO DE DORAMAS {} ** ".format(nome.upper()))
print()
while op != 0:
    print('===================================================')
    print("MENU INICIAL")
    print('''[ 1 ] - Criar tabela
[ 2 ] - Gravar tabela no arquivo
[ 3 ] - Ler tabela do arquivo
[ 4 ] - Apagar tabela do arquivo
[ 5 ] - Listar dados da tabela
[ 6 ] - Consultar um registro
[ 7 ] - Inserir novo registro na tabela
[ 8 ] - Apagar registro
[ 9 ] - Listagem total ou filtrada
[ 0 ] - Sair do programa''')
    print('====================================================')
    print()
    qtd = 6
    op = int(input("Digite a sua opção: "))
    if op == 1:
        filename = str(input("Digite um nome para o arquivo e adicione a extensão.csv no final: "))
        criar_tabela(filename)
        print()
        print("Tabela Criada com sucesso Dorameira(o)!")

    elif op == 2:
        filename2 = str(input("Digite o nome do arquivo com a extensão.csv no final: "))
        gravar_tabela(filename2)
        print()
        print("Tabela gravada com sucesso Dorameira(o)!")

    elif op == 3:
        filename3 = str(input("Digite o nome do arquivo com a extensão.csv no final: "))
        ler_tabela(filename3)
        print()
        print("Tabela lida com sucesso Dorameira(o)!")

    elif op == 4:
        filename4 = str(input("Digite um nome para o arquivo e adicione a extensão.csv no final: "))
        apagar_tabela(filename4)

    elif op == 5:
        filename5 = str(input("Digite o nome do arquivo, com a extensão .csv no final, que contém a tabela que você desjea ordenar: "))
        listardados_tabela(filename5)
        print()
        print("Tabela ordenada com sucesso Dorameira(o)!")

    elif op == 6:
        filename6 = str(input("Digite o nome do arquivo com a extensão.csv no final: "))
        consultar_registro(filename6)

    elif op == 7:
        filename7 = str(input("Digite o nome do arquivo com a extensão .csv no final: "))
        inserir_novoregistro(filename7)
        print()
        print("Novo registro adicionado com sucesso Dorameira(o)!!")

    elif op == 8:
        filename8 = str(input("Digite o nome do arquivo com a extensão .csv no final: "))
        apagar_registro(filename8)
        print("Registro apagado com sucesso Dorameira(o)!")

    elif op == 9:
        filename9 = str(input("Digite o nome do arquivo com a extensão .csv no final: "))
        listagem_total_friltada(filename9)

    elif op == 0:
        print("Programa encerrado com sucesso!")
        sair_programa()

    else:
        print("Opção inválida Dorameira(o)! Tente de novo!")
    print()
