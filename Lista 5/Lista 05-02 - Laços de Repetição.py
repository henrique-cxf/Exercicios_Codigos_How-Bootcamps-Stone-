"""
How Bootcamps - Stone - /código[s]
Data: 14/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 02 da lista 5 do bootcamp \código[s]

Enunciado:
Escreva um programa que exiba uma tabela de conversão de temperatura para graus Celsius e graus Fahrenheit. 
A tabela deve incluir linhas para todas as temperaturas entre 0 e 100 graus Celsius que são múltiplos de 10 graus Celsius. 
Dê um título apropriado para cada coluna. A fórmula para converter entre graus Celsius e graus Fahrenheit podem ser encontrados 
na Internet (faz parte do exercício pesquisar!)
"""

temperaturas = []
indice = 1

for temperatura in range(100):
    if temperatura % 10 == 0:
        fahrenheit = ((temperatura * 9) / 5) + 32
        #dados = [temperatura, fahrenheit]
        temperaturas.append([indice, temperatura, fahrenheit])
        indice = indice + 1
    

from tabulate import tabulate as tbl

print(tbl(temperaturas, headers = ["Índice", "°C", "°F"]))






