from colorama import Fore, Style, init
init(autoreset=True)
casa = int(input('O valor da casa: R$'))
salario = int(input('Seu salario: R$'))
f = int(input('Quantos anos de Financiamento: '))
prestacao = casa / (f * 12)
minimo = salario * 30 / 100
print('Para uma casa de R${} e o tempo de financiamento de {} anos'.format(casa, f))
print('O valor da prestação mensal sera de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('O acesso foi', Fore.GREEN + Style.BRIGHT + 'CONCEDIDO!!')
else:
    print('O valor excedeu e o acesso foi', Fore.RED + Style.BRIGHT + 'NEGADO!!')