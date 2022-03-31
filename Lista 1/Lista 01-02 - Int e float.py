"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 02 da lista 1 do bootcamp \código[s]

Enunciado:
Faça um programa que receba a base e altura de um triângulo e imprima a área dele.
"""

base = float(input("informe o valor da base do triângulo em metros: "))
altura = float(input("informe o valor da altura do triângulo em metros: "))

area = (base * altura) / 2

print(f"A área do triângulo é igual à: {area:.2f} m²")
