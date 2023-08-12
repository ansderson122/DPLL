
PATH = 'entrada.txt'


dados = []
res = []

with open(PATH, 'r') as entrada:
    for linhas in entrada:
        if linhas[0] == "p": continue
        clausula = linhas.split(" ")
        clausula = [int(literal) for literal in clausula if literal != "0\n"]
        dados.append(clausula)

def simplifica(f :list, a:int)-> None:
    for clausula in reversed(f):
        for literal in clausula:
            if a == literal:
                f.remove(clausula)
                break
            elif -a == literal:
                clausula.remove(literal)
    
    print(f)
    for clausula in f:
        if len(clausula) == 1:
            res.append(clausula[0])
            simplifica(f, clausula[0])



def DPLL():
    res.append(10) #aqui dever ser chamado uma função para escolhe um literal
    simplifica(dados,res[0])
    print("res : " + str(res))


if __name__ == "__main__":
    DPLL()