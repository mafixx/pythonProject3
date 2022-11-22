"""
Empacotamento e desempacotamento de argumentos
ou
Argumentos arbitrários

*args   --> Lista arbitrária de argumentos (aqui os argumentos são passados para a função por posição)
**kwargs  --> Conjunto chave-valor de argumentos (aqui são passados por nome)

Os nomes args e kwargs são apenas nomes padrão que são apenas recomendados.
Pode ser utilizado qualquer nome

"""


# Exemplo de empacotamento de argumentos
def func01(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} = {valor}")


# Exemplo de desempacotamento de argumentos por nome
def func02(inicio, fim, valor):
    return inicio <= valor <= fim


if __name__ == "__main__":
    func01(nome="Maria", idade=30)
    func01(jogo="Brasil x Argentina", data="12 de dezembro de 2022")

    print(func02(**{"valor": 10, "inicio": 15, "fim": 20}))
    print(func02(**{"valor": 30, "inicio": 25, "fim": 40}))

