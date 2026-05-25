class Produto:
    def __init__(self,nome,preço):
        self.nome = nome
        self.preço = preço

    def InformaçoesDoProduto(self):
        print(f"nome: {self.nome}\npreço: {self.preço}")

Produto1 = Produto("arroz","18,99")
print(Produto1.nome,Produto1.preço)
Produto1.ExibirInformaçoesDoProduto()