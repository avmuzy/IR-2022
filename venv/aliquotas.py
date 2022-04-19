salário = float(input("Digite o salário mensal para cálculo do imposto: "))
base = salário
imposto = 0
if base < 2500:
    print('Isento')
elif base >= 2500 and base < 3200:
    print('Aliquota de 7,5%')
elif base >= 3200 and base < 4200:
    print('Aliquota de 15%')
elif base >= 4200 and base < 5300:
    print('Aliquota de 22,5%')
elif base >= 5300:
    print('Aliquota de 27,5%')
