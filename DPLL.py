
PATH = 'entrada.txt'


dados = []

with open(PATH, 'r') as entrada:
    for linhas in entrada:
        if linhas[0] == "p": continue
        clausula = linhas.split(" ")
        clausula = [int(literal) for literal in clausula if literal != "0\n"]
        dados.append(clausula)

def simplifica(f :list)-> None:
    #escolhe um literal 
    a = 10 #aqui dever ser chamado uma função para escolhe um literal

    for clausula in reversed(f):
        for literal in clausula:
            if a == literal:
                f.remove(clausula)
                break
            elif -a == literal:
                clausula.remove(literal)
  

simplifica(dados)
print(dados)