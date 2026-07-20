frase = str(input('Digite uma frase:')).strip() .upper()
lista = frase.split()
junto = ''.join(lista)
inverso = junto[::-1]
print('A frase {} invertida é {}'.format(junto, inverso))
if inverso == junto:
    print('ESSA FRASE É UM PALINDROMO!')
else:
    print('ESSA FRASE NÃO É UM PALINDROMO!')
