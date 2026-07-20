largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
ar = largura * altura
t = ar / 2
print(f'Sua parede tem a dimensao de {largura}x{altura} e sua area é de {ar}m².')
print(f'Para pintar essa parede, voce precisará de {t}l de tinta.')
