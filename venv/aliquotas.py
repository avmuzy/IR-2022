salário = float(input("Digite o salário mensal para cálculo do imposto: "))
base = salário
imposto = 0
if base < 2500:
    print('Isento')
elif base >= 2500 < 3200:
    print('Aliquota de 7,5%')
elif base >= 3200 < 4200:
    print('Aliquota de 15%')