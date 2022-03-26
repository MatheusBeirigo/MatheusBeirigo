import nomes 
import acoes
import locais
import random
import desfecho_viloes
import desfecho_protagonista

def nome(x, y):
        list = []
        for i in range(x):
            nome = nomes.nomes(y)
            list.append(nome)
        return list

def primeiro_nome(nome):
    nome = nome.split()
    nome = nome[0]
    return nome

def selectRandom(nomes):
        return random.choices(nomes)

def tratandoListas(lista):
        listaTratada = "".join(lista)
        return listaTratada

def main():
    prot = int(input("Quantos serão os protagonistas? (Apenas números pares): "))
    if prot%2!=0:
        print("O número de protagonistas não é válido!")
        exit()
    vil = int(input("Quantos serão os vilões? (Apenas números pares): "))
    if vil%2!=0:
        print("O número de vilões não é válido!")
        exit()
    coad = int(input("Quantos serão os personagens coadjuvantes? (Apenas números pares): "))
    if coad%2!=0:
        print("O número de personagens coadjuvantes não é válido!")
        exit()
    #print(prot,vil,coad)
#-------------------------------------------------------------------------------------------------------
    n_prot = int(prot/2)
    n_vil = int(vil/2)
    n_coad = int(coad/2)
#-------------------------------NOME DOS PERSONAGENS--------------------------------------------------- 
    prot_fem = nome(n_prot, True)
    prot_masc = nome(n_prot, False)
    vil_fem = nome(n_vil, True)
    vil_masc = nome(n_vil, False)
    coad_fem = nome(n_coad, True)
    coad_masc = nome(n_coad, False)
#------------------------------------------------------------------------------------------------------ 
    protagonistas = prot_fem + prot_masc
    viloes = vil_fem + vil_masc
    coadjuvantes = coad_fem + coad_masc
#-------------------------------NOME DA NOVELA----------------------------------------------------------
    novela = str(input("Qual será o nome da novela? "))
    novela = novela.upper()
#-------------------------------NÚMERO DE EPISÓDIOS-----------------------------------------------------
    episodios = int(input("Quantos episódios terá a novela? "))
    print("")
#-------------------------------IMPRESSÕES INICIAIS-----------------------------------------------------
    print(f"***{novela}***")
#---------------------CRIANDO ARQUIVO DE TEXTO---------------------------    
    arq = open(f"Resenha_de_{novela}.txt","x",encoding='utf-8')
    arq.close()
    txt = open(f"Resenha_de_{novela}.txt","a",encoding='utf-8')
    txt.write(f"***{novela}***\n")
#------------------------------------------------------------------------    
    print("")
    txt.write("\n")
    print("Protagonistas")
    txt.write("Protagonistas\n")
    print("=============")
    txt.write("=============\n")
    for i in range(n_prot):
        print(prot_fem[i])
        txt.write(f"{prot_fem[i]}\n")
    for i in range(n_prot):
        print(prot_masc[i])
        txt.write(f"{prot_masc[i]}\n")
    print("")
    txt.write("\n")
    print("Vilões")
    txt.write("Vilões\n")
    print("=============")
    txt.write("=============\n")
    for i in range(n_vil):
        print(vil_fem[i])
        txt.write(f"{vil_fem[i]}\n")
    for i in range(n_vil):
        print(vil_masc[i])
        txt.write(f"{vil_masc[i]}\n")
    print("")
    txt.write("\n")
    print("Personagens coadjuvantes")
    txt.write("Personagens coadjuvantes\n")
    print("=============")
    txt.write("=============\n")
    for i in range(n_coad):
        print(coad_fem[i])
        txt.write(f"{coad_fem[i]}\n")
    for i in range(n_coad):
        print(coad_masc[i])
        txt.write(f"{coad_masc[i]}\n")
    print("")
    txt.write("\n")
#-------------------------------PRIMEIRO NOME----------------------------------------------------------
#Tem a função lá, tô com preguiça de fazer um por um
#-------------------------------EPISODIOS-------------------------------------------------------------
    
    for i in range(episodios):
#protagonista > ação > coadjuvante > local
#vilão > ação > protagonista > local
#protagonista > ação > vilão > local
        txt.write("\n")
        print(f"Episódio {i+1}")
        txt.write(f"Episódio {i+1}\n")
        print("==================")
        txt.write("==================\n")
        for i in range(len(protagonistas)):
            print(f"{tratandoListas(protagonistas[i])} {acoes.abrirArquivos()} {tratandoListas(coadjuvantes[i])} {locais.abrirArquivos()}")
            
            txt.write(f"{tratandoListas(protagonistas[i])} {acoes.abrirArquivos()} {tratandoListas(coadjuvantes[i])} {locais.abrirArquivos()}\n")
        
        for i in range(len(viloes)):
            print(f"{tratandoListas(viloes[i])} {acoes.abrirArquivos()} {tratandoListas(protagonistas[i])} {locais.abrirArquivos()}")
            
            txt.write(f"{tratandoListas(viloes[i])} {acoes.abrirArquivos()} {tratandoListas(protagonistas[i])} {locais.abrirArquivos()}\n")
        
        for i in range(len(coadjuvantes)):
            print(f"{tratandoListas(coadjuvantes[i])} {acoes.abrirArquivos()} {tratandoListas(viloes[i])} {locais.abrirArquivos()}")
            
            txt.write(f"{tratandoListas(coadjuvantes[i])} {acoes.abrirArquivos()} {tratandoListas(viloes[i])} {locais.abrirArquivos()}\n")
        print("")
        txt.write("\n")

#-------------------------------EPISODIO FINAL----------------------------------------------------------
    print("")
    txt.write("\n")
    print("EPISÓDIO FINAL")
    txt.write("EPISÓDIO FINAL\n")
    print("==================")
    txt.write("==================\n")
#para cada vilão > desfecho
    for i in range(len(viloes)):
        x =(f"{tratandoListas(viloes[i])} {desfecho_viloes.abrirArquivos()}")
        if "#" in x:
            x = x.replace("#",tratandoListas(selectRandom(protagonistas)))
            print(x)
            txt.write(f"{x}\n")
        else:
            print(x)
            txt.write(f"{x}\n")
#para cada protagonista > desfecho
    for i in range(len(protagonistas)):
        y = (f"{tratandoListas(protagonistas[i])} {desfecho_protagonista.abrirArquivos()}")
        if "#" in y:
            y = y.replace("#", tratandoListas(selectRandom(viloes)))
            print(y)
            txt.write(f"{y}\n")
        else:
            print(y)
            txt.write(f"{y}\n")
    print("")
    txt.write("\n")
#-------------------------------------------------------------------------------------------------------
    print("===")
    txt.write("===\n")
    print(f"Arquivo <Resenha_de_{novela}.txt> salvo com sucesso")
    txt.write(f"Arquivo <Resenha_de_{novela}.txt> salvo com sucesso\n")
    txt.close()
    return
main()