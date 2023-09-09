import random
import math
from fractions import Fraction

x = input ("Ingese el valor de x: ")
x = int(x)
valores = {}

a = random.randint(1, 10)
c = random.randint(1, 10)

numerador = Fraction((-1 * a) * math.pow(x, 2) - c)
denominador = Fraction(x)

b = numerador / denominador

valores = {
  'a': a,
  'b': b,
  'c': c,
}

def validarEcuacion(a, b, c, x):
  resultadoA = a * math.pow(x, 2)
  resultadoB = b * x
  resultadoFinal = resultadoA + resultadoB + c
  print(f'Los valores son: {valores}')
  print(f'ax^2 = ({a})({x})^2 = {resultadoA}')
  print(f'bx = ({b})({x}) = {resultadoB}')
  print(f'c = {c}')
  print(f'({resultadoA}) + ({resultadoB}) + ({c})')
  print(f'{resultadoFinal}')

validarEcuacion(valores['a'], valores['b'], valores['c'], x)

# Equipo
# Angel Almanza
# Luis Murillo