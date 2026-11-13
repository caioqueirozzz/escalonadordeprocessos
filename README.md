# Escalonador de Processos

Simulador dos algoritmos de escalonamento **FCFS**, **SJF** e **Round Robin** (quantum = 2).


## Como rodar

```bash
python3 escalonador.py <arquivo_de_entrada>
```


## Formato do arquivo de entrada

Cada linha representa um processo com dois valores separados por espaço:

```
<tempo_de_chegada> <duração_de_CPU>
```

Exemplo (`entrada1.txt`):
```
0 10
4 4
8 6
21 8
```

## Saída

O programa imprime as médias de **tempo de retorno**, **tempo de resposta** e **tempo de espera** para cada algoritmo:

```
FCFS <retorno> <resposta> <espera>
SJF  <retorno> <resposta> <espera>
RR   <retorno> <resposta> <espera>
```

Os valores usam vírgula como separador decimal. Exemplo:

```
FCFS 17,0 7,0 7,0
SJF 14,5 4,5 4,5
RR 18,5 3,5 8,5
```