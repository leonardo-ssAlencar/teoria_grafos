from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_arestas(self):

        arestas_vertices = {}
        for i in self.vertices:
            arestas = []
            for j in self.arestas:
                if self.arestas[j].v1 == i or self.arestas[j].v2 == i:
                    arestas.append(self.arestas[j])

        arestas_vertices[i.rotulo] = arestas

        return arestas_vertices



    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''

        vertices_nAdjacentes = set()

        arestasV = self.vertices_arestas()


        for i in arestasV:
            for j in self.vertices:
                if arestasV[i].v1 == j or arestasV[i].v2 == j:
                    segundo = str
                    if arestasV[i].v1 == j:
                        vertices_nAdjacentes.add(i + "-" + segundo)
                    else:
                        vertices_nAdjacentes.add(i + "-" + segundo)
        return vertices_nAdjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        for i in self.arestas:

            if self.arestas[i].v1 == self.arestas[i].v2:
                return True

        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        existeVertice = False

        for i in self.vertices:
            if i.rotulo == V:
                existeVertice = True
                break

        if existeVertice is False:
            raise VerticeInvalidoError

        grau = 0
        for i in self.arestas:
            verVertice1 = self.arestas[i].v1.rotulo == V
            verVertice2 =  self.arestas[i].v2.rotulo == V

            if verVertice1 or verVertice2:
                grau+=1

                if self.arestas[i].v1 == self.arestas[i].v2:
                    grau+=1

        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in self.arestas:
            v1 = self.arestas[i].v1
            v2 = self.arestas[i].v2
            for j in self.arestas:
                if i == j:
                    continue

                v3 = self.arestas[j].v1
                v4 = self.arestas[j].v2
                if (v1 == v3 or v1 == v4) and (v2 == v3 or v2 == v4):
                    return True

        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        arestas = set()

        temVertice = False

        for i in self.vertices:
             if i.rotulo == V:
                 temVertice = True

        if not temVertice:
            raise VerticeInvalidoError

        for i in self.arestas:
            if self.arestas[i].v1.rotulo == V or self.arestas[i].v2.rotulo == V:
                arestas.add(i)
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        return not self.ha_laco() and not self.ha_paralelas() and self.vertices_nao_adjacentes() == set()

    def dfs(self,V):

        self.get_vertice(V)

        nosVisitados = MeuGrafo()

        self.proximo_vertice(V,None, nosVisitados)


        return nosVisitados

    def proximo_vertice(self, V, aresta, arvore):
        if self.get_vertice(V) in arvore.vertices:
            return

        # No caso do vertice raiz

        arvore.adiciona_vertice(V)
        if aresta is not None:
            arvore.adiciona_aresta(aresta.rotulo, aresta.v1.rotulo, aresta.v2.rotulo)

        for i in self.arestas_sobre_vertice(V):
            if i not in arvore.arestas.keys():
                a = self.arestas[i]
                proximo = ""

                if a.v1.rotulo != V:
                    proximo = a.v1.rotulo
                else:
                    proximo = a.v2.rotulo

                self.proximo_vertice(proximo, a, arvore)

        return

    def bfs(self, V):

        arvore = MeuGrafo()
        
        arvore.adiciona_vertice(V)
        
        self.bfs_prox(V, arvore)
        return  arvore

    def bfs_prox(self, V, arvore):

        proximos_vertices = []
        for i in self.arestas_sobre_vertice(V):
            aresta = self.arestas[i]

            vertice = aresta.v1 if aresta.v1.rotulo != V else aresta.v2

            if vertice not in arvore.vertices:
                proximos_vertices.append(vertice)
                arvore.adiciona_vertice(vertice.rotulo)
                arvore.adiciona_aresta(aresta.rotulo, aresta.v1.rotulo, aresta.v2.rotulo)
        
        for i in proximos_vertices:
            self.bfs_prox(i.rotulo, arvore)


    def conexo(self):

        arvore = self.bfs(self.vertices[0].rotulo)

        return len(arvore.vertices) == len(self.vertices)
    
 
    def caminho(self, v1, v2):
        
        arvore = self.dfs(v1)

        arvore.get_vertice(v2)

        caminho = []

        caminho.append(v1)
        prox_vertice = v1
        for i in arvore.arestas:
            aresta = arvore.arestas[i]
            
            prox_vertice = aresta.v1.rotulo if aresta.v1.rotulo != prox_vertice else aresta.v2.rotulo
            
            caminho.append(aresta.rotulo)
            caminho.append(prox_vertice)

            if aresta.v2.rotulo == v2:
                break
        
        return caminho, arvore


