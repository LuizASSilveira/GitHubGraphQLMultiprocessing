from multiprocessing import Process, Manager, current_process

from src.querys import Query
from ctypes import c_char_p
import requests
import time
import sys
import json

headers = {"Authorization": 'Bearer {0}'.format(sys.argv[1])}


def apiGitRequest(query, variables):
    request = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables},
                            headers=headers, timeout=30)
    if request.status_code == 200:
        return json.loads(request.content.decode('utf-8'))
    else:
        return None


def Produtor(lockBuffer, buffer, nameProject):
    owner, name = nameProject.split('/')
    queryVariables = {
        "owner": owner,
        "name": name
    }
    after = ''
    while True:
        query = Query.queryRepCommits(after),
        query = query[0]
        req = apiGitRequest(query, queryVariables)
        data = req['data']['repository']['defaultBranchRef']['target']['history']['nodes']

        try:
            lockBuffer.acquire()
            for d in data:
                buffer[name].append(d)
        finally:
            lockBuffer.release()
            print(name + ' ---> ' + current_process().name + ' Pruduzindo +100')

        pageInfo = req['data']['repository']['defaultBranchRef']['target']['history']['pageInfo']
        if not pageInfo['hasNextPage']:
            break
        after = pageInfo['endCursor']


def Consumer(lockBuffer, lockNameUsers, name, buffer, nameUsers, endProducer):
    while True:
        #  Manipula lockBuffer
        lockBuffer.acquire()
        data = buffer[name].pop() if len(buffer[name]) >= 1 else ''
        lockBuffer.release()

        if len(data):
            if not data['author']['user']:  # Caso de nao possua author
                continue
            # print(name + ' ---> ' + current_process().name + ' Consumindo')
            nameUser = data['author']['user']['login']

            #  Manipula Dicionario lockNameUsers
            lockNameUsers.acquire()
            if nameUser not in nameUsers[name].keys():
                nameUsers[name][nameUser] = 1
            else:
                nameUsers[name][nameUser] += 1
            lockNameUsers.release()
        else:
            if endProducer:  # Termina se não existe mais produtor
                break


if __name__ == '__main__':

    numberProduter = 1  # qtd de consumidores por produtor
    numberConsumers = 2  # qtd de consumidores por produtor

    inicio = time.time()
    with Manager() as manager:
        nameUsers = manager.dict(
            {'laravel': manager.dict(), 'vscode': manager.dict()})  # nome dos desenvolvedores por projetos
        buffer = manager.dict(
            {'laravel': manager.list(), 'vscode': manager.list()})  # nome dos desenvolvedores por projetos
        # projects = manager.list(['laravel/laravel', 'microsoft/vscode'])# listas dos projetos a serem analizados

        array = ['laravel/laravel', 'microsoft/vscode']

        lockBuffer = manager.Lock()
        lockNameUsers = manager.Lock()
        endProducer = manager.Value('i', 0)
        listOfProducers = []
        listOfConsumers = []
        auxNumberProduter = 0  # controla a posição da lista de Produtor
        auxNumberConsumers = 0  # controla a posição da lista de consumer

        inicio = time.time()
        for i, name in enumerate(array):
            nameProject = name.split('/')[1]

            for nCons in range(numberProduter):
                listOfProducers.insert(auxNumberProduter, Process(target=Produtor, args=(lockBuffer, buffer, name)))
                listOfProducers[auxNumberProduter].start()
                auxNumberProduter += 1

            time.sleep(1)

            for nCons in range(numberConsumers):
                listOfConsumers.insert(auxNumberConsumers, Process(target=Consumer, args=(
                    lockBuffer, lockNameUsers, nameProject, buffer, nameUsers, endProducer)))
                listOfConsumers[auxNumberConsumers].start()
                auxNumberConsumers += 1

            for prod in listOfProducers:
                prod.join()
            endProducer.set(1)

            for cons in listOfConsumers:
                cons.join()

        fim = time.time()
        print('Tempo de execução {}'.format(fim - inicio))

        for name in nameUsers.keys():
            print(nameUsers[name])
