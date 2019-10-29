import time
dicionario = {}
usuarios = {}

#OUTRAS FUNÇÕES:
def removerBarra(string):
    palavra = ""
    for x in string:
        if x != "\n":
            palavra+=x
    return palavra


#CRIPTOGRAFIA:
"""
Funções para criptografar, descriptogravar uma palavrar ou arquivo inteiro.
"""
def crip(string):    
    arquivo = open("chavePublica.txt","r")
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
    arquivo = open("chavePrivada.txt","r")
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
"""
Todas as funções do menu principal!
"""

def cadastrar(cpf,disciplina,cpfProfessor=""):
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

def remover(cpf,disciplina,cpfProfessor=""):
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

def atualizar(cpf,disciplina,cpfProfessor=""):
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

def encontrarPorDisciplina(cpf,disciplina,cpfProfessor=""):
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
            print(f"Disciplina: {x[1]}")
    if flag == True:
        arquivo = open("log.txt","a")
        tempo = time.asctime()
        arquivo.writelines(f"— O CPF {cpfProfessor} fez uma busca pela disciplina {disciplina} no cpf '{cpf}' na data e hora [{tempo}]\n")
        arquivo.close()
    elif flag == False:
        print("Aluno não encontrado!")
    return

def encontrarTodasDisciplina(cpf,cpfProfessor=""):
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

def ordenar(disciplina, cpfProfessor=""):
    lista = []
    flag = False
    for x in dicionario.keys():
        nome = dicionario[x][0]
        nota1 = dicionario[x][1]
        nota2 = dicionario[x][2]
        media = dicionario[x][3]
        dataCadastro = dicionario[x][4]
        lista.append([x[0],x[1],nome,nota1,nota2,media,dataCadastro])

    #Bublesort:
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

def relatorio(cpfProfessor=""):
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
    arquivo.writelines(f"— O CPF {cpfProfessor} fez um relatório na data e hora [{tempo}]\n")
    arquivo.close()
    return flag

def relatorioPlanilha(disciplina,cpfProfessor=""):
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

#CADASTRO E LOGIN:
"""
Todas as funções de cadastro e login.
"""
def cadastrarPessoas():
    cadastro = input("Você é professor[1] ou aluno[2]? [Digite a opção de acordo com o número]\n")
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
        
def login(cpf):
    flag = False
    senha = input("Senha: ")
    for x in usuarios.keys():
        if cpf == x and senha == usuarios[x][2]:
            flag = True
            print(f"Seja bem vindo {usuarios[x][1]}")
            nivelAcesso = usuarios[x][0]
    if flag == False:
        print("Usuário não encontrado!")
    elif flag == True:
        return nivelAcesso

def conferirDisciplina(cpf):
    flag = False
    for x in usuarios.keys():
        if cpf == x and usuarios[x][0] == "1":
            nomeDisciplina = usuarios[x][3]
    return nomeDisciplina

def alterarNivel(cpf,disciplina,cpfProfessor=""):
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
    elif flag == False:
        print("CPF de aluno não encontrado!")
    return

#ESCREVER TUDO NO ARQUIVO:
"""
Tudo que for feito no programa será escrito ou removido do arquivo.
"""
def tirarDoArquivoElementos():
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
                else:
                    arquivo.writelines(crip(w[cont])+"\n")
                cont+=1
            arquivo.writelines("\n")
    arquivo.close()
    
def escreverNoArquivoUsuarios():
    arquivo2 = open("usuarios.txt","w")
    #Tirando de usuarios e escrevendo no arquivo Usuarios.txt:
    for x,w in usuarios.items():
        if len(w) == 4:
            arquivo2.writelines(crip(x)+"\n"+crip(w[0])+"\n"+crip(w[1])+"\n"+crip(w[2])+"\n"+crip(w[3])+"\n\n")
        if len(w) == 3:
            arquivo2.writelines(crip(x)+"\n"+crip(w[0])+"\n"+crip(w[1])+"\n"+crip(w[2])+"\n\n")
    arquivo2.close()
    return
    
#MENU PRINCIPAL:
"""
Inicio do programa com todas as funções reunidas.
"""
#
"""
Aqui ele vai tentar colocar tudo que estiver no arquivo usuarios no dicionario de usuarios.
"""
salvarCadastro = False
try:
    tirarDoArquivoUsuarios()
    salvarCadastro = True
except:
    salvarCadastro = False


flag = True
entrar = False
while flag:
    op = input("[1] = Cadastrar \n[2] = Login \n[3] = Sair \n")
    if (op == "1" and salvarCadastro == True) or op == "1":
        cadastrarPessoas()
        escreverNoArquivoUsuarios()
    elif op == "2":
        cpfLogin = input("Digite seu CPF: ")
        acesso = login(cpfLogin)
        if acesso == "1" or acesso == "2":
            flag = False
            entrar = True
    elif op == "3":
        print("Até mais!")
        flag = False
    else:
        print("Opção digitada incorretamente!")

tirouDosArquivos = False
try:
    tirarDoArquivoElementos()
    tirouDosArquivos = True
except:
    tirouDosArquivos = False


while entrar:
    tempo = time.asctime()
    if acesso == "1":
        nomeDisciplina = conferirDisciplina(cpfLogin)
        opcao = input("[1] = Cadastrar \n[2] = Remover \n[3] = Atualizar \n[4] = buscar \n[5] = Alterar Nível de acesso \n[6] = Ordenar todos por nome \n[7] = Gerar Relatório ou planilha \n[8] = Encerrar \n")
        arquivo3 = open("log.txt","a")
        if opcao == "8":
            escreverNoArquivoElemento() #Ao sair, tudo que estiver nos dicionarios vão ser escritos no arquivo.
            arquivo3.writelines(f"— O CPF '{cpfLogin}' encerrou o programa na data e hora [{tempo}]\n")
            print("Até mais!")
            entrar = False
            arquivo3.close()
        else:
            if tirouDosArquivos == True or opcao == "1":
                if opcao == "1":
                    cpf = input("CPF: ")
                    cadastrar(cpf,nomeDisciplina,cpfLogin)
                    print("Aluno cadastrado com sucesso!")
                    escreverNoArquivoElemento()
                    tirouDosArquivos = True
                elif opcao == "2":
                    cpf = input("Digite o CPF do aluno que deseja remover: ")
                    remover(cpf,nomeDisciplina,cpfLogin)
                    escreverNoArquivoElemento()
                elif opcao == "3":
                    cpf = input("Digite o CPF para encontrarmos no Banco de Dados: ")
                    atualizar(cpf,nomeDisciplina)
                    escreverNoArquivoElemento()
                elif opcao == "4":
                    cpf = input("Digite o CPF que deseja encontrar: ")
                    encontrarPorDisciplina(cpf,nomeDisciplina,cpfLogin)
                elif (opcao == "5" and salvarCadastro == True) or opcao == "5":
                    cpf = input("Digite o CPF do aluno que deseja alterar o nível: ")
                    alterarNivel(cpf,nomeDisciplina,cpfLogin)
                    escreverNoArquivoUsuarios()
                elif opcao == "6":
                    if ordenar(nomeDisciplina) == False:
                        print("Não há nada para ordernar de acordo com a sua disciplina!")
                elif opcao == "7":
                    relatorioP = input("Digite o número da sua opção: \n[1] Relatório em arquivo \n[2] Planilha em csv \n")
                    if relatorioP == "1":
                        relatorio()
                        print("Relatório feito com sucesso!")
                    elif relatorioP == "2":
                        relatorioPlanilha(nomeDisciplina,cpfLogin)
                        print("Planilha feito com sucesso!")
                    else:
                        print("Opção digitada incorretamente.")
            else:
                print("ERROR: 2 erros podem ter acontecido: \n1 — Se você cadastrou algo, encerre o programa antes! \n2 — Não há nada no arquivo! Cadastre algo novo para poder manipular. :D")
    elif acesso == "2":
        opcao = input("[1] = Conferir as notas por disciplina! \n[2] = Conferir as notas de todas disciplinas! \n[3] = Encerrar \n")
        tirarDoArquivoElementos()
        if opcao == "1":
            cpfAluno = input("Digite seu CPF novamente: ")
            disciplina = input("Digite o nome da disciplina que deseja encontrar: ")
            encontrarPorDisciplina(cpfAluno,disciplina,cpfLogin)
        elif opcao == "2":
            cpfAluno = input("Digite seu CPF novamente: ")
            encontrarTodasDisciplina(cpfAluno,cpfLogin)
        elif opcao == "3":
            arquivo3 = open("log.txt","a")
            arquivo3.writelines(f"— O CPF '{cpfAluno}' encerrou o programa na data e hora [{tempo}]\n")
            print("Até mais!")
            entrar = False
            arquivo3.close()

                
        
