from DPLL import DPLL
from gera import geraTxtDados
import time

num_clausulas = 50000
num_variaveis = 500
tamanho_medio_clausula = 10

geraTxtDados(num_clausulas,num_variaveis,tamanho_medio_clausula)

inicio = time.time()
DPLL("dados_dpll.txt")
fim = time.time()

tempo_decorrido = fim - inicio

print(f"Tempo decorrido: {tempo_decorrido:.4f} segundos")
print("Com uma entrada de {} clausulas e {} variaveis, com o  tamanho medio clausula {}".format(num_clausulas,num_variaveis,tamanho_medio_clausula))