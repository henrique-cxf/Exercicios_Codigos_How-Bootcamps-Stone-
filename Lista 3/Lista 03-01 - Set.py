"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 01 da lista 3 do bootcamp \código[s]

Enunciado:
Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que existam alunos matriculados conforme abaixo:
•	Alunos matriculados em inglês:
o	João Alves dos Santos
o	Maria Magalhães
o	Antônio da Silva Ferreira
o	José Júnior Jarbas
o	Henrique da Silva Sauro
o	Joaquina Ferreira da Silva
o	Fabiana Aparecida Bianco
o	Marrone Gutierres
o	Carlos Magno Farad
o	Antônio da Silva Júnior Amaral

•	Alunos matriculados em francês:
o	João Alves dos Santos
o	Antônio da Silva Ferreira
o	Fernanda Abdala Mohamed
o	Abner Mignon Alib
o	Alisson Figueiredo
o	Henrique da Silva Sauro
o	Maria Magalhães
o	Marrone Gutierres
o	Joaquina Ferreira da Silva

Faça um programa que responda as seguintes perguntas:

1.	Quantos alunos estão matriculados na escola, no total?
2.	Quantos e quais estão matriculados APENAS em INGLES?
3.	Quantos e quais estão matriculados APENAS em FRANCES?
4.	Quantos e quais estão matriculados EM AMBOS os cursos?
5.	Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?
"""

alunos_ingles = []
alunos_frances = []

alunos_ingles.append("João Alves dos Santos")
alunos_ingles.append("Maria Magalhães")
alunos_ingles.append("Antônio da Silva Ferreira")
alunos_ingles.append("José Júnior Jarbas")
alunos_ingles.append("Henrique da Silva Sauro")
alunos_ingles.append("Joaquina Ferreira da Silva")
alunos_ingles.append("Fabiana Aparecida Bianco")
alunos_ingles.append("Marrone Gutierres")
alunos_ingles.append("Carlos Magno Farad")
alunos_ingles.append("Antônio da Silva Júnior Amaral")

alunos_ingles.sort

alunos_frances.append("João Alves dos Santos")
alunos_frances.append("Antônio da Silva Ferreira")
alunos_frances.append("Fernanda Abdala Mohamed")
alunos_frances.append("Abner Mignon Alib")
alunos_frances.append("Alisson Figueiredo")
alunos_frances.append("Henrique da Silva Sauro")
alunos_frances.append("Maria Magalhães")
alunos_frances.append("Marrone Gutierres")
alunos_frances.append("Joaquina Ferreira da Silva")

alunos_frances.sort

qtd_alunos_matriculados = len(set(alunos_ingles) | set(alunos_frances))

print(f"\n{qtd_alunos_matriculados}")

print(f"\n\n{set(alunos_ingles) - set(alunos_frances)}")

print(f"\n\n{set(alunos_frances) - set(alunos_ingles)}")

print(f"\n\n{set(alunos_frances) & set(alunos_ingles)}")

print(f"\n\n{set(alunos_frances) ^ set(alunos_ingles)}")
