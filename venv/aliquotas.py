salário = float(input("Digite o salário mensal para cálculo do imposto: "))
base = salário
imposto = 0
if base < 2500:
    print('Isento')