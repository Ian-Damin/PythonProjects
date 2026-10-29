carrinho = []
itens = ["Maçã", "Banana", "Pera", "Alface"]

print("Escolha o que você quer colocar no carrinho:\n")

while True:
    for i, item in enumerate(itens):
        print(i, item)

    escolha = input("\nDigite o número do produto (ou 's' para finalizar): ")

    if escolha.lower() == "s":
        break

    if not escolha.isdigit():
        print("Digite apenas números!")
        continue

    escolha = int(escolha)

    if escolha >= len(itens):
        print("Escolha um número que foi mostrado acima!")
        continue

    carrinho.append(itens[escolha])
    print(f"{itens[escolha]} adicionado! Carrinho: {carrinho}\n")

print("\nSeu carrinho final:")
for item in carrinho:
    print("-", item)
