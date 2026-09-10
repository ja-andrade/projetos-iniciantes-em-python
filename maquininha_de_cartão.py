valor_compra = float(input("Qual o valor da compra?"))
if valor_compra > 0:
    escolha = int(input("Qual o tipo de tarnsaçâo?"
                    "\n1- Débito "
                    "\n2- Crédito à vista"
                    "\n3- Crèdito parcelado\n"))
    if escolha > 3 or escolha <= 0:
        print(f"Numero {escolha} não esta entre as opcões. ")
    else:
        match escolha:
            case 1:
                valor_taxa = valor_compra * 0.015
                print(f"TRANSÇÃO: Débito"
                      f"\nVALOR DA TAXA: R${valor_taxa:.2f}"
                      f"\nVENDEDOR RECEBE: R${valor_compra - valor_taxa:.2f}")
            case 2:
                valor_taxa = valor_compra * 0.03
                print(f"TRANSAÇÃO: Crédito à vista"
                      f"\nVALOR DA TAXA: R${valor_taxa:.2f}"
                      f"\nVENDEDOR RECEBE: R${valor_compra - valor_taxa:.2f}")
            case 3:
                numero_parcelas = int(input("Em quantas vezes você quer parcelar?(2x a 6x)"))
                if numero_parcelas > 6 or numero_parcelas <= 1:
                    print("Numero de parcelas não disponivel!!")
                else:
                    valor_taxa = (((numero_parcelas / 100) + 0.05) * valor_compra)
                    print(f"TRANSÇÃO: Crédito parcelado"
                          f"\nNUMERO DE PARCELAS: {numero_parcelas}x de R${valor_compra / numero_parcelas:.2f}"
                          f"\nVALOR DA TAXA: R${valor_taxa:.2f}"
                          f"\nVENDEDOR RECEBE: R${valor_compra - valor_taxa}")
else:
    print("Esse valor não é compativel com a transação.")
