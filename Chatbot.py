import telepot
import time

dicionario = {}
usuarios = {}
parametros = {"conta":"","senha":"","user":False,"password":False,"entrou":False}

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
    """
    Função recebe uma string e descriptogra, a sua descriptografia consiste em abrir o arquivo "chavePrivada.txt",
    depois pega os valores de "d" e "n" para podermos utilizar na formula da descriptofragia no terceiro for.
    """
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

#>>>>>>> Chatbot:
tirarDoArquivoElementos()
tirarDoArquivoUsuarios()

telegram = telepot.Bot("1019904371:AAF5C72fAiWTYwQ9nzSi2zEiQj7aJGd_DcU")
def recebendoMsg(msg):
    text = msg["text"]
    ID = msg["from"]["id"]
    nome = msg["from"]["first_name"]
    
    notas = dicionario
    if (text == "/start" in text) or (not parametros["user"] and not parametros["entrou"]):
        telegram.sendMessage(ID, f"Olá {nome} seja bem vindo ao nosso Sistemas de notas ❤ \n\nAqui será possível você verificar as notas de todas suas disciplinas.")
        telegram.sendMessage(ID, f"Para começarmos é preciso que você digite primeiramente o seu CPF(apenas números): ") 
        parametros["user"] = True
    elif parametros["user"] and not parametros["password"] and not parametros["entrou"]:
        parametros["conta"] = text
        telegram.sendMessage(ID, f"Digite sua senha:")
        parametros["password"] = True
    elif parametros["password"] and not parametros["entrou"]:
        parametros["senha"] = text
        parametros["password"] = False
        for x in usuarios.keys():
            if parametros["conta"] == x and parametros["senha"] == usuarios[x][2]:
                parametros["entrou"] = True
                telegram.sendMessage(ID,f"Estamos verificando suas informações...") 
                time.sleep(3)
                telegram.sendMessage(ID,f"Seja bem vindo {usuarios[x][1]}") 
                telegram.sendMessage(ID,f"Todas as suas notas de todas as disciplinas a seguir: ") 
        if not parametros["entrou"]:
            telegram.sendMessage(ID, "Usuário não encontrado! Tente novamente. Clique e recomeçe> /start")
            parametros["user"] = False
        if parametros["entrou"]:
            for x in dicionario.keys():
                if parametros["conta"] == x[0]:
                    telegram.sendMessage(ID,f"Disciplina: {x[1]} \nNota da 1º Unidade: {notas[x][1]} \nNota da 2º Unidade: {notas[x][2]} \nMedia: {notas[x][3]} \nData de Cadastro: {notas[x][4]}")                            
            telegram.sendMessage(ID, f"Até mais {nome}")

telegram.message_loop(recebendoMsg)
while True:
    pass
