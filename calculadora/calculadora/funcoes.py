def soma(a, b):
    soma = a + b
    return soma

def subtracao(a,b):
    subtracao = a - b
    return subtracao

def multiplicacao(a,b):
    mult = a * b
    return mult

def divisao(a, b):
    if b != 0:
        divisao = a / b
    else:
        print('Divisão inválida')
        divisao = 0
    return divisao