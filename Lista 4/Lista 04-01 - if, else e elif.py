"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 01 da lista 4 do bootcamp \código[s]

Enunciado:
Escreva um programa que diga se um número dado pelo usuário é par ou ímpar
"""
numero = float(input("Forneça um número: "))

resultado = numero % 2

if resultado == 0:
    print("O número é par")
else:
    print("O número é ímpar")