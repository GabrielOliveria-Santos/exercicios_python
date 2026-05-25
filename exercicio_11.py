nota = float(input("qual a sua nota? "))
if nota >= 7:
    print("aprovado")
elif nota >= 5 and nota < 7:
    print("recuperação")
else:
    print("reprovado")