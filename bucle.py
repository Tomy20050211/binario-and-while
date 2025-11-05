number = int(input("Ingresa un numero entero: "))

for contador in range(number):
    print("Numero: ", contador + 1)
    contador +=1

if number %2 == 0:
    print("Tu numero es par")
else:
    print("Tu numero es impar")