#Ordem de listas
lista = []

while(True):

    addLista = input("digite aqui numeros que deseja colocar na lista: ")

    if(addLista.isdigit() == True):
        lista.append(int(addLista))
    else:
        print("digite apenas digitos!")

    numerosOrdem = sorted(lista)
    

    saida = input("\nSe você quiser sair aperte (s): ").lower()
    if (saida == "s"):
        print("você saiu!!!")
        print(numerosOrdem)
        break
