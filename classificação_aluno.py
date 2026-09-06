nome_aluno = input("Qual o nome do aluno?")
total_de_presenca = int(input("Quantos dias de presença o aluno teve?(Obs: de 0 a 100)"))
if 75 <= total_de_presenca <= 100:
    nota1 = float(input("Qual a primeira nota do aluno?"))
    nota2 = float(input("Qual a segunda nota do aluno"))
    if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
        print("Algum valor das notas está fora de 0 a 10.")
    else:
        media_notas = (nota1 + nota2) / 2
        if 7 <= media_notas <= 10:
            print(f"Parabéns {nome_aluno} sua media é de {media_notas:.2f}, você foi APROVADO!!!!")
        elif 5 <= media_notas < 7:
            print(f"Aluno {nome_aluno} sua media é de {media_notas:.2f}, sua nota não foi suficiente para passar. Tera que fazer RECUPERAÇÃO!!!")
        else:
            print(f"Aluno {nome_aluno} sua media foi de {media_notas:.2f} está, infelizmente, REPROVADO!!!.")
elif 0 <= total_de_presenca < 75:
    print(f"Aluno {nome_aluno} REPROVADO por falta!! Tente novamente no próximo ano.")
else:
    print("A quantidade de presença digitada não é compativel")
