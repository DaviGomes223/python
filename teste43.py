from colorama import Fore, Style, init
init(autoreset=True)
peso = float(input('Qual é o seu peso em KG? '))
altura = float(input('Qual é a sua altura em M? '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))
print(Fore.MAGENTA + Style.BRIGHT + 'CLASSIFICAÇÃO:', end=' ')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')
    print(Fore.RED + Style.BRIGHT + 'BUSQUE UM MÉDICO IMEDIATAMENTE!!!')
