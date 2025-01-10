def verifica(matricula):
    if matricula.isdigit() and matricula[4:5]:
        ano = int(matricula[0:2])
        semestre = int(matricula[2])
        sequencial = int(matricula[3:])

        if 20 <= ano <= 24 and (semestre == 1 or semestre == 2) and 1 <= sequencial <= 90:
            print("Válida")
        else:
            print("Inválida")
    else:
        print("Inválida")

for i in range(0,4):
    matricula = input("Digite a matrícula:")
    verifica(matricula)