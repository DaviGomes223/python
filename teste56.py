c = 0
somaidade = 0
mediaidade = 0
Idadevelho = 0
nomevelho = ''
mulheres = 0
for p in range (1, 5):
    c += 1
    print('====== {} PESSOA ======'.format(c))
    nome = str(input('Nome da pessoa: '))
    Idade = int(input('Idade da pessoa: '))
    genero = str(input('[M/F]: '))
    somaidade += Idade
    if p == 1 and genero in 'Mm':
        nomevelho = nome
        Idadevelho = Idade
    if genero in 'Mm' and Idade > Idadevelho:
        Idadevelho = Idade
        nomevelho = nome
    if Idade <= 20 and genero in 'Ff':
        mulheres += 1
mediaidade = somaidade / 4
print('A média de idade equivale a {}'.format(mediaidade))
print('O homem mais velho é o {} com {} anos'.format(nomevelho, Idadevelho))
print('Há {} mulheres com menos de 20 anos'.format(mulheres))
