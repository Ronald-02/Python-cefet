def menu():
    print("Escolha uma das opções: ")
    print("1. Quadrado")
    print("2. Retângulo")
    print("3. Triângulo")
    print("4. Trapézio")
    print("5. Fim")
    opcao = int(input("Opção: "))
    while opcao < 1 or opcao > 5:
        opcao = int(input("Opção inválida. Tente novamente: "))
    return opcao

def quadrado():
    lado = float(input("lado do quadrado: "))
    return lado * lado

def retangulo():
    base = float(input("Base do retângulo: "))
    altura = float(input("Altura do retângulo: "))
    return base * altura

def triangulo():
    base = float(input("Base do triângulo: "))
    altura = float(input("Altura do triângulo: "))
    return (base * altura) / 2


def trapezio():
    base_maior = float(input("Base maior do trapézio: "))
    base_menor = float(input("Base menor do trapézio: "))
    altura = float(input("Altura do trapézio: "))
    return ((base_maior * base_menor) * altura) / 2

opcao = menu()
while opcao != 5:
    if opcao == 1:
        area = quadrado()
        print("Área do quadrado:", area)
    if opcao == 2:
        area = retangulo()
        print("Área do retângulo:", area)
    if opcao == 3:
        area = triangulo()
        print("Área do triângulo:", area)
    if opcao == 4:
        area = trapezio()
        print("Área do trapézio:", area)
    opcao = menu()

print("Fim")