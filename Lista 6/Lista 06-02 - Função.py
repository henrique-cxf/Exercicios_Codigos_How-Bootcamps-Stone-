"""
How Bootcamps - Stone - /código[s]
Data: 20/03/2022
Autor: Henrique Ferreira
E-mail: henrique.ccxf@gmail.com
Git:
Linkedin: https://www.linkedin.com/in/henrique-ferreira1
Objetivos do scripts:
    Realizar o exercício 02 da lista 6 do bootcamp \código[s]

Enunciado:
Escreva uma função que, dado três comprimentos de retas quaisquer, diga se essas três retas podem ou não formar um triângulo,
retornando true em caso positivo e false em caso negativo. Dica n°1: Se algum dos comprimentos for negativo ou zero, não é possível formar um triângulo.
Dica n°2: se qualquer um dos comprimentos for maior ou igual à soma dos outros dois, então os comprimentos não podem ser usados para formar um triângulo.
Caso contrário, eles podem formar um triângulo.
"""
def formar_triangulo2(lado1: float, lado2: float, lado3: float) -> str:
    """Verifica se três retas poderiam formar um triângulo. Caso não possam formar um triângulo, a função indicará qual condição não foi atendida."""
    if lado1 > 0:
        if lado2 > 0:
            if lado3 > 0:
                if lado1 < lado2 + lado3:
                    if lado2 < lado1 + lado3:
                        if lado3 < lado1 + lado2:
                            return "Os comprimentos fornecidos atendem à todos os crtiérios para formarem um triângulo"
                        else:
                            return "Os comprimentos fornecidos não podem formar um triângulo, pois Lado3 >= Lado1 + Lado2"
                    else:
                        return "Os comprimentos fornecidos não podem formar um triângulo, pois Lado2 >= Lado1 + Lado3"
                else:
                    return "Os comprimentos fornecidos não podem formar um triângulo, pois Lado1 >= Lado2 + Lado3"
            else:
                return "Erro! O terceiro lado fornecido é menor do que zero."
        else:
            return "Erro! O segundo lado fornecido é menor do que zero."
    else:
        return "Erro! O primeiro lado fornecido é menor do que zero."

lado1: float = -3
lado2: float = 4
lado3: float = 5

print(f"\n{formar_triangulo2(lado1, lado2, lado3)}")


lado1: float = 3
lado2: float = -4
lado3: float = 5

print(f"\n{formar_triangulo2(lado1, lado2, lado3)}")

lado1: float = 3
lado2: float = 4
lado3: float = -5

print(f"\n{formar_triangulo2(lado1, lado2, lado3)}")

lado1: float = 3
lado2: float = 4
lado3: float = 5

print(f"\n{formar_triangulo2(lado1, lado2, lado3)}")

lado1: float = 10
lado2: float = 4
lado3: float = 5

print(f"\n{formar_triangulo2(lado1, lado2, lado3)}")

lado1: float = 3
lado2: float = 10
lado3: float = 5

print(f"\n{formar_triangulo2(lado1, lado2, lado3)}")

lado1: float = 3
lado2: float = 4
lado3: float = 10

print(f"\n{formar_triangulo2(lado1, lado2, lado3)}")


"""
### VERSÃO SIMPLIFICADA####
def formar_triangulo(lado1: float, lado2: float, lado3: float) -> str:
    '''Verifica se três retas poderiam formar um triângulo.'''
    if (lado1 > 0 and lado2 > 0 and lado3 > 0):
        if (lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2):
            return "Os comprimentos fornecidos podem formar um triângulo"
        else:
            return "Os comprimentos fornecidos não podem formar um triângulo"
    else:
        return "Erro! Digite valores maiores do que zero para todos os lados dos triângulos."

lado1: float = -3
lado2: float = 4
lado3: float = 5

print(f"\n{formar_triangulo(lado1, lado2, lado3)}")


lado1: float = 3
lado2: float = -4
lado3: float = 5

print(f"\n{formar_triangulo(lado1, lado2, lado3)}")

lado1: float = 3
lado2: float = 4
lado3: float = -5

print(f"\n{formar_triangulo(lado1, lado2, lado3)}")

lado1: float = 3
lado2: float = 4
lado3: float = 5

print(f"\n{formar_triangulo(lado1, lado2, lado3)}")

lado1: float = 10
lado2: float = 4
lado3: float = 5

print(f"\n{formar_triangulo(lado1, lado2, lado3)}")

lado1: float = 3
lado2: float = 10
lado3: float = 5

print(f"\n{formar_triangulo(lado1, lado2, lado3)}")

lado1: float = 3
lado2: float = 4
lado3: float = 10

print(f"\n{formar_triangulo(lado1, lado2, lado3)}")
"""