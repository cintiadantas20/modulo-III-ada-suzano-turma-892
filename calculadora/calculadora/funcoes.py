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

def calcule():
    a = int(input('Digite um número:'))
    b = int(input('Digite outro número:'))
    operacao = input('Digite uma operação:')
    if operacao == 'soma'.lower() or '+':
        resultado = soma(a, b)
    elif operacao == 'subtracao'.lower() or '-':
        resultado = subtracao(a, b)
    elif operacao == 'multiplicacao'.lower() or '*':
        resultado = multiplicacao(a, b)
    elif operacao == 'divisao'.lower() or '/':
        resultado = divisao(a, b)
    print(resultado)
    return resultado
