import time
dicionario = {}
usuarios = {}

#OUTRAS FUNÇÕES:
def removerBarra(string):
    """
    Essa função recebe uma string que contenha '/n' e retira-o retornando apenas a string.
    """
    palavra = ""
    for x in string:
        if x != "\n":
            palavra+=x
    return palavra


#CRIPTOGRAFIA:
def crip(string):
    """
    Função recebe uma string e criptografa, a sua criptografia consiste em abrir o arquivo de "chavePublica.txt",
    depois pega os valores de "e" e "n" para podermos utilizar na formula da critografia no segundo for.
    """
    arquivo = open("./keys/chavePublica.txt","r")
    lista2 = arquivo.readlines()
    for x in lista2:
        e = ""
        n = ""
        flag = False
        for numero in x:
            if numero != " " and flag == False:
                e+=numero
            elif numero == " ":
                flag = True
            elif numero != "\n":
                n+=numero
    string2 = ""
    for caractere in string:
        string2 += str((ord(caractere)**int(e))%int(n)) + ' '
    return string2

def descrip(string):
    """
    Função recebe uma string e descriptogra, a sua descriptografia consiste em abrir o arquivo "chavePrivada.txt",
    depois pega os valores de "d" e "n" para podermos utilizar na formula da descriptofragia no terceiro for.
    """
    arquivo = open("./keys/chavePrivada.txt","r")
    lista2 = arquivo.readlines()
    for x in lista2:
        d = ""
        n = ""
        flag = False
        for numero in x:
            if numero != " " and flag == False:
                d+=numero
            elif numero == " ":
                flag = True
            elif numero != "\n":
                n+=numero
    lista = []
    string2 = ""
    for caractere in string:
        if caractere != " ":
            string2+=caractere
        elif caractere == " ":
            lista.append(string2)
            string2 = ""
    string3 = ""
    for x in lista:
        string3 += chr((int(x)**int(d))%int(n))
    return string3

#FUNÇÕES DO MENU:
def cadastrar(dicionario,cpf,disciplina,cpfProfessor=""):
    """
    Função com objetivo de cadastrar as notas do aluno no dicionário.
    """
    nome = input("Nome: ")
    nota1 = input("Nota da 1º Unidade: ")
    nota2 = input("Nota da 2º Unidade: ")
    media = (float(nota1)+float(nota2))/2
    tempo = time.asctime()
    dicionario[cpf,disciplina] = (nome,nota1,nota2,str(media),tempo)
    arquivo = open("log.txt","a")
    arquivo.writelines(f"— O CPF '{cpfProfessor}' cadastrou o cpf '{cpf}' no nome de '{nome}' na data e hora [{tempo}]\n")
    arquivo.close()
    return

def remover(dicionario,cpf,disciplina,cpfProfessor=""):
    """
    Função com objetivo de remover um aluno no dicionário.
    """
    flag = False
    tempo = time.asctime()
    for x in dicionario.keys():
        if cpf == x[0] and disciplina == x[1]:
            flag = True
            chave = x  
    if flag == True:
        print("Aluno removido com sucesso")
        dicionario.pop(chave)
        arquivo = open("log.txt","a")
        arquivo.writelines(f"— O CPF '{cpfProfessor}' removeu o cpf '{cpf}' na data e hora [{tempo}]\n")
        arquivo.close()
    elif flag == False:
        print("Não há alunos de acordo com a sua disciplina!")
    return

def atualizar(dicionario,cpf,disciplina,cpfProfessor=""):
    """
    Função com objetivo de atualizar os dados de um aluno no dicionário.
    """
    flag = False
    novaMedia = False
    arquivo = open("log.txt","a")
    for x in dicionario.keys():
        tempo = time.asctime()
        if cpf == x[0] and disciplina == x[1]:
            flag = True
            nome = dicionario[x][0] #Pode alterar
            nota1 = dicionario[x][1] #Pode alterar
            nota2 = dicionario[x][2] #Pode alterar
            media = dicionario[x][3] #Pode alterar
            dataCadastro = dicionario[x][4] #Não pode alterar
            atualizacao = time.asctime() #Não pode alterar
            alterar = input(f"\nO que deseja alterar do aluno {nome}: \n[1] = nome \n[2] = nota da 1º unidade \n[3] = nota da 2º unidade \n[4] = nota da média \n")        
            if alterar == "1":
                nome = input(f"Digite novo nome para substituir {nome}: ")
                arquivo.writelines(f"— O CPF '{cpfProfessor}' atualizou o nome cadastrado no '{cpf}' na data e hora [{tempo}]\n")
            elif alterar == "2":
                nota1 = input(f"Nova nota da 1º unidade de {nome}: ")
                arquivo.writelines(f"— O CPF '{cpfProfessor}' atualizou a nota da 1º unidade cadastrado no '{cpf}' na data e hora [{tempo}]\n")
                novaMedia = True
            elif alterar == "3":
                nota2 = input(f"Nova nota da 2º unidade de {nome}: ")
                novaMedia = True
                arquivo.writelines(f"— O CPF '{cpfProfessor}' atualizou a nota da 2º unidade cadastrado no '{cpf}' na data e hora [{tempo}]\n")
            elif alterar == "4":
                media = input(f"Nova nota da média de {nome}: ")
                arquivo.writelines(f"— O CPF '{cpfProfessor}' atualizou a média cadastrado no '{cpf}' na data e hora [{tempo}]\n")
    arquivo.close()
    if flag == True and novaMedia == True:
        print("Atualizado com sucesso!")
        media = (float(nota1)+float(nota2))/2
        dicionario[cpf,disciplina] = (nome,nota1,nota2,str(media),dataCadastro,atualizacao)
    elif flag == True:
        print("Atualizado com sucesso!")
        dicionario[cpf,disciplina] = (nome,nota1,nota2,str(media),dataCadastro,atualizacao)
    elif flag == False:
        print("Aluno não encontrado de acordo com a sua disciplina!")
    return

def encontrarPorDisciplina(dicionario,cpf,disciplina,cpfProfessor=""):
    """
    Função com objetivo de encontrar o cadastro de apenas um aluno no dicionário de acordo com a disciplina.
    """
    flag = False
    for x in dicionario.keys():
        if cpf == x[0] and disciplina == x[1]:
            flag = True
            print("Perfil encontrado!")
            print(f"CPF: {cpf}")
            print(f"Nome: {dicionario[(cpf,disciplina)][0]}")
            print(f"Nota1: {dicionario[(cpf,disciplina)][1]}")
            print(f"Nota2: {dicionario[(cpf,disciplina)][2]}")
            print(f"Media: {dicionario[(cpf,disciplina)][3]}")
            print(f"Data de Cadastro: {dicionario[(cpf,disciplina)][4]}")
            print(f"Disciplina: {x[1]}\n")
    if flag == True:
        arquivo = open("log.txt","a")
        tempo = time.asctime()
        arquivo.writelines(f"— O CPF {cpfProfessor} fez uma busca pela disciplina {disciplina} no cpf '{cpf}' na data e hora [{tempo}]\n")
        arquivo.close()
    elif flag == False:
        print("Aluno não encontrado!")
    return

def encontrarTodasDisciplina(dicionario,cpf,cpfProfessor=""):
    """
    Função com objetivo de encontrar o cadastro de apenas um aluno no dicionário de todas as disciplinas.
    """
    flag = False
    for x in dicionario.keys():
        if cpf == x[0]:
            flag = True
            print(f"CPF: {cpf}")
            print(f"Nome: {dicionario[x][0]}")
            print(f"Nota1: {dicionario[x][1]}")
            print(f"Nota2: {dicionario[x][2]}")
            print(f"Media: {dicionario[x][3]}")
            print(f"Data de Cadastro: {dicionario[x][4]}")
            print(f"Disciplina: {x[1]}\n")
    if flag == True:
        arquivo = open("log.txt","a")
        tempo = time.asctime()
        arquivo.writelines(f"— O CPF {cpfProfessor} fez uma busca por TODAS as disciplinas no cpf '{cpf}' na data e hora [{tempo}]\n")
        arquivo.close()
    elif flag == False:
        print("Aluno não encontrado!")
    return

def ordenar(dicionario, disciplina, cpfProfessor=""):
    """
    Função com objetivo de ordenar todos os alunos do dicionário por ordem de nome.
    """
    lista = []
    flag = False
    for x in dicionario.keys():
        nome = dicionario[x][0]
        nota1 = dicionario[x][1]
        nota2 = dicionario[x][2]
        media = dicionario[x][3]
        dataCadastro = dicionario[x][4]
        lista.append([x[0],x[1],nome,nota1,nota2,media,dataCadastro])

    #Bubblesort:
    cont = 0
    while cont<len(lista):
        cont2 = 0
        while cont2<len(lista)-1:
            if lista[cont2][2]>lista[cont2+1][2]:
                flag = lista[cont2+1]
                lista[cont2+1] = lista[cont2]
                lista[cont2] = flag
            cont2+=1
        cont+=1
    #Todos em ordem:    
    cont = 0
    flag = False
    arquivo = open("log.txt","a")
    tempo = time.asctime()
    while cont<len(lista):
        if disciplina == lista[cont][1]:
            arquivo.writelines(f"— O CPF {cpfProfessor} fez uma ordenação por nome na data e hora [{tempo}]\n")
            if flag == False:
                print(f"Todos os alunos cadastrados por ordem de nome na sua disciplina: {disciplina}\n")
                flag = True
            print(f"CPF: {lista[cont][0]}")
            print(f"Disciplina: {lista[cont][1]}")
            print(f"Nome: {lista[cont][2]}")
            print(f"Nota1: {lista[cont][3]}")
            print(f"Nota2: {lista[cont][4]}")
            print(f"Media: {lista[cont][5]}")
            print(f"Data de Cadastro: {lista[cont][6]}\n")
        cont+=1
    return flag

def relatorio(dicionario, cpfProfessor=""):
    """
    Função com objetivo de criar um relatório com todos os cadastro de acordo com a disciplina do professor, incluindo as atualizações que foram feitas.
    """
    lista = []
    cont = 0
    for x in dicionario.items():
        lista.append(x)
        
    novaLista = []
    cont = 0
    while cont<len(lista):
        if len(lista[cont][1]) == 5:
            chave = lista[cont][0]
            valor = lista[cont][1]
            novaLista.append([chave[0],chave[1],valor[0],valor[1],valor[2],valor[3],valor[4]])
        elif len(lista[cont][1]) > 5:
            chave = lista[cont][0]
            valor = lista[cont][1]
            cont2 = 0
            lis = []
            lis.append(chave[0])
            lis.append(chave[1])
            while cont2<len(lista[cont][1]):
                lis.append(valor[cont2])
                cont2+=1
            novaLista.append(lis)
        cont+=1
     
    arquivo = open("relatorio.txt","a")
    cont = 0
    while cont<len(novaLista):
        lista = novaLista
        if len(novaLista[cont]) == 7:
            arquivo.writelines(f"Cadastro Nº{cont}\n")
            arquivo.writelines(f"CPF: {lista[cont][0]}\n")
            arquivo.writelines(f"Disciplina: {lista[cont][1]}\n")
            arquivo.writelines(f"Nome: {lista[cont][2]}\n")
            arquivo.writelines(f"Nota1: {lista[cont][3]}\n")
            arquivo.writelines(f"Nota2: {lista[cont][4]}\n")
            arquivo.writelines(f"Media: {lista[cont][5]}\n")
            arquivo.writelines(f"Data de Cadastro: {lista[cont][6]}\n\n")
        elif len(novaLista[cont]) >7:
            cont2 = 7
            arquivo.writelines(f"Cadastro Nº{cont}\n")
            arquivo.writelines(f"CPF: {lista[cont][0]}\n")
            arquivo.writelines(f"Disciplina: {lista[cont][1]}\n")
            arquivo.writelines(f"Nome: {lista[cont][2]}\n")
            arquivo.writelines(f"Nota1: {lista[cont][3]}\n")
            arquivo.writelines(f"Nota2: {lista[cont][4]}\n")
            arquivo.writelines(f"Media: {lista[cont][5]}\n")
            arquivo.writelines(f"Data de Cadastro: {lista[cont][6]}\n")
            while cont2<len(novaLista[cont]):
                arquivo.writelines(f"Atualização: {lista[cont][cont2]}\n")
                cont2+=1
            arquivo.writelines("\n")
        cont+=1
    arquivo.close()
    arquivo = open("log.txt","a")
    tempo = time.asctime()
    arquivo.writelines(f"— O CPF '{cpfProfessor}' fez um relatório na data e hora [{tempo}]\n")
    arquivo.close()
    return flag

def relatorioPlanilha(dicionario, disciplina,cpfProfessor=""):
    """
    Função com objetivo de criar um relatório no arquivo CSV com todos os cadastro de acordo com a disciplina do professor.
    """
    lista = []
    for x in dicionario.keys():
        nome = dicionario[x][0]
        nota1 = dicionario[x][1]
        nota2 = dicionario[x][2]
        media = dicionario[x][3]
        dataCadastro = dicionario[x][4]
        lista.append([x[0],x[1],nome,nota1,nota2,media,dataCadastro])
    #Bubblesort:
    cont = 0
    while cont<len(lista):
        cont2 = 0
        while cont2<len(lista)-1:
            if lista[cont2][2]>lista[cont2+1][2]:
                flag = lista[cont2+1]
                lista[cont2+1] = lista[cont2]
                lista[cont2] = flag
            cont2+=1
        cont+=1
    #Escrevendo na Planilha:
    import csv
    with open('relatorio.csv', 'w', newline='') as csvfile:
        escrita = csv.writer(csvfile, delimiter=';')
        escrita.writerow(["Nomes"]+["Nota da 1º Unidade"]+["Nota da 2º Unidade"]+["Média Final"])
        for elementos in lista:
            if disciplina == elementos[1]:
                escrita.writerow([f"{elementos[2]}",f"{elementos[3]}",f"{elementos[4]}",f"{elementos[5]}"])
    arquivo = open("log.txt","a")
    tempo = time.asctime()
    arquivo.writelines(f"— O CPF '{cpfProfessor}' fez um relatório em CSV na data e hora [{tempo}]\n")
    arquivo.close()
    return

#>>>>>>> CADASTRO E LOGIN:
def cadastrarPessoas(usuarios):
    """
    Função com objetivo de cadastrar alunos ou professores no sistema.
    """
    print(35*"-=")
    print("[Digite a opção de acordo com o número, você é professor ou aluno?]")
    print(35*"-=")
    cadastro = input("[1] — Professor \n[2] — Aluno \nDigite a sua opção: ")
    flag = False
    arquivo = open("log.txt","a")
    tempo = time.asctime()
    if cadastro == "1" or cadastro == "2":
        cpf = input("Digite seu CPF: ")
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        arquivo.writelines(f"— O CPF '{cpf}' foi cadastrado no banco de dados na data e hora [{tempo}]\n")
        arquivo.close()
        flag = True
    if cadastro == "1":
        disciplina = input("Digite a disciplina que você ensina: ")
        print("Cadastro realizado com sucesso!")
        usuarios[cpf] = (cadastro,nome,senha,disciplina)
    elif cadastro == "2":
        print("Cadastro realizado com sucesso!")
        usuarios[cpf] = (cadastro,nome,senha)
    if flag == False:
        print("Opção digitada incorretamente!")
    return
        
def login(usuarios,cpf):
    """
    Função com objetivo de fazer login de alunos ou professores no sistema.
    """
    flag = False
    senha = input("Senha: ")
    for x in usuarios.keys():
        if cpf == x and senha == usuarios[x][2]:
            flag = True
            print(f"\n>>>>> Seja bem vindo |{usuarios[x][1]}|\n")
            nivelAcesso = usuarios[x][0]
    if flag == False:
        print(">>>>> Usuário não encontrado!")
    elif flag == True:
        return nivelAcesso

def conferirDisciplina(usuarios,cpf):
    """
    Função serve para retornar o nome dos professores nos usuários, isso será usado depois caso ele queira
    adicionar, remover, atualizar ou buscar um aluno de acordo com a sua disciplina.
    """
    flag = False
    for x in usuarios.keys():
        if cpf == x and usuarios[x][0] == "1":
            nomeDisciplina = usuarios[x][3]
    return nomeDisciplina

def alterarNivel(usuarios,cpf,disciplina,cpfProfessor=""):
    """
    Função com objetivo de alterar o nível de um aluno para monitor, os monitores tem o mesmo nível de acesso de um professor.
    """
    flag = False
    for x in usuarios.keys():
        if cpf == x:
            pergunta = input(f"Você deseja alterar o nível de acesso de {usuarios[x][1]}? \n[1] = Sim \n[2] = Não \n")
            if pergunta == "1":
                flag = True
                cpf = x
                nome = usuarios[x][1]
                senha = usuarios[x][2]
            elif pergunta == "2":
                print("Até mais!")
            else:
                print("Opção invalida!")
    if flag == True:
        arquivo = open("log.txt","a")
        tempo = time.asctime()
        arquivo.writelines(f"— O CPF '{cpfProfessor}' alterou o nível do cpf '{cpf}' na data e hora [{tempo}]\n")
        arquivo.close()
        usuarios.pop(cpf)
        usuarios[cpf] = ("1",nome,senha,disciplina)
        print("Nível de acesso alterado com sucesso!")
    elif flag == False and pergunta == "1":
        print("CPF de aluno não encontrado!")
    return

#>>>>>>> ESCREVER TUDO NO ARQUIVO:
def tirarDoArquivoElementos():
    """
    Função com objetivo de tirar tudo que tem no arquivo elemento.txt e colocar no dicionario para poder ser manipulado posteriormente.
    """
    #Tirando do arquivo Elemento.txt e colocando em Dicionario:
    arquivo = open("elemento.txt","r")
    lista = arquivo.readlines()
    listaTotal = []
    lista2 = []
    for x in lista:
        if removerBarra(x) != "":
            lista2.append(descrip(removerBarra(x)))
        elif removerBarra(x) == "":
            listaTotal.append(lista2)
            lista2 = []    
    for x in listaTotal:
        cont = 2
        chave1 = x[0]
        chave2 = x[1]
        posicao = x
        lista = []
        while cont < len(posicao):
            lista.append(posicao[cont])
            cont+=1
        dicionario[chave1,chave2] = tuple(lista)
    arquivo.close()
    return

def tirarDoArquivoUsuarios():
    """
    Função com objetivo de tirar tudo que tem no arquivo Usuarios.txt e colocar no dicionario para poder ser manipulado posteriormente.
    """
    arquivo = open("usuarios.txt","r")
    lista = arquivo.readlines()
    listaTotal = []
    lista2 = []
    for x in lista:
        if removerBarra(x) != "":
            lista2.append(descrip(removerBarra(x)))
        elif removerBarra(x) == "":
            listaTotal.append(lista2)
            lista2 = []
    for x in listaTotal:
        chave = x[0]
        if len(x) == 5:
            usuarios[chave] = (x[1],x[2],x[3],x[4])
        elif len(x) < 5:
            usuarios[chave] = (x[1],x[2],x[3])
    arquivo.close()
    return

def escreverNoArquivoElemento():
    """
    Função com objetivo de tirar tudo que tem no dicionario e escrever no arquivo elemento.txt.
    """
    #Tirando de dicionario e escrevendo no arquivo Elemento.txt:
    arquivo = open("elemento.txt","w")
    for x,w in dicionario.items():
        if len(w) == 5:
            arquivo.writelines(crip(x[0])+"\n"+crip(x[1])+"\n"+crip(w[0])+"\n"+crip(w[1])+"\n"+crip(w[2])+"\n"+crip(w[3])+"\n"+crip(w[4])+"\n\n")
        elif len(w) > 5:
            cont = 0
            tamanho = len(w)
            while cont<tamanho:        
                if cont == 0:
                    arquivo.writelines(crip(x[0])+"\n"+crip(x[1])+"\n")
                    arquivo.writelines(crip(w[cont])+"\n")
                else:
                    arquivo.writelines(crip(w[cont])+"\n")
                cont+=1
            arquivo.writelines("\n")
    arquivo.close()
    
def escreverNoArquivoUsuarios():
    """
    Função com objetivo de tirar tudo que tem no dicionario/usuarios e escrever no arquivo usuarios.txt.
    """
    arquivo2 = open("usuarios.txt","w")
    #Tirando de usuarios e escrevendo no arquivo Usuarios.txt:
    for x,w in usuarios.items():
        if len(w) == 4:
            arquivo2.writelines(crip(x)+"\n"+crip(w[0])+"\n"+crip(w[1])+"\n"+crip(w[2])+"\n"+crip(w[3])+"\n\n")
        if len(w) == 3:
            arquivo2.writelines(crip(x)+"\n"+crip(w[0])+"\n"+crip(w[1])+"\n"+crip(w[2])+"\n\n")
    arquivo2.close()
    return

#>>>>>>> TRATAMENTO DE ERRO:
"""
Aqui ele vai tentar colocar tudo que estiver no arquivo usuarios no dicionario de usuarios.
Esse tratamento de erro tem como objetivo de mostrar um erro, caso os arquivos não exista.
"""

salvarCadastro = False
try:
    tirarDoArquivoUsuarios()
    salvarCadastro = True
except:
    salvarCadastro = False


#>>>>>>> MENU PRINCIPAL:
"""
Inicio do programa com todas as funções de cadastro, login e logout reunidas.
"""
flag = True
entrar = False
while flag:
    print(40*"=")
    print(" SEJA BEM VINDO AO NOSSO SISTEMA DE NOTAS!")
    print(40*"=")
    op = input("[1] = Cadastrar \n[2] = Login \n[3] = Sair \nDigite a sua opção: ")
    if (op == "1" and salvarCadastro == True) or op == "1":
        cadastrarPessoas(usuarios)
        escreverNoArquivoUsuarios()
    elif op == "2":
        cpfLogin = input("Digite seu CPF: ")
        acesso = login(usuarios,cpfLogin)
        if acesso == "1" or acesso == "2":
            flag = False
            entrar = True
    elif op == "3":
        print("Até mais!")
        flag = False
    else:
        print("Opção digitada incorretamente!")

#>>>>>>> TRATAMENTO DE ERRO2:
"""
Aqui o programa tentará usar a função tirarDoArquivoElementos() no qual tira tudo que tem no arquivo elemento.txt e coloca no dicionário
Esse tratamento de erro tem como objetivo de mostrar um erro caso o arquivo não exista.
"""
tirouDosArquivos = False
try:
    tirarDoArquivoElementos()
    tirouDosArquivos = True
except:
    tirouDosArquivos = False

#>>>>>>> SUB-MENU:
"""
Inicio do programa com todas as funções dos alunos e professores..
"""
while entrar:
    tempo = time.asctime()
    if acesso == "1":
        nomeDisciplina = conferirDisciplina(usuarios,cpfLogin)
        opcao = input("[1] = Cadastrar \n[2] = Remover \n[3] = Atualizar \n[4] = buscar \n[5] = Alterar Nível de acesso \n[6] = Ordenar todos por nome \n[7] = Gerar Relatório ou planilha \n[8] = Encerrar \n")
        arquivo3 = open("log.txt","a")
        if opcao == "8":
            escreverNoArquivoElemento()
            arquivo3.writelines(f"— O CPF '{cpfLogin}' encerrou o programa na data e hora [{tempo}]\n")
            print("Até mais!")
            entrar = False
            arquivo3.close()
        else:
            if tirouDosArquivos == True or opcao == "1":
                if opcao == "1":
                    cpf = input("CPF: ")
                    cadastrar(dicionario,cpf,nomeDisciplina,cpfLogin)
                    print("Nota de aluno cadastrado com sucesso!")
                    escreverNoArquivoElemento()
                    tirouDosArquivos = True
                elif opcao == "2":
                    cpf = input("Digite o CPF do aluno que deseja remover: ")
                    remover(dicionario,cpf,nomeDisciplina,cpfLogin)
                    escreverNoArquivoElemento()
                elif opcao == "3":
                    cpf = input("Digite o CPF para encontrarmos no Banco de Dados: ")
                    atualizar(dicionario,cpf,nomeDisciplina,cpfLogin)
                    escreverNoArquivoElemento()
                elif opcao == "4":
                    cpf = input("Digite o CPF que deseja encontrar: ")
                    encontrarPorDisciplina(dicionario,cpf,nomeDisciplina,cpfLogin)
                elif (opcao == "5" and salvarCadastro == True) or opcao == "5":
                    print(40*"-=")
                    print("ATENÇÃO: Para alterar o nível de acesso de um aluno para monitor na sua disciplina, ele precisará está cadastrado como aluno antes.")
                    print(40*"-=")
                    cpf = input("Digite o CPF do aluno que deseja alterar o nível: ")
                    alterarNivel(usuarios,cpf,nomeDisciplina,cpfLogin)
                    escreverNoArquivoUsuarios()
                elif opcao == "6":
                    if ordenar(dicionario,nomeDisciplina,cpfLogin) == False:
                        print("Não há nada para ordernar de acordo com a sua disciplina!")
                elif opcao == "7":
                    relatorioP = input("Digite o número da sua opção: \n[1] Relatório em arquivo \n[2] Planilha em csv \n")
                    if relatorioP == "1":
                        relatorio(dicionario,cpfLogin)
                        print("Relatório feito com sucesso!")
                    elif relatorioP == "2":
                        relatorioPlanilha(dicionario,nomeDisciplina,cpfLogin)
                        print("Planilha feito com sucesso!")
                    else:
                        print("Opção digitada incorretamente.")
            else:
                print("ERROR: Não há nada no arquivo! Cadastre algo novo para poder manipular. :D")
    elif acesso == "2":
        opcao = input("[1] = Conferir as notas por disciplina! \n[2] = Conferir as notas de todas disciplinas! \n[3] = Encerrar \n")
        tirarDoArquivoElementos()
        if opcao == "1":
            cpfAluno = input("Digite seu CPF novamente: ")
            disciplina = input("Digite o nome da disciplina que deseja encontrar: ")
            encontrarPorDisciplina(dicionario,cpfAluno,disciplina,cpfLogin)
        elif opcao == "2":
            cpfAluno = input("Digite seu CPF novamente: ")
            encontrarTodasDisciplina(dicionario,cpfAluno,cpfLogin)
        elif opcao == "3":
            print("Até mais!")
            entrar = False
