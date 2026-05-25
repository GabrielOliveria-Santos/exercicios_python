try:
    valor = float(input("Digite o valor do produto: "))
    quantidade = int(input("Digite a quantidade de produtos: "))
    total = valor * quantidade
    print("total a pagar: ", total)
except:
     print("Erro ao calcular o total")