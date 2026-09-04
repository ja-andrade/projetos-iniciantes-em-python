nota1 = float(input("Qual a primeira nota?"))
nota2 = float(input("Qual a segunda nota?"))
media = (nota1 + nota2) / 2
if nota1 > 10 or nota2 > 10:
    print("Alguma das notas está acima do limite total de pontos possivel na prova.")
else:
    print(f"Sua nota media é de:{media:.2f}")
    if media >= 7:
        print("Parabéns, vocé está aprovado!!!")
    else:
        print("infelizmente vocé não foi aprovado.")