import sys
import copy

class Processo:
    def __init__(self, pid, chegada, duracao):
        self.pid      = pid      
        self.chegada  = chegada   
        self.duracao  = duracao   
        self.restante = duracao   
        self.inicio   = -1        
        self.fim      = -1        


def media(soma, n):
    return soma / n


def fcfs(processos, n):
    procs = copy.deepcopy(processos)
    procs.sort(key=lambda p: (p.chegada, p.pid))

    t = 0
    tretorno = tresposta = tespera = 0

    for p in procs:
        if t < p.chegada:              
            t = p.chegada

        p.inicio = t
        p.fim    = t + p.duracao
        t        = p.fim

        retorno  = p.fim    - p.chegada
        resposta = p.inicio - p.chegada
        espera   = retorno  - p.duracao

        tretorno  += retorno
        tresposta += resposta
        tespera   += espera

    return tretorno, tresposta, tespera



def sjf(processos, n):
    procs     = copy.deepcopy(processos)
    executado = [False] * n

    t = 0
    tretorno = tresposta = tespera = 0
    concluidos = 0

    while concluidos < n:
        disponiveis = [i for i in range(n)
                       if not executado[i] and procs[i].chegada <= t]

        if not disponiveis:
            t = min(procs[i].chegada for i in range(n) if not executado[i])
            continue

        idx = min(disponiveis,
                  key=lambda i: (procs[i].duracao, procs[i].chegada, i))

        p        = procs[idx]
        p.inicio = t
        p.fim    = t + p.duracao
        t        = p.fim
        executado[idx] = True
        concluidos    += 1

        retorno  = p.fim    - p.chegada
        resposta = p.inicio - p.chegada
        espera   = retorno  - p.duracao

        tretorno  += retorno
        tresposta += resposta
        tespera   += espera

    return tretorno, tresposta, tespera



def roundRobin(processos, n, quantum=2):
    procs      = copy.deepcopy(processos)
    adicionado = [False] * n   
    fila       = []            

    t = 0
    tretorno = tresposta = tespera = 0
    concluidos = 0

    for i in range(n):
        if procs[i].chegada <= t:
            fila.append(i)
            adicionado[i] = True

    if not fila:
        t = procs[0].chegada
        for i in range(n):
            if procs[i].chegada <= t:
                fila.append(i)
                adicionado[i] = True

    while concluidos < n:

        if not fila:
            t = min(procs[i].chegada for i in range(n) if not adicionado[i])
            for i in range(n):
                if not adicionado[i] and procs[i].chegada <= t:
                    fila.append(i)
                    adicionado[i] = True
            continue

        idx = fila.pop(0)
        p   = procs[idx]

        if p.inicio == -1:
            p.inicio = t

        exec_time      = min(quantum, p.restante)
        t_fim_quantum  = t + exec_time
        p.restante    -= exec_time


        for i in range(n):
            if not adicionado[i] and procs[i].chegada <= t_fim_quantum:
                fila.append(i)
                adicionado[i] = True

        t = t_fim_quantum

        if p.restante == 0:
            p.fim = t
            concluidos += 1

            retorno  = p.fim    - p.chegada
            resposta = p.inicio - p.chegada
            espera   = retorno  - p.duracao

            tretorno  += retorno
            tresposta += resposta
            tespera   += espera
        else:
            fila.append(idx)

    return tretorno, tresposta, tespera



def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "entrada.txt"

    processos = []
    with open(filename, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            partes  = linha.split()
            chegada = int(partes[0])
            duracao = int(partes[1])
            processos.append(Processo(len(processos), chegada, duracao))

    n = len(processos)

    tretornoFCFS, trespostaFCFS, tesperaFCFS = fcfs(processos, n)
    tretornoSJF,  trespostaSJF,  tesperaSJF  = sjf(processos, n)
    tretornoRR,   trespostaRR,   tesperaRR   = roundRobin(processos, n)

    tMretornoFCFS  = media(tretornoFCFS,  n)
    tMrespostaFCFS = media(trespostaFCFS, n)
    tMesperaFCFS   = media(tesperaFCFS,   n)

    tMretornoSJF   = media(tretornoSJF,   n)
    tMrespostaSJF  = media(trespostaSJF,  n)
    tMesperaSJF    = media(tesperaSJF,    n)

    tMretornoRR    = media(tretornoRR,    n)
    tMrespostaRR   = media(trespostaRR,   n)
    tMesperaRR     = media(tesperaRR,     n)

    def fmt(x):
        return f"{x:.1f}".replace('.', ',')

    print(f"FCFS {fmt(tMretornoFCFS)} {fmt(tMrespostaFCFS)} {fmt(tMesperaFCFS)}")
    print(f"SJF {fmt(tMretornoSJF)} {fmt(tMrespostaSJF)} {fmt(tMesperaSJF)}")
    print(f"RR {fmt(tMretornoRR)} {fmt(tMrespostaRR)} {fmt(tMesperaRR)}")


if __name__ == "__main__":
    main()
