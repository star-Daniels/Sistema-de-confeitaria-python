
def merge_sort(vendas):

    if len(vendas) <= 1:
        return vendas

    meio = len(vendas) // 2

    esquerda = merge_sort(vendas[:meio])
    direita = merge_sort(vendas[meio:])

    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):

        if esquerda[i].total_venda >= direita[j].total_venda:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado
