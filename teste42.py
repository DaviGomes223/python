from colorama import Fore, init
init(autoreset=True)
seg1 = float(input('PRIMEIRO SEGMENTO: '))
seg2 = float(input('SEGUNDO SEGMENTO: '))
seg3 = float(input('TERCEIRO SEGMENTO: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('OS SEGMENTOS FORMAM UM TRIANGULO', end=' ')
    if seg1 == seg2 == seg3:
        print(Fore.GREEN + 'EQUILATERO!')
    if seg1 != seg2 != seg3 != seg1:
        print(Fore.BLUE + 'ESCALENO!')
    if seg1 == seg2 != seg3 or seg2 == seg3 != seg1 or seg3 == seg1 != seg2:
        print(Fore.YELLOW + 'ISOSCELES!')
else:
    print('OS SEGMENTOS NÃO FORMAM UM TRIANGULO!')