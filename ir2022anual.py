salario = float(input("Digite o salário para cálculo do imposto: "))

base = salario * 12
print("Rendimento anual:", base)
imposto = 0

dependentes = int(input(" digite o numero de dependentes: "))
geral_dependente = (dependentes * 2275.08)
educacao = (dependentes * 3561.50)
print("Valor para dedução com dependentes:", (geral_dependente+educacao))


if base < 30000:
    print('Isento')

elif 30000 <= base < 38400:
    print('Aliquota de 7,5%')
    print("Imposto devido:", ((base*7.5)/100))

elif 38400 <= base < 50400:
    print('Aliquota de 15%')
    print("Imposto devido:", ((base*15)/100))

elif 50400 <= base < 63600:
    print('Aliquota de 22,5%')
    print("imposto devido:", ((base*22.5)/100))
else:
    print('Aliquota de 27,5%')
    print("Imposto devido:", ((base*27.5)/100))
