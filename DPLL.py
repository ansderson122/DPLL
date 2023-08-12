import copy
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
    global dados
    for clausula in reversed(f):
        for literal in clausula:
            if a == literal:
                f.remove(clausula)
                break
            elif -a == literal:
                clausula.remove(literal)
                if len(clausula) == 0: # clausala vazia 
                    f = copy.deepcopy(dados)
                    res.remove(a)
                    res.append(-a)
                    simplifica(f,-a)
                    return

    dados = copy.deepcopy(f)
    print(f)

    # testa se ha duas clausulas unitaria com sinais diferente 
    for i in range(len(f)):
        for j in range(i+1,len(f)):
            if len(f[i]) > 1: # não uma clausula unitaria 
                continue
            if len(f[j]) > 1:
                continue

            if f[i][0] == -f[j][0]:
                print("É insatisfativel")
                return
            
        
       
    for clausula in f:
        if len(clausula) == 1:
            res.append(clausula[0])
            simplifica(f, clausula[0])
        



def DPLL():
    res.append(4) #aqui dever ser chamado uma função para escolhe um literal
    f = copy.deepcopy(dados)
    continua = True
    
    simplifica(f,res[0])
    

    print("res : " + str(res))


if __name__ == "__main__":
    DPLL()