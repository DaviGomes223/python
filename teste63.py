print('-' * 20)
print('SEQUENCIA DE FIBONACCI')
print('-' * 20)
n = int(input('Digite um número total de sequencias: '))
termo1 = 0
termo2 = 1
c = 3
print('{} - {} '.format(termo1, termo2), end='')
while c <= n:
    termo3 = termo1 + termo2
    print('- {} '.format(termo3), end='')
    c += 1
    termo1 = termo2
    termo2 = termo3
print('\n\t\tFinalizando...')
print('\t\t    FIM', end='')




anterior = 0
proxima = 1
contador = 3
n2 = int(input('\n\nQuantos termos voce quer ver? '))
print('{} - {} '.format(anterior, proxima), end='')
while contador <= n2:
    soma = anterior + proxima
    print('- {} '.format(soma), end='')
    contador += 1
    anterior = proxima
    proxima = soma
print('FIM')

