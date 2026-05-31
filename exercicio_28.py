class Produto:
    def __init__(self,nome,preço):
        self.nome = nome
        self.preço = preço

    def ExibirValor(self):
        print(f"nome: {self.nome} | preço: R${str(self.preço).replace(".",",")}")

def valor_compra(valor,quantidade):
    return valor * quantidade

produtos = []

while True:
    print("\nescolha o numero da opção:\n1- Cadastrar Produto\n2- Listar Produtos\n3- Comprar Produto\n4- Sair")
    menu = int(input())

    if menu == 1:
        while True:
            try:
                produto = {
                "nome": "" ,
                "preço": ""
                }
                while True:
                    produto["nome"] = input("Digite o nome do produto: ")
                    if produto["nome"] == "":
                        print("Erro: Digite o nome correto")
                        continue
                    break

                while True:
                    produto["preço"] = float(str(input("Digite o preço do produto: ")).replace(",","."))
                    if produto["preço"] <= 0:
                        print("Erro: Digite o preço correto")
                        continue
                    break
            except ValueError:
                print("Erro:Digite o valor correto")
                continue
            break
            
        produto1 = Produto(produto["nome"],produto["preço"])
        produtos.append(produto1)

    elif menu == 2:
        if len(produtos) == 0:
            print("Nenhum produto cadastrado")
        
        else:
            for indice,produto in enumerate(produtos):
                print(f"numero do produto: {indice} | nome do produto: {produto.nome} | preço do produto: {str(produto.preço).replace(".",",")}")
    
    elif menu == 3:
            try:
                numero_produto = int(input("Digite o numero do produto: "))
                quantidade = int(input("Digite a quantidade de produtos: "))
            except ValueError:
                print("Erro:Digite o valor correto")
                continue
            try:
                produto_escolhido = produtos[numero_produto]
            except:
                print("digite o numero do produto correto")
                continue
            valor_final = int(valor_compra(produto_escolhido.preço,quantidade))
        
            if valor_final >= 100:
                print("\nvocê terá desconto")
                valor_final = valor_final
            else:
                print("\nvocê não terá desconto")

            produtos[numero_produto] = Produto(produtos[numero_produto].nome,produtos[numero_produto].preço)
            produtos[numero_produto].ExibirValor()
            print(f"O valor total ficou {str(valor_final).replace(".",",")}")

            while True:
                continuar_compra = input("\nvocê quer finalizar a compra? (S/N)")

                if continuar_compra.lower() == "s":
                    print("Finalizando compra ...")
                    break
                elif continuar_compra.lower() == "n":
                    print("Cancelando compra ...")
                    break
                else:
                    print("Erro:Digite apena S ou N")
                    continue

    elif menu == 4:
        print("Parando ...")
        break

    else:
        print("Erro: Digite apenas numero da opção")
        continue