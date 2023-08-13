import random

def gera_dados_aleatorios(num_clausulas, num_variaveis, tamanho_medio_clausula):
    dados = []

    for _ in range(num_clausulas):
        tamanho_clausula = random.randint(1, tamanho_medio_clausula * 2)
        clausula = []

        for _ in range(tamanho_clausula):
            variavel = random.randint(1, num_variaveis)
            if random.random() < 0.5:
                variavel = -variavel
            clausula.append(variavel)

        dados.append(clausula)

    return dados

def escreve_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for clausula in dados:
            linha = ' '.join(map(str, clausula)) + ' 0\n'
            arquivo.write(linha)

def main():
    num_clausulas = 10000
    num_variaveis = 500
    tamanho_medio_clausula = 3
    nome_arquivo = 'dados_dpll.txt'

    dados = gera_dados_aleatorios(num_clausulas, num_variaveis, tamanho_medio_clausula)
    escreve_arquivo(dados, nome_arquivo)

if __name__ == "__main__":
    main()
