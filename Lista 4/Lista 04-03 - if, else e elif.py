"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 03 da lista 4 do bootcamp \código[s]

Enunciado:
A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns

Barulho	Nível sonoro (dB)
Britadeira	130
Cortador de grama	106
Despertador	70
Cômodo em silêncio	40

Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho. 
Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado está. 
Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo. 
"""

nivel_sonoro = float(input("Informe o nível sonoro em decibeís: "))

britadeira = 130
cortador_de_grama = 106
despertador = 70
comodo_em_silencio = 40

if nivel_sonoro <= comodo_em_silencio:
    mensagem = "O nível sonoro informado é menor ou igual ao ruído mínimo da tabela (Cômodo em silêncio = 40 Dbs)"
else:
    if nivel_sonoro <= despertador:
        mensagem = "O nível sonoro informado encontra-se entre o nível sonoro de um despertado (70 Dbs), valor incluso no intervalo, e um cômodo em silêncio (40 Dbs)"
    else:
        if nivel_sonoro < cortador_de_grama:
            mensagem = "O nível sonoro informado encontra-se entre o nível sonoro de um cortador de grama (106 Dbs), valor incluso no intervalo, e um despertador (70 Dbs)"
        else:
            if nivel_sonoro < britadeira:
                mensagem = "O nível sonoro informado encontra-se entre o nível sonoro de um cortador de grama (106 Dbs), valor incluso no intervalo, e uma britadeira (130 Dbs)"
            else:
                mensagem = "O nível sonoro informado é maior ou igual ao ruído máximo da tabela (Britadeira = 130 Dbs)"

print(f"\n{mensagem}")











