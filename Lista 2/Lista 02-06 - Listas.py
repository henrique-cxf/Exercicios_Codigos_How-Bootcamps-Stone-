"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 06 da lista 2 do bootcamp \código[s]

Enunciado:
Faça um programa que remova strings vazias de uma lista de strings. Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser
>>> [“Olá”, “meu”, “nome”, “é”, “facilitador”]
"""

lst = ["Olá", "", "meu", "nome", "", "é", "facilitador",""]

while "" in lst:
    lst.remove("")
print(lst)

#opção professor
lst_sem_str_vazias = []

for palavra in lst:
    # Se a string não for vazia (sim, isso é uma condição!)
    if palavra:
        lst_sem_str_vazias.append(palavra)

print(lst_sem_str_vazias)