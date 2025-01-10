def leValidaQtd():
    qtd = int(input("Digite a quantidade de funcionários: "))
    while qtd <= 0:
        qtd = int (input(input("Digite um número maior que 0: ")))
    return qtd

def funcionarios(qtd):
    idosos = 0
    for i in range(qtd):
        idade = int(input("Digite a idade do funcionários: "))
    if idade >= 60:
        idosos += 1
    return idosos

qtd_funcionarios = leValidaQtd()
quantidade_idosos = funcionarios(qtd_funcionarios)
print("Quantidade de funcionários idosos: ", quantidade_idosos)