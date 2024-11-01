qtd_alunos = int (input("digite a quantidade de alunos na turma: "))
qtd_reprovados = int(input("digite a quantidade de alunos reprovados: "))

percentual_reprovados = (qtd_reprovados / qtd_alunos * 100) if qtd_alunos >= 0 else 0
percentual_aprovados = 100 - percentual_reprovados

print(f"percentual_aprovados: {percentual_aprovados:.2f}%")
print(f"percentual_reprovados: {percentual_reprovados:.2f}%")