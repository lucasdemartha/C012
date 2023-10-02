#Lucas Ribeiro de Martha
#Luiza Ribeiro de Martha
#Leonardo Teodoro de Oliveira

import queue
import time

# Classe que representa um processo com nome, tempo de chegada e tempo de execução.
class Processo:
    def __init__(self, nome, tempo_chegada, tempo_execucao):
        self.nome = nome                   # Nome do processo
        self.tempo_chegada = tempo_chegada # Tempo de chegada do processo
        self.tempo_execucao = tempo_execucao # Tempo de execução do processo

# Função para simular o escalonamento FCFS.
def simular_fcfs(processos):
    fila_pronto = queue.Queue()       # Fila de pronto (READY QUEUE)
    tempo_atual = 0                 # Tempo atual
    tempos_retorno = []             # Lista para armazenar os tempos de retorno dos processos

    for processo in processos:
        while tempo_atual < processo.tempo_chegada:
            tempo_atual += 1
        print(f"Executando {processo.nome} (Tempo de Execucao: {processo.tempo_execucao}) no tempo {tempo_atual}")
        tempo_atual += processo.tempo_execucao  # Simula a execução do processo
        tempo_retorno = tempo_atual - processo.tempo_chegada  # Calcula o tempo de retorno do processo
        tempos_retorno.append(tempo_retorno)  # Armazena o tempo de retorno na lista

    tempo_medio_retorno = sum(tempos_retorno) / len(tempos_retorno)
    print(f"Tempo Medio de Retorno: {tempo_medio_retorno}")

if __name__ == "__main__":
    # Exemplo de processos: (Nome, Tempo de Chegada, Tempo de Execução)
    processos = [
        Processo("P1", 0, 8),
        Processo("P2", 1, 4),
        Processo("P3", 2, 9),
        Processo("P4", 3, 5),
    ]

    print("Simulando Escalonamento FCFS:")
    simular_fcfs(processos)