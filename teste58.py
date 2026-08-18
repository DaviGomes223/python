from random import randint
from colorama import Style, Fore, init

init(autoreset=True)

num = randint(0, 10)
print('''Sou seu computador...
Pensei em um número de 0 a 10, será que voce consegue adivinhar? ''')
acertou = False
palpites = 1
while not acertou:
    num1 = int(input('Em que número pensei? '))
    if num1 != num:
        print(Fore.RED + Style.BRIGHT + 'Voce errou! Tente novamente na linha abaixo: ')
        palpites += 1
    if num1 == num:
        acertou = True
        print(Fore.GREEN + Style.BRIGHT + 'Voce acertou!! Parabens!!')
        print(Fore.YELLOW + Style.BRIGHT + 'Voce precisou de {} palpites para acertar o número escolhido pelo seu computador!!'.format(palpites))
    else:
        if num1 > num:
            print(Fore.RED + Style.BRIGHT + 'Menos...')
        if num1 < num:
            print(Fore.RED + Style.BRIGHT + 'Mais...')
