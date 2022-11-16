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