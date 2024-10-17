matricula_aluno = str(input("digite a matrícula do aluno: "))
nota1 = float(input("digite a primeira nota do aluno: "))
nota2 = float(input("digite a segunda nota do aluno: "))
media = (nota1+nota2) / 2
media_truncada = int(media) #media truncada ignora a parte decimal
print("o aluno da matrícula", matricula_aluno, "teve média truncada de", media_truncada)