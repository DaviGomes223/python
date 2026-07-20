pr = float(input('Qual é o preço do produto? R$'))
des =  pr - (pr * 5 / 100)
print(f'O produto que custava R${pr}, com o desconto de 5% vai custar R${des :.2f}')