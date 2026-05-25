def verificação_idade ():
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"
idade = int(input("qual é a sua idade? "))
maior_ou_menor_idade = verificação_idade()
print(maior_ou_menor_idade)