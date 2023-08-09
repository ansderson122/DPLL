
PATH = 'entrada.txt'


dados = []

with open(PATH, 'r') as entrada:
    for linhas in entrada:
        if linhas[0] == "p": continue
        clausula = []
        for literal in linhas.split(" "):
            if int(literal) != 0: clausula.append(int(literal))
        dados.append(clausula)

print(dados)