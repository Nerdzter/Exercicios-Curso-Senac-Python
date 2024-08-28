# Preços dos itens
hamburguer = 10.0
x_burguer = 12.0
x_eggs_burguer = 15.0
refrigerante = 5.0

# Quantidade de itens consumidos
qtd_hamburguer = int(input("Quantidade de Hamburguer: "))
qtd_x_burguer = int(input("Quantidade de X-Burguer: "))
qtd_x_eggs_burguer = int(input("Quantidade de X-Eggs-Burguer: "))
qtd_refrigerante = int(input("Quantidade de Refrigerante: "))

# Calculo da conta
conta = (qtd_hamburguer * hamburguer) + (qtd_x_burguer * x_burguer) + (qtd_x_eggs_burguer * x_eggs_burguer) + (qtd_refrigerante * refrigerante)

print("Valor da conta: R$", conta)