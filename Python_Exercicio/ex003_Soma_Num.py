"""
Crie um programa que leia dois numeros e retorne a soma entre eles.
"""


def soma(x, y):
    return x + y


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

print(f"Soma entre {n1} + {n2} = {soma(n1, n2)}")
