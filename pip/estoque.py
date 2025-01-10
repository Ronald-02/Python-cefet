def contar_estoque_zerado(quantidade_modelos):
    estoque_zerado = 0

    for _ in range(quantidade_modelos):
        input("Digite o código do modelo: ")
        if int(input("Digite a quantidade em estoque: ")) == 0:
            estoque_zerado += 1

    return estoque_zerado

quantidade_modelos = int (input("Digite a quantidade de modelos de automóveis produzidos pela fábrica: "))
print("A quantidade de modelos com estoque zerado é:", contar_estoque_zerado(quantidade_modelos))