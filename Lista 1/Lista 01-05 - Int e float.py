"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 05 da lista 1 do bootcamp \código[s]

Enunciado:
Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos. 
Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 3+1+4+1=9.
"""
numero = input("Digite um número com 4 dígitos: ")

numero1 = int(numero[0])
numero2 = int(numero[1])
numero3 = int(numero[2])
numero4 =int(numero[3])

resultado = numero1 + numero2 + numero3 + numero4

#solução usando lista
#numeros = []
#numeros.append(int(numero[0]))
#numeros.append(int(numero[1]))
#numeros.append(int(numero[2]))
#numeros.append(int(numero[3]))
#resultado = sum(numeros)

#elaborar solução usando looping

print(f"{numero1:.2f} + {numero2:.2f} + {numero3:.2f} + {numero4:.2f} = {resultado:.2f}")