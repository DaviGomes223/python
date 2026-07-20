salario = float(input('Digite seu salario: R$ '))
if salario > 1250:
    novo = salario + (salario * 10 / 100)
    print(f'O salario que valia R${salario :.0f} \nagora passa a valer R${novo :.0f}')
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print(f'O salario que valia R${salario :.0f} \nagora passa a valer R${novo :.0f}')
