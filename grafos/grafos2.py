class Vertice:
    def __init__(self,i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.vecinos = []

    def agregarVecino(self, n): #n de neighbor
        if v not in self.vecinos:
            self.vecinos.append(n)


class Grafica:
    def __init__(self):
        self.vertices = {}


    def agregarVertice(self, v): #v de vertice
        if v not in self.vertices:
            self.vertices[v] = Vertice(v) #crear llave = valor (objeto de tipo vertice con el identificar v)
            
    # no direccionado
    def agregarAristas(self,a,b): #los 2 vertices que seran unidos
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b)
            self.vertices[b].agregarVecino(a)
            
        
def main():
    g = Grafica()

    lista = [0,1,2,3,4,5,6]

    for v in lista:
        g.agregarVertice(v)


    lista = [2,0,0,6,6,3,0,5,6,5,0,1,6,4,1,4]
    for i in range(0,len(lista)-1,2):
        g.agregarArista(lista[i], lista[i+1])

    for v in g.vertices:
        print(v,g.vertices[v].vecinos)


main()