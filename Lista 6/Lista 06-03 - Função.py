"""
How Bootcamps - Stone - /código[s]
Data: 20/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 03 da lista 6 do bootcamp \código[s]

Enunciado:
Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""

def inverte_ordem(num: int) -> int:
    """Reverte a ordem de um número inteiro. Por exemplo: 127 -> 721"""
    num_str = str(num)
    resultado = ""
    for index in range(len(num_str)):
        resultado = resultado + num_str[len(num_str)-1-index]
    return int(resultado)

num = 127

print(f"\n{num} -> {inverte_ordem(num)}")
