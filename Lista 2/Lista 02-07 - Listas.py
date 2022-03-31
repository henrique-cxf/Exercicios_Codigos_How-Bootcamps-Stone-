"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 07 da lista 2 do bootcamp \código[s]

Enunciado:
Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro.

Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para int.
"""

lst = [ "1" , "7", "99", "15"]
resultado1 = []
resultado2 = []
for elemento in range(len(lst)):
    lst[elemento] = int(lst[elemento])
    #resultado1.append(lst[elemento])
    #resultado1.append(type(lst[elemento]))
#print (f"\n{lst}")
print(f"\n{resultado1}")

for elemento in range(len(lst)):
    lst[elemento] = str(lst[elemento])
    #resultado2.append(lst[elemento])
    #resultado2.append(type(lst[elemento]))
print (f"\n{lst}")
#print(f"\n{resultado2}\n")

