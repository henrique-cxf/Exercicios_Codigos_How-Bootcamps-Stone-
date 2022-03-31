"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 03 da lista 3 do bootcamp \código[s]

Enunciado:
Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
>>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>>> {“química”: 87, “física”: 83, matemática”: 81}

"""

materia_notas = {"Matemática": 81, "Física": 83, "Química": 87}

materia_notas_ordenado = dict(sorted(materia_notas.items(), key = lambda tupla: tupla[1], reverse = True))

print(materia_notas_ordenado)