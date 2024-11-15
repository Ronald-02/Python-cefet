import math

x1 = float(input("Digite a coordenada x do ponto A: "))
x2 = float(input("Digite a coordenada x do ponto A: "))
y1 = float(input("Digite a coordenada x do ponto B: "))
y2 = float(input("Digite a coordenada x do ponto B: "))
x3 = float(input("Digite a coordenada x do ponto C: "))
y3 = float(input("Digite a coordenada x do ponto C: "))

lado_ab = math.sqrt((x2 - x1)**2 + (y2 - y1) **2)
lado_bc = math.sqrt((x3 - x2)**2 + (y3 - y2) **2)
lado_ca = math.sqrt((x3 - x1)**2 + (y3 - y1) **2)

perimetro = lado_ab + lado_bc + lado_ca

print("O perímetro do triângulo é: ", round(perimetro, 2))