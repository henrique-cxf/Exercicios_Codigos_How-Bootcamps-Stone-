"""
How Bootcamps - Stone - /código[s]
Data: 14/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 04 da lista 5 do bootcamp \código[s]

Enunciado:
Uma aproximação para o valor de pi pode ser calculado a partir da fórmula abaixo (uma série infinita):
pi≈ 3+ 4/2x3x4 - 4/4x5x6+ 4/6x7x8 - 4/8x9x10 + 4/10x11x12 - 4/12x13x14+⋯
Escreva um programa que calcule o número pi com 15 aproximações. 
A primeira aproximação deve considerar apenas o primeiro termo da série, ou seja 3. 
A segunda aproximação deve considerar a soma até o segundo termo, e assim por diante!
"""


for elemento in range(10000000):
    if elemento == 0:
        aproximacao = 3
    else:
        if elemento % 2 != 0:
            aproximacao = aproximacao + 4 / ((elemento * 2) * ((elemento * 2) + 1) * ((elemento * 2) + 2)) 
        else:
            aproximacao = aproximacao - 4 / ((elemento * 2) * ((elemento * 2) + 1) * ((elemento * 2) + 2)) 

print(f"\nO valor de pi com 15 aproximações é igual à: {aproximacao}")