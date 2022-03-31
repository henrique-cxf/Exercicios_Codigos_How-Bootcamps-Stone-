"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 05 da lista 4 do bootcamp \código[s]

Enunciado:
Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo) com três letras, um traço e quatro números. Exemplos: 
•	Dada a entrada ABT-1234 o programa deveria exibir True
•	Dada a entrada JKL9999 o programa deveria exibir False
•	Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False 

"""

placa = input("Digite a placa do carro no seguinte formato (LLL-1111): ").upper()

letras = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "W", "Z")
numeros = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

resultado = True

if len(placa) != 8:
    print(f"\nErro! A placa contem menos ou mais que 8 caracteres.")
    resultado = False

else:
    
    for caracter in placa[0:3]:
        if caracter not in letras:
            resultado = False
            break
    
    if placa[3] != "-":
        resultado = False
    
    for caracter in placa[4:8]:
        if caracter not in numeros:
            resultado = False

if resultado == False:
    print(f"\n\nA sequência informada não pertence à uma placa ({resultado})")
else:
    print(f"\n\nA sequência informada pertence à uma placa ({resultado})")


