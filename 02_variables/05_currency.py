pesos = int(input("Quanto restou em pesos? "))
solas = int(input("Quanto restou em solas? "))
reais = int(input("Quanto restou em reais? "))

pesos_tax = pesos * 0.00025
solas_tax = solas * 0.28
reais_tax = reais * 0.18

usd = (pesos_tax + solas_tax + reais_tax)
print(usd)