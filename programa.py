from funcoes import *
from random import randint as sorteia 

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
} 
nome_do_navio = {
    "porta-aviões":[4,1], #tamanho, quantidade
    "navio-tanque":[3,2],
    "contratorpedeiro":[2,3],
    "submarino": [1,4],
}  
for navios, tamanho in nome_do_navio.items():
    cont = 0 
    while cont < tamanho[1]:
        print(f'Insira as informações referentes ao navio {navios} que possui tamanho {tamanho[0]}') 
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if navios != "submarino":
            orientacao = int(input("[1] Vertical [2] Horizontal "))
            if orientacao == 1:
                orientacao = "vertical"
            elif orientacao == 2:
                orientacao = "horizontal"
            
        atualizado = posicao_valida(frota, linha, coluna ,orientacao,tamanho[0])
        if atualizado == False:
            print("Esta posição não está válida!")
            print(f'Insira as informações referentes ao navio {navios} que possui tamanho {tamanho[0]}') 

        while atualizado == False:
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            if navios != "submarino":
                orientacao = int(input("[1] Vertical [2] Horizontal "))
                if orientacao == 1:
                    orientacao = "vertical"
                elif orientacao == 2:
                    orientacao = "horizontal"
            atualizado = posicao_valida(frota, linha, coluna ,orientacao,tamanho[0])
            if atualizado == False:
                print("Esta posição não está válida!")
                print(f'Insira as informações referentes ao navio {navios} que possui tamanho {tamanho[0]}') 
        posicao_selec = define_posicoes(linha,coluna,orientacao,tamanho[0])
        preencher = preenche_frota(frota,navios, linha, coluna, orientacao, tamanho[0])
        cont += 1
print(frota)



