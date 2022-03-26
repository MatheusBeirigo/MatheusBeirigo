from random import randint

def escolheDeLista(nomeLista):
    return nomeLista[randint(0, len(nomeLista)-1)]

arq = open("nomes_femininos.txt", "r")
arq_linha = arq.readline()
arq_nomes = []
while arq_linha:
    #print(arq_linha)
    arq_linha = arq.readline()
    arq_nomes.append(arq_linha)
    nome = escolheDeLista(arq_nomes)
arq.close()
print(nome)