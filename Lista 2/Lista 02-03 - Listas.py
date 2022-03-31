"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 03 da lista 2 do bootcamp \código[s]

Enunciado:
Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições. Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser
>>> O maior elemento é 8 e está na posição 3
>>> O menor elemento é 3 e está na posição 4
Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.
"""

lista = [16541651, 4, 6, 8, -10, 4]

maior_elemento = max(lista)
posicao_maior_elemento = lista.index(maior_elemento)
menor_elemento = min(lista)
posicao_menor_elemento = lista.index(menor_elemento)

print(f">>> O maior elemento é {maior_elemento} e está localizado na posição {posicao_maior_elemento}")
print(f">>> O maior elemento é {menor_elemento} e está localizado na posição {posicao_menor_elemento}")

#Solução 2

