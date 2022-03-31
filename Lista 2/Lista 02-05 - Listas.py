"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 05 da lista 2 do bootcamp \código[s]

Enunciado:
Dada a seguinte lista lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] adicione o elemento 7000 logo após o elemento 6000 na lista acima. O resultado final deverá ser:
>>> [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""


lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

#lst.insert(2[1],7000)
lst[2][2].append(7000)
print (lst)
