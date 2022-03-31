"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 04 da lista 1 do bootcamp \código[s]

Enunciado:
Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário.
"""

peso = float(input("Inform seu peso em kg: "))
altura = float(input("Informe sua altura em metros: "))

imc = peso / (altura **2)

print(f"O IMC do usuário é igual à {imc:.2f} kg/m²")