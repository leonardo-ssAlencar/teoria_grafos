from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):


    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''

        vertices_nAdjacentes = set()
        for i in self.vertices:
            vertices = self.vertices.copy()
            vertices.remove(i)
            for j in self.arestas_sobre_vertice(i.rotulo):
    
             try:
                if self.arestas[j].v1 == i:
                  vertices.remove(self.arestas[j].v2)
                else:
                  vertices.remove(self.arestas[j].v1)
             except:
                pass

            for x in vertices:
                valor = str.format("{}-{}", i.rotulo, x.rotulo)
                vertices_nAdjacentes.add(valor)

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

    def arestas_sobre_vertice(self, V, dir=False):
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
            if not dir:
                if self.arestas[i].v1.rotulo == V or self.arestas[i].v2.rotulo == V: 
                    arestas.add(i)
            
            else:
                if self.arestas[i].v1.rotulo == V:
                    arestas.add(i)
            
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        return not self.ha_laco() and not self.ha_paralelas() and self.vertices_nao_adjacentes() == set()
    

    def djkstra(self, v_inicio : str, v_final: str):

        mDjkstra = dict()
        nao_examinados = []

        for i in self.vertices: #inicializa a tabela
            mDjkstra[i.rotulo] = {"peso" : 0 if i.rotulo == v_inicio else float("inf"), "permanente" : 1 if i.rotulo == v_inicio else 0, "anterior" : "" }
            nao_examinados.append(i.rotulo)

        
        v_atual = v_inicio # Aqui seria o w
        
        while v_atual != v_final: # Verifica se chegou ao destino
            
            menor = None
            for j in self.arestas_sobre_vertice(v_atual, True): # verifica as arestas
                
                arr = self.arestas[j]
                v1 = arr.v1
                v2 = arr.v2

                if v1 != v2: # descarta se for laço

                    
                    phi_r_w = mDjkstra[v1.rotulo]["peso"] + arr.peso # calcula o Phi
                    
                    if not mDjkstra[v2.rotulo]["permanente"] and  mDjkstra[v2.rotulo]["peso"] > phi_r_w: # verifica se necessita atualizar a tabela
                        mDjkstra[v2.rotulo]["peso"] = phi_r_w # atualiza o valor na tabela
                        mDjkstra[v2.rotulo]["anterior"] = v_atual # atualiza 
                    
                    if menor == None or mDjkstra[v2.rotulo]["peso"] < mDjkstra[menor]["peso"]:
                        menor = v2.rotulo
            
            

                
            if menor == None: return None

            mDjkstra[menor]["permanente"] = 1 # marca o vertice como já analisado

            v_atual = menor # atualiza W
            nao_examinados.remove(menor)

        i = v_final
        resultado = v_final

        print(mDjkstra)


        while i != v_inicio:
            resultado = mDjkstra[i]["anterior"] + " - " +resultado
            i = mDjkstra[i]["anterior"]

        return resultado

