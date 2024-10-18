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