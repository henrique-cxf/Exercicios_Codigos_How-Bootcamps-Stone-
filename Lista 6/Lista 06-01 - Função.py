"""
How Bootcamps - Stone - /código[s]
Data: 20/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 01 da lista 6 do bootcamp \código[s]

Enunciado:
Em uma determinada país, as tarifas de táxi consistem em uma tarifa básica de R$4,00 mais R$0,25 para cada 140 metros percorridos.
Escreva uma função que receba a distância percorrida (em quilômetros) como único parâmetro e retorna a tarifa total como único resultado.
Escreva um programa que demonstre o uso da sua função.
"""
def tarifa_taxi(dist: float) -> float:
    """Calcula a tarifa total, a partir da distância em km, de um serviço de táxi."""
    tarifa_total = 4 + dist*1000*0.25/140
    return tarifa_total
    
distancia = float(input("Informe a distância em km percorrida durante sua viagem: "))

tarifa_total = tarifa_taxi(distancia)

print(f"\nO preço de sua viagem de {distancia} km é igual à R${tarifa_total:4.2f}")