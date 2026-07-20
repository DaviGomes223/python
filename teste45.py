from random import randint
from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

pc = randint(1, 3)
print('''SUAS OPÇÕES:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA ''')
opçao = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('_' * 50)

if pc == 1 and opçao == 2:
    print('\t\tComputador jogou PEDRA \n\t\tJogador jogou PAPEL ')
    print(Fore.GREEN + Style.BRIGHT + '\t\tJOGADOR VENCEU!! ')
elif pc == 2 and opçao == 1:
    print('\t\tComputador jogou PAPEL \n\t\tJogador jogou PEDRA ')
    print(Fore.RED + Style.BRIGHT + '\t\tCOMPUTADOR VENCEU!! ')
elif pc == 3 and opçao == 1:
    print('\t\tComputador jogou TESOURA \n\t\tJogador jogou PEDRA ')
    print(Fore.GREEN + Style.BRIGHT + '\t\tJOGADOR VENCEU!! ')
elif pc == 1 and opçao == 3:
    print('\t\tComputador jogou PEDRA \n\t\tJogador jogou TESOURA ')
    print(Fore.RED + Style.BRIGHT + '\t\tCOMPUTADOR VENCEU!! ')
elif pc == 2 and opçao == 3:
    print('\t\tComputador jogou PAPEL \n\t\tJogador jogou TESOURA ')
    print(Fore.GREEN + Style.BRIGHT + '\t\tJOGADOR VENCEU!! ')
elif pc == 3 and opçao == 2:
    print('\t\tComputador jogou TESOURA \n\t\tJogador jogou PAPEL')
    print(Fore.RED + Style.BRIGHT + '\t\tCOMPUTADOR VENCEU!! ')
elif pc == opçao:
    print(Fore.YELLOW + Style.BRIGHT + 'Os dois jogaram a mesma coisa, resultando em EMPATE!!!')
elif opçao >= 4:
    print(Fore.RED + Style.BRIGHT + 'NÃO EXISTE ESSA OPÇÃO, DIGITE O NÚMERO CORRETAMENTE!!!')
print('_' * 50)
