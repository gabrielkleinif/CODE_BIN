print("Conversor de Decimal para Binário")

# solicita o número decimal a ser convertido
decimal = int(input("Digite um número decimal: "))

# inicializa a variável para armazenar o número binário
binario = ""

# converte o número decimal em binário usando o método de divisões sucessivas
while decimal > 0:
    resto = decimal % 2
    binario = str(resto) + binario
    decimal //= 2

# exibe o resultado
print("O número decimal", decimal, "em binário é", binario)
