"""
Criar uma calculadora de nota com 3 parâmetros: nota_1, nota_2 e nota_3

media < 5 -> reprovado
media >= 5 -> em exame
media >= 7 -> aprovado
"""


def calcula_media(nota_1, nota_2, nota_3):
    return (nota_1 + nota_2 + nota_3) / 3


def exibir_resultado(media):
    if media < 5:
        print("Reprovado!")
    elif 5 <= media < 7:
        print("Em exame.")
    else:
        print("Aprovado!")


if __name__ == "__main__":

    media = calcula_media(4, 5.5, 5)
    exibir_resultado(media)

    exibir_resultado(calcula_media(6, 6, 9))

