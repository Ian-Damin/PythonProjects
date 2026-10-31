#Sorted names
nomes = []

while(True):

    adicionarNome = input("Escreva um nome aqui: ")

    if(adicionarNome.isalpha() == True):
        nomes.append(adicionarNome)
        nomesOrdem = sorted(nomes)
    else:
        print("Você digitou um digitou ou caracter especial! ")



    saida = input("\nSe você quiser sair aperte (s): ").lower()
    if (saida == "s"):
        print("você saiu!!!")
        print(nomesOrdem)
        break
