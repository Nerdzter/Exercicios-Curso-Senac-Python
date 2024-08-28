# Valor da fábrica
valor_fabrica = float(input("Valor da fábrica: "))

# Calculo do imposto e valor pago ao vendedor
imposto = valor_fabrica * 0.4
valor_vendedor = valor_fabrica * 0.05

# Calculo do valor final
valor_final = valor_fabrica + imposto + valor_vendedor

print("Valor pago de imposto: R$", imposto)
print("Valor pago ao vendedor: R$", valor_vendedor)
print("Valor final: R$", valor_final)