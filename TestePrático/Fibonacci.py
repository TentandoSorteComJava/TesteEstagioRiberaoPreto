import math

def quadradoPerfeito(x):
    s = int(math.sqrt(x))
    return s * s == x

def numeroFibonacci(n):
    return quadradoPerfeito(5 * n * n + 4) or quadradoPerfeito(5 * n * n - 4)

numero = int(input("De um numero: "))

if numeroFibonacci(numero):
    print(numero, " esta na sequencia Fibonacci.")
else:
    print(numero, "5 nao esta na sequencia Fibonacci.")