nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {} e {}, a media do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('O aluno esta REPROVADO!!')
elif media >= 5 and media <= 7:
    print('O aluno esta de RECUPERAÇÃO!!')
else:
    print('O aluno esta APROVADO!!')
