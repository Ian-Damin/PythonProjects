lista = [2, 3, 6, 7, 10, 1]
resultadoSoma = 0
resultadoMultiplica = 0
resultadoMedia = 0
maior = 0
menor = lista[0]
digitoPar = 0
digitoImpar = 0

for numeros in lista:
    resultadoSoma += numeros
    resultadoMultiplica *= numeros
    resultadoMedia = resultadoSoma/len(lista)

for numeros in lista:
    if(numeros > maior):
        maior = numeros

for numeros in lista:
    if (numeros < menor):
        menor = numeros

for numeros in lista:
    if (numeros % 2 == 0):
        digitoPar += 1
    else:
        digitoImpar += 1
    

print(f"Soma: {resultadoSoma}")
print(f"Multiplicação: {resultadoMultiplica}")
print(f"Media: {resultadoMedia:.3}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Pares: {digitoPar}")
print(f"Impares: {digitoImpar}")
