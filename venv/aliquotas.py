salário = float(input("Digite o salário mensal para cálculo do imposto: "))
base = salário
imposto = 0
if base < 2500:
    print('Isento')
elif 2500 <= base < 3200:
    print('Aliquota de 7,5%')
elif 3200 <= base < 4200:
    print('Aliquota de 15%')
elif 4200 <= base < 5300:
    print('Aliquota de 22,5%')
else:
    print('Aliquota de 27,5%')
