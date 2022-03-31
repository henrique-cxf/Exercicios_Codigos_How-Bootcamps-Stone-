"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 01 da lista 1 do bootcamp \código[s]

Enunciado:
Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
•	A soma de A e B;
•	A diferença quando se subtrai B de A;
•	O produto (multiplicação) entre A e B;
•	O quociente (parte inteira da divisão) quando se divide A por B;
•	O resto da divisão entre A e B;
•	O resultado de log10 de A;
•	O resultado de A elevado a B;
"""

from cmath import log10


a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

print(a + b)
print(b - a)
print(a * b)
print(a // b)
print(a % b)
print(log10(a))
print(a ** b)

