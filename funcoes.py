# POSIÇÕES
def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_posicao = []

        
    for i in range(tamanho):
        if orientacao=='vertical':
            lista_posicao.append([linha, coluna])
            linha+=1
        elif orientacao=='horizontal':
            lista_posicao.append([linha, coluna])
            coluna+=1
    return lista_posicao
# FROTA COM POSIÇÕES

def preenche_frota(frota, nome_do_navio, linha, coluna, orientacao, tamanho):
    lista_posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if len (frota) != 0:
        if nome_do_navio in frota:
            valor_i = frota[nome_do_navio]
            valor_i.append(lista_posicao)
            frota[nome_do_navio] = valor_i
        else: 
            lista_final = []
            lista_final.append(lista_posicao)
            frota[nome_do_navio]= lista_final
    else:
        lista_final = []
        lista_final.append(lista_posicao)
        frota[nome_do_navio]= lista_final
    return frota
# FAZ JOGADA
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'  
    return tabuleiro

                
