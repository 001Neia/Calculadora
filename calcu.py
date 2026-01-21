def appSumar(num1, num2):
    resultado = num1 + num2
    return resultado
def aplicacionParaRestar(numero1, numero2):
    ejecucion = numero1 - numero2
    return ejecucion
n1 = int(input("Ingresa primer numero: "))
n2 = int(input("Ingresa segundo numero: "))
print(appSumar(n1, n2))
print(aplicacionParaRestar(n1, n2))