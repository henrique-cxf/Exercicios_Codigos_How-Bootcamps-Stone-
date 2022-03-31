"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 02 da lista 4 do bootcamp \código[s]

Enunciado:
Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.
"""
numero1 = float(input("Forneça o primeiro número: "))
numero2 = float(input("Forneça o segundo número: "))

resultado = numero1 % numero2

if resultado == 0:
    print(f"O primeiro número fornecido {numero1} é divisível pelo segundo número fornecido {numero2}")
else:
    print(f"O primeiro número fornecido {numero1} não é divisível pelo segundo número fornecido {numero2}")