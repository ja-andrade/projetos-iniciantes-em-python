preco_produto = float(input("Qual o valor do produto?"))
if preco_produto >= 100:
    desconto = float(input("Qual o valor do desconto?(Obs: apenas numeros)"))
    if 0 <= desconto <= 100:
        valor_final = preco_produto - ((preco_produto * desconto) / 100)
        print(f"O valor final com {desconto:.2f}% de desconto é de R${valor_final:.2f}")
    else:
        print("O valor do desconto não é compativel. Tente novamente.")
else:
    print(f"O valor do produto é de: {preco_produto:.2f}")
    print(f"O valor digitado não entra no minimo para desconto. Adicione mais R${100 - preco_produto:.2f} para adiciniar um cupom.")