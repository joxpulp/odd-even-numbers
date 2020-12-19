numerosImpares = 0
numerosPares = 0

numero = int (input ("Introduce un número o escriba 0 para detener:"))

while numero != 0:
    
    if numero % 2 == 1:
        numerosImpares += 1
    else:
        numerosPares += 1
    numero = int (input ("Introduce un número o escriba 0 para detener:"))


print("Números impares: ", numerosImpares)
print("Números pares: ", numerosPares)