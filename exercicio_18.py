def valor_quantidade(n1,n2):
    return n1 * n2
valor = float(input("qual o valor  do produto? "))
quantidade = int(input("qual a quantidade de produtos? "))
total_pagar = valor_quantidade(valor,quantidade)
print(total_pagar)