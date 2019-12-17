# GitHubGraphQLMultiprocessing

O projeto tem como objetivo testar algumas formas de execução paralela em python 3 para a realização de requisições mais eficientes atravez da api GitHub. Como o tempo de resposta da Api do GitHub depende da complexidade da consulta a ser relizado projetos que utilizam da mesma para minerar grandes volumes de dados perdem muito tempo de tempo de processamento da maquina que esta utilizada.

### Biblioteca
  multiprocessing
  

### Configurações da Máquina
  * Processador: Intel(r) Core(TM) i5-5200U |
  * Memoria (RAM): 8,00GB |
  * SO: Windows 10 |
  
  
| Número de processos | Tempo de execução  | Speedup            |
|---------------------|--------------------|--------------------|
| 1                   | 1038.1795041561127 |                    |
| 2                   | 518.6191303730011  | 2.0018149029894703 |
| 3                   | 548.2239379882812  | 1.8937142875696622 |
| 4                   | 541.9422702789307  | 1.9156643817832757 |
| 6                   | 445.7503414154053  | 2.329060480042591  |
