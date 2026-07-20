from colorama import Fore, Back, Style, init

init(autoreset=True)
init(autoreset=True)

# CODIGOS COPIADOS DO CLAUDE CODE PARA TESTES E CONSULTA

# Cores principais
print(Fore.BLACK + "Texto preto")
print(Fore.RED + "Texto vermelho")
print(Fore.GREEN + "Texto verde")
print(Fore.YELLOW + "Texto amarelo")
print(Fore.BLUE + "Texto azul")
print(Fore.MAGENTA + "Texto magenta")
print(Fore.CYAN + "Texto ciano")
print(Fore.WHITE + "Texto branco")

print(Fore.WHITE + "Davi Gomes")

print(Back.GREEN + "Davi gomes")

# Título
print(Fore.GREEN + Style.BRIGHT + "=== Meu Programa ===\n")

# Mensagens com cores
print(Fore.YELLOW + "⚠️  Aviso: processando...")
print(Fore.GREEN + "✓ Sucesso: operação concluída")
print(Fore.RED + "✗ Erro: algo deu errado")

# Com fundo
print(Back.BLUE + Fore.WHITE + "Informação importante")

# Tabela colorida
print(Fore.CYAN + "Nome" + "\t" + "Status")
print(Fore.YELLOW + "Item 1" + "\t" + Fore.GREEN + "OK")

# TESTES COM O COLORAMA

print(Fore.BLACK + Back.RED + Style.DIM + "DAVI GOMES" "\t" + Fore.GREEN + "MACENA DA ROCHA")


# Fonte
print(Style.BRIGHT + "JOAO")

# Cor
print(Fore.GREEN + "JOAO")

# Cor de Fundo
print(Back.GREEN + "JOAO")