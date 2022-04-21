salário = float(input("Digite o salário para cálculo do imposto: "))
base = salário *12
print("Rendimento anual:",base)
imposto = 0
if base < 30000:
    print('Isento')

elif 30000 <= base < 38400:
    print('Aliquota de 7,5%')
    print("Imposto devido:", ((base*7.5)/100))

elif 38400 <= base < 50400:
    print('Aliquota de 15%')


elif 50400 <= base < 63600:
    print('Aliquota de 22,5%')
else:
    print('Aliquota de 27,5%')