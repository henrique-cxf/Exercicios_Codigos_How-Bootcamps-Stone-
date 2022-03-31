"""
How Bootcamps - Stone - /código[s]
Data: 14/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 01 da lista 5 do bootcamp \código[s]

Enunciado:
 Neste exercício, você criará um programa que calcula a média de uma coleção de valores inseridos pelo usuário e imprime-a na tela. 
 O usuário digitará 0 como um valor para indicar que nenhum outro valor será fornecido. 
 Seu programa deve exibir uma mensagem de erro se o primeiro valor inserido pelo usuário for 0.
 Atenção! - Como o 0 é um valor de condição de parada, ele não deve entrar no cálculo da média!
"""

valores = []

valor = float(input("Digite o primeiro valor (diferente de zero): "))
valores.append(valor)

deuruim = 0

if valor == 0:
    print("\nErro! O primeiro valor digitado foi igual à zero.")
    deuruim = 1

while valor != 0:
    valor = float(input("Digite um número real. (Digite 0 para parar): "))
    valores.append(valor)

if deuruim != 1:
    valores.remove(0)
    media = sum(valores) / len(valores)
    print(f"A média dos {len(valores)} valores digitados é igual à {media}.")
