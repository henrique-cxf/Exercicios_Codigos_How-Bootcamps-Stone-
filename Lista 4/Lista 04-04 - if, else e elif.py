"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 04 da lista 4 do bootcamp \código[s]

Enunciado:
Faça um programa que imprima na tela se um dado ano é bissexto ou não de acordo com as regras na ordem abaixo:

1.	Um ano que é divisível por 400 é bissexto.
2.	Dos anos que não entram na regra 1, se o ano for divisível por 100 então ele não é bissexto.
3.	Dos anos que não entram na regra 2, se o ano for divisível por 4 então ele é um ano bissexto.
4.	Todos os outros anos não são bissextos

"""

ano = float(input("Forneça um ano: "))

regra1 = ano % 400
regra2 = ano % 100
regra3 = ano % 4

if regra1 == 0:
    print(f"\nO ano é bissexto")
else: 
    if regra2 == 0:
        print(f"\nO ano não é bissexto")
    else:
        if regra3 == 0:
            print(f"\nO ano é bissexto")
        else:
            print(f"\nO ano não é bissexto")

