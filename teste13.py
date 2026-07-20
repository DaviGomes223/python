pr = float(input('Digite o salario do funcionario: R$ '))
va = int(input('Digite o porcentual a ser aumentado: '))
des = pr + (pr * va / 100)
print(f'Um funcionario que ganhava R${pr}, com {va}% de aumento , passa a receber R${des :.2f} ')
