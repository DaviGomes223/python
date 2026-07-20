from colorama import Fore, Style, init

init(autoreset=True)
valor = float(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opçao = int(input('Sua opção: '))
if opçao == 1:
    total = valor - (valor * 10 / 100)
elif opçao == 2:
    total = valor - (valor * 5 / 100)
elif opçao == 3:
    total = valor
    parcela = total / 2
    print( Fore.YELLOW + Style.BRIGHT + 'Sua compra foi parcelada em 2x de {} SEM JUROS!'.format(parcela))
elif opçao == 4:
    total = valor + (valor * 20 / 100)
    totalparc = int(input('Quantas vezes parceladas? '))
    parcela = total / totalparc
    print( Fore.YELLOW + Style.BRIGHT + 'Sua compra foi parcelada em {}x de {:.2f} com 20% de juros!'.format(totalparc, parcela))
elif opçao >= 5:
    total = 0
    print(Style.BRIGHT + Fore.RED + 'Essa opção não existe, tente novamente escolhendo um número que prossiga o pagamento!! :( ')
print(Style.BRIGHT + Fore.GREEN + 'Sua compra de R${:.2f} terá o custo final de R${:.2f}!'.format(valor, total))
