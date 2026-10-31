#Jogo de adivinhar palavra!
palavraSecret = "perfume"
tentativas = 0
letrasAcertadas = []

print("a palavra secreta é:", "*" * len(palavraSecret))

while(True):
    
    letra = input("Digite uma letra qualquer para tentar descobrir a palavra secreta: ").lower()


    if len(letra) != 1:
        print("digite apenas uma letra!")
        continue

    tentativas += 1

    if letra in palavraSecret:
        if letra not in letrasAcertadas:
            letrasAcertadas.append(letra)
        print("Você acertou uma letra!")
    
    else:
        print("essa letra não está na palavra secreta!")

    palavra = ""
    for l in palavraSecret:
        if l in letrasAcertadas:
            palavra += l
        else:
            palavra += "*"

    print(palavra)

    if palavra == palavraSecret:
        print(f"Você acertou a palavra: {palavra}")
        print(f"Com essa quantidade de tentativas: {tentativas}")
        break
