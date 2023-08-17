import copy

def carregaDados(PATH):
    dados = []
    numLinhas = 0
    try:
        with open(PATH, 'r') as entrada:
            for linhas in entrada:
                if linhas[0] == "p": 
                    linhas1 = linhas.split(" ")
                    numLinhas = linhas1[3]
                    continue
                clausula = linhas.split(" ")
                clausula = [int(literal) for literal in clausula if literal != "0\n" and literal != ""]
                dados.append(clausula)
    except FileNotFoundError:
        print(f"Arquivo '{PATH}' não encontrado.")
        return e
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return e
    return dados

def simplifica(f :list, a:int)-> list:
    #print("res : " + str(res)) # removar o comentário para debug 1/4

    for clausula in reversed(f):
        for literal in clausula:
            if a == literal:
                f.remove(clausula)
                break
            elif -a == literal:
                clausula.remove(literal)
    #print(f) # removar o comentário para debug 2/4
    #input() # removar o comentário para debug 3/4
    return f
              
def satisfativel(f:list)->bool:
    # testa se ha duas clausulas unitaria com sinais diferente 
    # e clausala vazia 
    for i in range(len(f)):
        if len(f[i]) == 0:
            return False
        for j in range(i+1,len(f)):
            if len(f[i]) == 1 and len(f[j]) == 1:
                if f[i][0] == -f[j][0]:
                    return False
    return True
       
# a variavel 'a' é a suposição inicical 
def DPLL(dados,res = []): 
    f = copy.deepcopy(dados)

    unit = 0 # numero de clausula unitarias 
    # elimina clausula unitarias  
    for clausula in f:
        if len(clausula) == 1:
            unit+=1
            res.append(clausula[0])
            f = simplifica(f, clausula[0])
            break

    # se não existe clausual unitarias 
    if unit == 0 and len(f) >= 1 and len(f[0]) >= 1:
        res.append(f[0][0]) # aqui pode se escolhe uma valor a partir de uma função
        f = simplifica(f, f[0][0])      

    if len(f) == 0:
        print("É satisfativel")
        return True

    if not satisfativel(f):
        f = copy.deepcopy(dados)
        x = res[len(res)-1]
        res.remove(x)
        res.append(-x)
        f = simplifica(f,-x)
        if not satisfativel(f):
            print("É insatisfativel")
            return False
                
    #print("res : " + str(res))
    return DPLL(f,res)

if __name__ == "__main__":
    res = []
    PATH = 'entrada.txt'
    dados = carregaDados(PATH)
    DPLL(dados,res)
    print("res : " + str(res))