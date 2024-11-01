def parImpar(num):
    resto = num % 2
    if resto == 0:
        print("Par")
    else:
        print("Ímpar")


numero = int(input("Digite um número inteiro: "))
parImpar(numero)
