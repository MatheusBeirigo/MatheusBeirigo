from random import randint

def escolheDeLista(nomeLista):
    return nomeLista[randint(0, len(nomeLista)-1)]

def abrirArquivos():
    arq = open("finais_viloes.txt","r",encoding='utf-8')
    arq_linha = arq.readline()
    arq_nomes = []
    while arq_linha:
        arq_linha = arq.readline()
        arq_nomes.append(arq_linha)
        nome = escolheDeLista(arq_nomes)
        nome = nome.strip("\n")
    arq.close()
    return nome
