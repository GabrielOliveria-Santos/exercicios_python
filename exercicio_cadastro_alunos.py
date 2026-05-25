def aluno_situaçao(nota):    # criando uma funçao
    if nota >= 7:    # se parâmetro for maior ou igual a 7 entra
        return "aprovado"    # retorna aprovado

    elif nota >=5 and nota < 7:    # se parâmetro for maior ou igual a 5 e menor que 7 entra
        return "recuperaçao"     # retorna recuperação
    else:    # se não for if nem elif entra
        return "reprovado"    # retorna reprovado

def media_final(nota):    # criando outra função
    media = sum(nota)/len(nota)    # variavel = soma todos os elementos do parâmetro e divide pela quantidade de elementos no parâmetro 
    return media    # retorna a variável media

def quantidade_situaçao(alunos):    #criando outra função
    aprovado = 0    # variavel aprovado é igual a 0
    recuperaçao = 0    # variavel recuperação é igual a 0
    reprovado = 0    # variavel reprovado é igual a 0

    for aluno in alunos:    # Para cada aluno que estiver dentro da lista alunos faça algo
        if aluno["nota"] >= 7:    # se nota do aluno for maior ou igual a 7 entra
            aprovado += 1    # variável aprovado aumenta o número em 1
        elif aluno["nota"] >=5 and aluno["nota"] < 7:    # e a nota do aluno for maior ou igual a 5 e menor que 7 entra
            recuperaçao += 1    # variavel recuperação aumenta em 1
        else:    # se não for if ou eles entra
            reprovado += 1    # variavel reprovado aumenta mais 1
    return aprovado,recuperaçao,reprovado    # retorna as variaveis aprovado,recuperaçao e reprovado

def maior_menor_nota(alunos):    # criando uma funçao para alunos com maior e menor nota
    maior = alunos[0]    # criando variavel e atribuindo o primeiro elemento(um dicionario)da lista alunos
    menor = alunos[0]    # criando variavel e atribuindo o primeiro elemento(um dicionario)da lista alunos

    for aluno in alunos:    # para cada aluno dentro da lista alunos faça algo
        if aluno["nota"] > maior["nota"]:    # se a nota do aluno for maior que a nota da variavel maior entra
            maior = aluno    # variavel maior recebe aluno
        if aluno["nota"] < menor ["nota"]:    #  se a nota do aluno for menor que a nota da variavel menor entra
            menor = aluno    # variavel menor recebe aluno
    return maior,menor    # retorna a variavel maior e menor

aluno_cadastro = []    # criando lista aluno_cadastro
notas = []    # criando lista notas
dados_aluno = []    # criando lista dados_aluno

while True:   # looping infinito

    cadastro = input("você quer cadastrar um aluno? (S/N)")    # variavel cadastro recebe input
    if cadastro.lower() == "s":    # se cadastro minusculo for igual a s entra
        print("continuando ...")    # manda a mensagem para usuario

        while True:    #looping infinito
            try:    # faz o codigo, se dar erro vai para o except
                aluno = {   #criando dicionario
                    "nome": input("qual o nome do aluno? "),    # nome do dicionario recebe input
                    "idade": int(input("qual a idade do aluno? ")),    # idade do dicionario recebe input
                    "nota": float(input("qual a nota do aluno? "))    # nota do dicionario recebe input
                }    #fecha o dicionario
            except ValueError:    # se o erro do codigo for de converssao de tipos de dados entra
                print("Erro: digite o valor correto")    #manda a mensagem para o usuario
                continue    #volta para o inicio do looping
            try:   #faz o codigo, se der erro vai para o execept
                float(aluno["nome"])   # tenta transformar o nome em float
                print("Erro: o nome esta errado")   #informa o erro
                continue   #volta para o inicio do looping
            except:    # se der erro no try entra no except
                if aluno["nota"] < 0 or aluno["nota"] > 10:    #se nota do aluno for menor que 0 e maior que 10 entra
                    print("Erro: a nota deve ser um numero entre 0 e 10")    #manda a mensagem para usuario
                    continue    #volta para o inicio do loping
                elif aluno["idade"] <= 0:    #se idade do aluno for menor o igual a 0 entra
                    print("Erro: a idade tem que ser maior que 0")    #manda a mensagem para o usuario
                    continue    #volta para o inicio do looping
                break    #sai do looping

        nota1 = str(aluno["nota"]).replace(".",",").strip()    #variavel recebe a nota do aluno convertido para string, troca "." por "," e tira os espaços
        nota = aluno["nota"]    #nota recebe nota do aluno
        notas.append(nota)    # adiciona a variavel nota para a lista notas
        aluno_cadastro.append(aluno)    #adiciona o dicionario aluno para a lista aluno_cadastro
        aluno_idade = str(aluno["idade"]).strip()    #variavel recebe idade o dicionario aluno, transforma em string e tira os espaços
        aluno_nome = aluno["nome"].strip()    #variavel recebe nome o dicionario aluno e tira os espaços
        dados_aluno.append(f"nome: {aluno_nome} | idade: {aluno_idade} | nota: {nota1} | situaçao: {aluno_situaçao(nota)}") #adiciona nome, idade, nota e situaçao do aluno a lista

    elif cadastro.lower() == "n":    #se cadastro minusculo for igual a "n" entra
        print("parando ...")    #manda a mensagem para o usuario
        break    #sai do looping

    else:   # se nao for o if nem o elif entra
        print("Erro: digite apenas S ou N")    #manda a mensagem para o usuario
        continue   #volta para o inicio do looping

try:   #faz o codigo, se der erro faz o except
    media_alunos = str(media_final(notas)).replace(".",",")    #variavel recebe return da funçao que é transformada em string e troca "." por ","
    aprovado,recuperaçao,reprovado = quantidade_situaçao(aluno_cadastro)    #variaveis recebem os returns da funçao
    aluno_maior_nota, aluno_menor_nota = maior_menor_nota(aluno_cadastro)    #variaveis recebem os returns da funçao

    print("--Resultado--")   #manda a mensagem para o usuario
    for dados in dados_aluno:    #para dados em dados_alunos faz algo
        print(dados)   #manda os dados para o usuario
    print(f"media da turma: {media_alunos}")    #manda a mensagem com a variavel para o usuario
    print(f"aprovado: {aprovado}\nrecuperaçao: {recuperaçao}\nreprovado: {reprovado}")    #manda mensagems com a variaveis para o usuario
    print(f"aluno com maior nota: {aluno_maior_nota['nome'].strip()} - {str(max(notas)).replace('.',',')}")   #manda a mensagem com a variavel para o usuario e pega a maior nota transforma em string e troca "." por ","
    print(f"aluno com menor nota: {aluno_menor_nota['nome'].strip()} - {str(min(notas)).replace('.',',')}")   #manda a mensagem com a variavel para o usuario e pega a menor nota transforma em string e troca "." por ","

except:# se der erro no try entra no except
    print("")    #manda nada ao usuario