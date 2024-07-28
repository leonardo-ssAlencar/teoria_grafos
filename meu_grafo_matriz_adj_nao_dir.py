from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''
        
        conjunto = set()
        for i in range(len(self.arestas)):
            for j in range(len(self.arestas)):
                if i == j: break
                if self.arestas[i][j] == {}:
                    val = self.vertices[j].rotulo+"-"+self.vertices[i].rotulo
                    conjunto.add(val)
                
                    
        return conjunto
        
     

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.arestas)):
            if self.arestas[i][i] != {}: 
                return True
        
        return False
            

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        vertice = self.get_vertice(V)
        if not vertice:
            raise VerticeInvalidoError
        
        grau = 0
        cont = 0
        for i in self.vertices:
            if i == vertice:
                for j in range(len(self.arestas)):
                    arestas = self.arestas[cont][j]
                    if len(arestas) > 0:
                        for k in arestas:
                            ar = self.get_aresta(k)
                            if ar.v1 == ar.v2:
                                grau+=1
                            grau+=1
                break
            cont+=1
        
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        
        for i in range(len(self.arestas)):
            for j in range(len(self.arestas)):
                if len(self.arestas[i][j]) > 1:
                    return True
        return False
    
    
    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        
        vertice = self.get_vertice(V)
        if not vertice:
            raise VerticeInvalidoError
        
        arestas = set()
        cont = 0
        for i in self.vertices:
            if i == vertice:
                for i in range(len(self.vertices)):
                   a = self.arestas[cont][i]
                   for i in a:
                       arestas.add(i)
                break 
            cont+=1
        
        
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        return not self.ha_laco() and not self.ha_paralelas() and self.vertices_nao_adjacentes() == set()
    

    def warshall(self): 

        nGrafo = list()
        tam =len(self.arestas)

        maxVal = 99
        

        for i in range(tam): 
            linha = list()
            for j in range(tam):
                if self.arestas[i][j] != {}:
                    linha.append(self.get_aresta(list(self.arestas[i][j].keys())[0]).peso)
                else:
                    linha.append(0 if i == j else maxVal)
            nGrafo.append(linha)        


        for k in range(tam):
            for i in range(tam):
                    for j in range(tam):
                            sum = nGrafo[i][k] + nGrafo[k][j]
        
                            if nGrafo[i][j] > sum:
                                nGrafo[i][j] = sum
        
        for i in range(tam):
            for j in range(tam):
                if nGrafo[i][j] == maxVal:
                    nGrafo[i][j] = "inf"

        return nGrafo
    
    def matriz_alcancabilidade(self):
        matriz = self.warshall()

        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz[i][j] == "inf":
                    matriz[i][j] = 0
                else:
                    matriz[i][j] = 1


        return matriz


        


        
                        
                            



            

                
        