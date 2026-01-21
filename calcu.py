def appSumar(num1, num2):
    resultado = num1 + num2
    return resultado
def appRestar(num1, num2):
    resultado = num1 - num2
    return resultado
def appMultiplicar(num1, num2):
    resultado = num1 * num2
    return resultado
n1 = int(input("Ingresa primer numero: "))
n2 = int(input("Ingresa segundo numero: "))
print(appSumar(n1, n2))
print (appRestar(n1, n2))
print(appMultiplicar(n1, n2))
