def converte(horas, minutos):
    totmin = horas * 60 + minutos
    return totmin


def diferencial(hprev, mprev, hefet, mefet):
    totprev = converte(hprev, mprev)
    totefet = converte(hefet, mefet)
    totdifer = totefet - totprev
    return totdifer


# Exemplo de uso
hprev = 14  # 14 horas
mprev = 30  # 30 minutos
hefet = 16  # 16 horas
mefet = 15  # 15 minutos

diferenca = diferencial(hprev, mprev, hefet, mefet)
print(f"A diferença é de {diferenca} minutos.")
