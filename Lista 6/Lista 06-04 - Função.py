"""
How Bootcamps - Stone - /código[s]
Data: 20/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 04 da lista 6 do bootcamp \código[s]

Enunciado:
Embaralha palavras: Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""

import random


def embaralha_palavras(palavra: str) -> str:
    "Retorna uma palavra com caracteres embaralhados"
    resultado = ""
    palavra = palavra.lower()
    palavra_embaralhada = list(palavra)
    
    for elemento in range(len(palavra_embaralhada)):
        num_aleatorio = random.randrange(0, int(len(palavra_embaralhada)))
        resultado = resultado + palavra_embaralhada.pop(num_aleatorio)
    return resultado

palavra = "PyThon"
print(embaralha_palavras(palavra))