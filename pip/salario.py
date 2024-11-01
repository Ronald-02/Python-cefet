def calcNovoSala(sala):
    perc = float(input("Digite percentual de aumento: "))
    bonus = float(input("Digite o valor do bônus: "))
    novo = sala + sala * perc / 100
    valor = novo + bonus
    print("Salário novo é", novo)
    print("Valor a ser recebido é", valor)
    return novo


# Exemplo de uso
sala_inicial = float(input("Digite o salário atual: "))
novo_salario = calcNovoSala(sala_inicial)
