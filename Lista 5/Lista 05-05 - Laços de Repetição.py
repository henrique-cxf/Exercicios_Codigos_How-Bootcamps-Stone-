"""
How Bootcamps - Stone - /código[s]
Data: 14/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 05 da lista 5 do bootcamp \código[s]

Enunciado:
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados
alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto
e depois calcular a média com as notas restantes). As notas não são informadas ordenadas. 
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7
Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""

nome = input("Informe o nome do atleta: ")
notas = []

for elemento in range(7):
    nota = float(input(f"Informe a nota de n° {elemento + 1} do atleta "))
    notas.append(nota)

maior_nota = notas.pop(notas.index(max(notas)))
menor_nota = notas.pop(notas.index(min(notas)))

media = sum(notas) / len(notas)

print(f"\nResultado Final:")
print(f"Atleta: {nome}")
print(f"Melhor nota: {maior_nota}")
print(f"Pior nota: {menor_nota}")
print(f"Média: {media}")
