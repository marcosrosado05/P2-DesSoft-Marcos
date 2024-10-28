# POSIÇÕES

def define_posicoes(linha,coluna,orientacao,tamanho): # Guarda as informações relativas à posição do navio 
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

def preenche_frota(frota:dict, nome_do_navio:str, linha, coluna, orientacao, tamanho):
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

# POSICIONA FROTA

def posiciona_frota(posicoes_navio):
    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
  
    for navios in posicoes_navio.values():
        for x in range(len(navios)):
            for y in range(len(navios[x])):
                x_coord = navios[x][y][0]
                y_coord = navios[x][y][1]
                tabuleiro[x_coord][y_coord] = 1
    return tabuleiro

# AFUNDADOS

def afundados(frota,tabuleiro):
    qnt_afundados = 0 
    for posicao_afundados in frota.values():
        for x in posicao_afundados:
            qnt_tiros = 0 
            for y in x:
                if tabuleiro[y[0]][y[1]] == "X":
                    qnt_tiros += 1
                if qnt_tiros == (len(x)):
                    qnt_afundados += 1 
    return qnt_afundados          
  
# POSIÇÃO VALIDA   
def posicao_valida(nome_do_navio, linha, coluna,orientacao,tamanho):
    atualizada = define_posicoes(linha,coluna,orientacao,tamanho)
    posicao_proibida = 0

    for lista_coordenadas in nome_do_navio.values():
        for coordenada in lista_coordenadas:
            for comparacao in atualizada:
                if comparacao == coordenada: 
                    posicao_proibida += 1 
            
    if posicao_proibida == 0:
        return True
    else:
        return False
# PERGUNTA POSICIONAMENTO DA FROTA

