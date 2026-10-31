#list comprehension.
#criação de numeros elevado ao quadrado e ao cubo.

numeros = [1,2,3,4]
#lista com numeros.
quadrados = [numero ** 2 for numero in numeros]
#criação da formula quadratica.
print (*quadrados) #imprimir função

numeros1 = [1,2,3,4]
cubo = [numero ** 3 for numero in numeros]
print (*cubo)

