from datetime import date

ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano 
idade2 = int
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, anoatual))
if idade < 18:
    idade2 = 18 - idade
    ano2 = anoatual + idade2
    print('Ainda faltam {} anos para seu alistamento militar'.format(idade2))
    print('Seu alistamento será em {}'.format(ano2))
elif idade > 18:
    idade2 = idade - 18
    ano2 = anoatual - idade2
    print('Voce deveria ter se alistado ha {} anos atras'.format(idade2))
    print('Seu alistamento deveria ter sido em {}'.format(ano2))
elif idade == 18:
    print('Vá se alistar imediatamente!!')