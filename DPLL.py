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
    #print("res : " + str(res))
    #print(f)
    #input()

    for clausula in reversed(f):
        for literal in clausula:
            if a == literal:
                f.remove(clausula)
                break
            elif -a == literal:
                clausula.remove(literal)
    return f
              
def satisfativel(f:list)->bool:
    # testa se ha duas clausulas unitaria com sinais diferente 
    for i in range(len(f)):
        for j in range(i+1,len(f)):
            if len(f[i]) == 1 and len(f[j]) == 1:
                if f[i][0] == -f[j][0]:
                    print("Existe f[{}] = {} e f[{}] = {}".format(i,f[i],j,f[j]))
                    return False
    return True
       
# a variavel 'a' é a suposição inicical 
def DPLL(PATH = 'entrada.txt',a = 10):
    global res
    res = []
    
    dados = carregaDados(PATH)
    res.append(a) 
    f = copy.deepcopy(dados)
    continua = True
    tentativa = 1

    f = simplifica(f,res[0])
    while continua: 
        unit = 0 # numero de clausula unitarias 
        # elimina clausula unitarias 
        if not satisfativel(f):
            if tentativa == 1:
                f = copy.deepcopy(dados)
                x = res[len(res)-1]
                res.remove(x)
                res.append(-x)
                f = simplifica(f,-x)
                tentativa += 1
            else:
                print("É insatisfativel")
                continua = False
                break 
        else:
            tentativa = 1

        dados = copy.deepcopy(f)

        for clausula in f:
            if len(clausula) == 1:
                unit+=1
                res.append(clausula[0])
                f = simplifica(f, clausula[0])

        for clausula in f:
            if len(clausula) == 0: # clausala vazia 
                f = copy.deepcopy(dados)
                x = res[len(res)-1]
                res.remove(x)
                res.append(-x)
                f = simplifica(f,-x)

        # se não existe clausual unitarias 
        if unit == 0 and len(f) >= 1 and len(f[0]) >= 1:
            res.append(f[0][0]) # aqui pode se escolhe uma valor a partir de uma função
            f = simplifica(f, f[0][0])      

        if len(f) == 0:
            print("É satisfativel")
            continua = False
        
    
    #print("res : " + str(res))
    return res
if __name__ == "__main__":
    DPLL()