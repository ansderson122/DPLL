import copy

def carregaDados(PATH):
    dados = []
    try:
        with open(PATH, 'r') as entrada:
            for linhas in entrada:
                if linhas[0] == "p": continue
                clausula = linhas.split()
                clausula = [int(literal) for literal in clausula if literal != "0\n"]
                dados.append(clausula)

    except FileNotFoundError:
        print(f"Arquivo '{PATH}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return dados

def simplifica(f :list, a:int)-> list:
    #print(f)
    #print("res : " + str(res))
    global dados,res
    for clausula in reversed(f):
        for literal in clausula:
            if a == literal:
                f.remove(clausula)
                break
            elif -a == literal:
                clausula.remove(literal)
                if satisfativel(f):
                    if len(clausula) == 0: # clausala vazia 
                        f = copy.deepcopy(dados)
                        res.remove(a)
                        res.append(-a)
                        print(-a)
                        f = simplifica(f,-a)
                        return f
                else:
                    return f

    dados = copy.deepcopy(f)
    return f
    

  
            
def satisfativel(f:list)->bool:
      # testa se ha duas clausulas unitaria com sinais diferente 
    for i in range(len(f)):
        for j in range(i+1,len(f)):
            if len(f[i]) == 1 and len(f[j]) == 1:
                if f[i][0] == -f[j][0]:
                    return False
    return True
       
# a variavel 'a' é a suposição inicical 
def DPLL(PATH = 'entrada.txt',a = 10):
    res = []
    dados = carregaDados(PATH)
    res.append(a) 
    f = copy.deepcopy(dados)
    continua = True

    #print("res : " + str(res))
    #print(f)

    f = simplifica(f,res[0])
    while continua:
        #print("res : " + str(res))
        #print(f)
        #input()

        
        unit = 0 # numero de clausula unitarias 
        # elimina clausula unitarias 
        for clausula in f:
            if len(clausula) == 1:
                unit+=1
                res.append(clausula[0])
                f = simplifica(f, clausula[0])
                if not satisfativel(f):
                    print("É insatisfativel")
                    
                    print(f)
                    continua = False
                    break 

        # se não existe clausual unitarias 
        if unit == 0 and len(f) >= 1:
            res.append(f[0][0]) # aqui pode se escolhe uma valor a partir de uma função
            f = simplifica(f, f[0][0])
            continue      

        if len(f) == 0:
            print("É satisfativel")
            continua = False
    
    print("res : " + str(res))
    


if __name__ == "__main__":
    DPLL()