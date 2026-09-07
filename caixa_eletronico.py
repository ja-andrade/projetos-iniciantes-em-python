saque_inicial = float(input("Quanto você quer sacar?"))
saque = saque_inicial
notas_de_100 = 0
notas_de_50 = 0
notas_de_10 = 0
if 0 < saque_inicial <= 1000:
    if saque >= 100:
        notas_de_100 = int(saque // 100)
        saque = saque % 100
    if saque >= 50:
        notas_de_50 = int(saque // 50)
        saque = saque % 50
    if saque >= 10:
        notas_de_10 = int(saque // 10)
        saque = saque % 10
    if 0 < saque < 10:
        print(f"o valor não pode ser efetuado porque R${saque:.2f} não pode ser sacado."
              f"\n adicione no minimo mais R${10 - saque:.2f} no valor final do saque")
    else:
        print(f"O valor de R${saque_inicial:.2f} sera feito em notas de:"
              f"\n{notas_de_100} nota(s) de R$100,00."
              f"\n{notas_de_50} nota(s) de R$50,00."
              f"\n{notas_de_10} notas(s) de R$10,00.")
elif saque_inicial > 1000:
    print("o valor exede o valor de saque permitido, até R$1000,00.")
else:
    print("O valor digitado não pode ser sacado. É um numero negativo.")