altura = float(input("Digite a altura: "))
comprimento = float(input("Digite o comprimento: "))

area = altura * comprimento
litros = area / 3
litrosV = litros / 3.6
preco = litrosV * 107

print("A quantidade de latas de tinta a serem compradas é: ",litrosV,
      "\nE o preço total é: ", preco)