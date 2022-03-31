"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 03 da lista 1 do bootcamp \código[s]

Enunciado:
No exercício acima você calculou a área de um triângulo a partir da sua base e altura.
Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área.
Compare a resposta com o exercício acima, dada das mesmas entradas. Os resultados devem ser idênticos.
"""


s1 = float(input("Informe o valor, em metros, do primeiro lado do triângulo: "))
s2 = float(input("Informe o valor, em metros, do segundo lado do triângulo: "))
s3 = float(input("Informe o valor, em metros, do terceiro lado do triângulo: "))

s = (s1+s2+s3)/2

#area = sqrt(s * (s-s1) * (s-s2) * (s-s3))
area = (s * (s-s1) * (s-s2) * (s-s3))**(1/2)



print(f"A área do triângulo é igual à: {area:.2f} m²")
