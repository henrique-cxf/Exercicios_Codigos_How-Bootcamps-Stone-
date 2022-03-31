"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 04 da lista 2 do bootcamp \código[s]

Enunciado:
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada 
juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: Exemplo de saída:
>>> Meses com temperatura acima da média anual de 35,5°:
>>> 1 – janeiro
>>> 3 – março
>>> 6 – junho
"""
temp_media_mensal = [42, 40.5, 39.8, 37.3, 33, 27, 19, 22, 28, 34, 38, 40.3]
meses_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

temp_media_anual = sum(temp_media_mensal) / len(temp_media_mensal)
i = 0
resultado = dict()
for temp in temp_media_mensal:
    if temp >= temp_media_anual:
        resultado[meses_ano[i]] = str(temp) + "°C"
        #print(f"{i+1} - {meses_ano[i]} com uma temperatura de {temp}°C") # resolvendo com print
    i = i + 1
print(resultado.items())
