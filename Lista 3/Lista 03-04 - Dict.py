"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 04 da lista 3 do bootcamp \código[s]

Enunciado:
Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dada o dicionário
>>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
A saída deverá ser
>>> {1: 8, 2: 4, 3: 6}
"""

dicionario = {1: 'vermelho', 2: 'azul', 3: 'marrom'}

for chaves in dicionario:
        dicionario[chaves]= len ( dicionario[chaves])

print(dicionario)
