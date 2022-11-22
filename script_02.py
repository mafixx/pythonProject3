"""
Empacotamento e desempacotamento de argumentos
ou
Argumentos arbitrários

*args   --> Lista arbitrária de argumentos (aqui os argumentos são passados para a função por posição)
**kwargs  --> Conjunto chave-valor de argumentos (aqui são passados por nome)

Os nomes args e kwargs são apenas nomes padrão que são apenas recomendados.
Pode ser utilizado qualquer nome

"""
from random import uniform
from exercicio_01 import calcula_media, exibir_resultado


# Empacotamento
def func01(*args):
    return len(args)


# Desempacotamento
def func02(inicio, fim, valor):
    return inicio <= valor <= fim


if __name__ == "__main__":
    # Estamos "empacotando" os argumentos no parâmetro args
    print(func01(4, 7, 10))
    print(func01("Cachorro", "Gato", 82.9))
    print(func01())

    # Chamando a função passando os valores dos argumentos normalmente
    print(func02(3, 4, 10))

    lista_faixas = [
        [4, 6, 5],
        [10, 90, 56],
        [30, 45, 20]
    ]

    for lista in lista_faixas:
        # print(func02(lista[0], lista[1], lista[2]))
        # Substituimos a expressão acima por:
        print(func02(*lista))

    # Exemplo 2: Calculando as médias aleatórias de 100 alunos
    # Usando list comprehension parar criar uma lista de listas com 100 itens
    lista_notas = [
        [uniform(1, 10), uniform(1, 10), uniform(1, 10)] for _ in range(100)
    ]
    print(lista_notas)

    for lista in lista_notas:
        exibir_resultado(calcula_media(*lista))
