from collections import deque
# Input:
# a-> b,c 
# b -> d,e
# c -> f,g
# Objetivo: recorrer el algoritmo

# def BFS(grafo):
#     V = len(grafo)
#     res = []
#     s = 0
#     q = deque()
#     visitado = [False] * V
#     visitado[s] = True
#     q.append(s)
#     while q:
#         curr = q.popleft()
#         res.append(curr)
#         for x in grafo[curr]:
#             if not visitado:
#                 # append
#                 visitado[x]=True
#                 q.append(x)
#     return res
# BFS()

grafo_ej = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}


# Escribir una función que realice la búsqueda en anchura. 
# La función debe recibir como entrada el grafo y un nodo inicial
# devolver el ordne de visita de los nodos
from collections import deque

def BFS2(grafo,nodo_raiz):
    len_grafo = len(grafo)
    res = []
    q = deque()
    frontier = []
    # nodo explorado / ninguno explorado al iniciar
    explored = [False] * len_grafo
    # tengo que asignar el nodo_raiz como 1.- nodo de partida 2.- nodo explorado
    explored[nodo_raiz] = True
    q.append(nodo_raiz)
    
    while q:
        frontier = q.popleft() #
        res.append(frontier) #pero que pasa si hay múltiples?
        for x in grafo[frontier]:
            






    return res

