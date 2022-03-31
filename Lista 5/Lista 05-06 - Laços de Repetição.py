"""
How Bootcamps - Stone - /código[s]
Data: 14/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 06 da lista 5 do bootcamp \código[s]

Enunciado:
Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.
"""

qtd_termos = int(input("Informe o número de termos da série (maior ou igual à 1): "))

serie = 1
num_termos = 1

for elemento in range(1, qtd_termos):
    serie = serie + 1 / elemento
    num_termos = num_termos + 1

print(f"Considerando {num_termos} termos, o resultado é {serie}")