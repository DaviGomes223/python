from datetime import date
nascimento = int(input('Ano de Nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento
if idade <= 9:
    print('Voce tem {} anos.\nSua categoria é MIRIM!'.format(idade))
elif idade <= 14:
    print('Voce tem {} anos.\nSua categoria é INFANTIL!'.format(idade))
elif idade <= 19:
    print('Voce tem {} anos.\nSua categoria é JÚNIOR!'.format(idade))
elif idade <= 25:
    print('Voce tem {} anos.\nSua categoria é SÊNIOR!'.format(idade))
elif idade > 26:
    print('Voce tem {} anos.\nSua categoria é MASTER!'.format(idade))
