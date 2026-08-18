from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('=' * 30)
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa ''')
    print('=' * 30)
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma de {} + {} resulta em {}'.format(num1, num2, soma))
    elif opcao == 2:
        multiplicacao = num1 * num2
        print('A multiplicação de {} x {} resulta em {}'.format(num1, num2, multiplicacao))
    elif opcao == 3:
        print('O maior número entre {} e {} é {}'.format(num1, num2, max(num1, num2)))
    elif opcao == 4:
        num1 = int(input('Novo primeiro valor: '))
        num2 = int(input('Novo segundo valor: '))    
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
        print('-' * 40)
        print('Seu programa foi finalizado com sucesso.')
    else:
        print(Fore.RED + Style.BRIGHT + 'Opçãõ Inválida. Tente Novamente: ')
