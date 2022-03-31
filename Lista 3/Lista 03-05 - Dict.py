"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 05 da lista 3 do bootcamp \código[s]

Enunciado:
Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. Exemplo: dado o dicionário
>>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
A saída deve ser
>>> Nota máxima -> Júnior : 80
>>> Nota mínima -> Theodoro : 20

"""

alunos_e_notas = {'Theodoro': 20, 'Márcia': 50, 'Júnior': 80}

valor_maximo = max(alunos_e_notas.values())
valor_minimo = min(alunos_e_notas.values())

lista_alunos_e_notas = list(alunos_e_notas.values())

indice_maximo = lista_alunos_e_notas.index(valor_maximo)


indice_minimo = lista_alunos_e_notas.index(valor_minimo)

print(f"Nota máxima -> {list(alunos_e_notas.keys())[indice_maximo]} : {valor_maximo}")

print(f"Nota máxima -> {list(alunos_e_notas.keys())[indice_minimo]} : {valor_minimo}")