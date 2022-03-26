from random import randint

def escolheDeLista(nomeLista):
    return nomeLista[randint(0, len(nomeLista)-1)]

def abrirArquivos(genFem):
    if genFem == True:
        arq = open("nomes_femininos.txt", "r",encoding='utf-8')
    else:
        arq = open("nomes_masculinos.txt", "r",encoding='utf-8')
    arq_linha = arq.readline()
    arq_nomes = []
    while arq_linha:
        arq_linha = arq.readline()
        arq_nomes.append(arq_linha)
        nome = escolheDeLista(arq_nomes)
        nome = nome.strip("\n")
    arq.close()

    arqs = open("sobrenomes.txt", "r",encoding='utf-8')
    arqs_linha = arqs.readline()
    arqs_sobrenome = []
    while arqs_linha:
        arqs_linha = arqs.readline()
        arqs_sobrenome.append(arqs_linha)
        sobrenome = escolheDeLista(arqs_sobrenome)
        sobrenome = sobrenome.strip("\n")
    arqs.close()
    return (nome + " " + sobrenome) 

def nomes(genFem):
    #genFem = True
    if genFem == True:
        return abrirArquivos(genFem)
        #print(x)
    else: 
        return abrirArquivos(genFem)
        #print(y)       