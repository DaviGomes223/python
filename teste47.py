from colorama import Fore, Style, init

init(autoreset=True)

for par in range(0, 51, 2):
    print(par, end=' ')
print(Fore.GREEN + Style.BRIGHT + '| CONTAGEM PAR! Acabou! ')
 

for impar in range(1, 51, 2):
    print(impar, end=' ')
print(Fore.RED + Style.BRIGHT + '| CONTAGEM IMPAR! Acabou! ')