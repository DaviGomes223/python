sexo = str(input('Informe seu sexo [M/F]:')) .strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Informe seu sexo corretamente: ')) .strip()
print('Sexo {} Registrado! '.format(sexo))
