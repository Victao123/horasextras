Horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_por_horatrabalhada = 15.00
if Horas_trabalhadas > 44:
    Horas_extras = Horas_trabalhadas - 44
    print(f"Você receberá R$ {Horas_extras * valor_por_horatrabalhada:.2f} de horas extras.")
else:
    print("Você não receberá horas extras. Você cumpriu a jornada corretamente.")
