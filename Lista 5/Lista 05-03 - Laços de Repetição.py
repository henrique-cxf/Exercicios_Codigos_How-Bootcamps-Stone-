"""
How Bootcamps - Stone - /código[s]
Data: 14/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 03 da lista 5 do bootcamp \código[s]

Enunciado:
 Um determinado zoológico cobra a entrada com base na idade do visitante. Os visitantes com 2 anos de idade ou menos não pagam para entrar.
 Crianças entre 3 e 12 anos custa R$14,00. Idosos com 65 anos ou mais custam R$18,00. A entrada para todos os outros visitantes é de R$23,00.
 Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo, com uma idade inserida em cada linha.
 O usuário digitará uma linha em branco para indicam que não há mais visitantes no grupo.
 Em seguida, seu programa deve exibir o custo de admissão para o grupo com uma mensagem apropriada.
 O custo deve ser exibido usando duas casas decimais.
"""
custo = []

idade = int(input("Digite a idade do primeiro visitante: "))

while idade != 0:
    idade = int(input("Digite a idade do próximo visitante (Digite 0 para parar): "))
    if idade <= 2:
        preco = 0
    elif idade <= 12:
        preco = 14
    elif idade >= 65:
        preco = 18
    else:
        preco = 23
    custo.append(preco)

    print(f"O grupo de {len(custo)} pessoas, deverá pagar R${sum(custo):10.2f}")

    continuar = True

preco_final = 0.0