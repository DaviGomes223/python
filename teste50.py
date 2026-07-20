from colorama import Fore, Style, init

init(autoreset=True)

soma = 0
cont = 0
for i in range(1, 7):
    num = int(input('Digite o {} valor: '.format(i)))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print(Fore.GREEN + Style.BRIGHT + 'Voce digitou {} valores PARES, e a soma é equivalente a {}'.format(cont, soma))
print(Fore.RED + Style.BRIGHT + 'Valores IMPARES são invalidados! ')