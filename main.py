print("Hola mundo")

a = 2
b = 3

suma = a + b

print(f"La suma es {suma}")

def saludar ():
  print("Hola")


saludar()
print("Fuera de la funcion")

a = 9
b = 50

if (a > b):
  print("A es mayor que B")
else:
  print("A no es mayor que B")

a = 20

if (a <= 10 and a >= 1):
  print("Esta entre 1 y 10")
else:
  print("No esta entre 1 y 10")


i = 1
while i <= 10:
  print (i)
  i += 1

for k in range(11):
  print(k)

print("Fin del cliclo")

for k in range(1, 11):
  print(k)

print("Fin del cliclo")

for k in range(1, 11, 2):
  print(k)

print("Fin del cliclo")

print("Numeros pares del 1 - 100")
for k in range(0, 101, 2):
  print(k)


nombre = input('Ingresa tu nombre: ')
print(f"Hola {nombre}")

import math

def calcularAreaCiruclo(radio):
  return math.pi * math.pow(radio, 2)


radio = input("Ingresa el radio del cirulo: ")
area = calcularAreaCiruclo(float(radio))
print(f"El area del circulo es: {area}")

def esPrimo(num):
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i < num:
    if num % i == 0:
      return False
    i += 1
  return True


num = esPrimo(int(input("Dame un numero para verificar si es primo: ")))

if num:
  print("Es primo")
else:
  print("No es primo")
