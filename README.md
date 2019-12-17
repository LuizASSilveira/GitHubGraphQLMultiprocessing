# GitHubGraphQLMultiprocessing

O projeto tem como objetivo testar algumas formas de execução paralela em python 3 para a realização de requisições mais eficientes atravez da api GitHub. Como o tempo de resposta da Api do GitHub depende da complexidade da consulta a ser relizado projetos que utilizam da mesma para minerar grandes volumes de dados perdem muito tempo de tempo de processamento da maquina que esta utilizada.

### Biblioteca
  multiprocessing
  

### Configurações da Máquina
  * Processador: Intel(r) Core(TM) i5-5200U
  * Memoria (RAM): 8,00GB
  * SO: Windows 10
  
  
| Número de processos | Tempo de execução (min)  | Speedup      |
|---------------------|--------------------|--------------------|
| 1                   | 17,3               |                    |
| 2                   | 8,6                | 2.0018149029894703 |
| 3                   | 9,13               | 1.8937142875696622 |
| 4                   | 9,0                | 1.9156643817832757 |
| 6                   | 7,42               | 2.329060480042591  |
