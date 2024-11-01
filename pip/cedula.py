def umaCedula(montante, cedula):
    qtd = montante // cedula
    resto = montante % cedula
    print(qtd, "cédulas de", cedula)
    return resto


def cedulas(valor):
    print("Quantidade de notas para o valor", valor, "é:")
    valor = umaCedula(valor, 200)
    valor = umaCedula(valor, 100)
    valor = umaCedula(valor, 50)
    valor = umaCedula(valor, 20)
    valor = umaCedula(valor, 10)
    valor = umaCedula(valor, 5)
    valor = umaCedula(valor, 2)
    valor = umaCedula(valor, 1)


# Exemplo de uso
valor_inicial = int(input("Digite o valor a ser sacado: "))
cedulas(valor_inicial)
