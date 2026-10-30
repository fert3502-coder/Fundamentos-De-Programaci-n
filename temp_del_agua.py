TEMP_SOLIDO = 0
TEMP_GAS = 100

temp = int(input("Temperatura del agua: "))

if TEMP_SOLIDO <= temp <= TEMP_GAS:
   print("Es liquido")
else:
   print("No es liquido")
