import math

lado_a = float (input("digite o comprimento do primeiro lado (cateto): "))
lado_b = float (input("digite o comprimento do segundo lado (cateto): "))

hipotenusa = math.sqrt(lado_a ** 2 + lado_b ** 2)

print(f"A hipotenusa do triângulo retângulo é: {hipotenusa:.2f}")