from meu_grafo_matriz_adj_nao_dir import MeuGrafo

grafo = MeuGrafo()




# g_p = MeuGrafo()
# g_p.adiciona_vertice("J")
# g_p.adiciona_vertice("C")
# g_p.adiciona_vertice("E")
# g_p.adiciona_vertice("P")
# g_p.adiciona_vertice("M")
# g_p.adiciona_vertice("T")
# g_p.adiciona_vertice("Z")
# g_p.adiciona_aresta('a1', 'J', 'C')
# g_p.adiciona_aresta('a2', 'C', 'E')
# g_p.adiciona_aresta('a3', 'C', 'E')
# g_p.adiciona_aresta('a4', 'P', 'C')
# g_p.adiciona_aresta('a5', 'P', 'C')
# g_p.adiciona_aresta('a6', 'T', 'C')
# g_p.adiciona_aresta('a7', 'M', 'C')
# g_p.adiciona_aresta('a8', 'M', 'T')
# g_p.adiciona_aresta('a9', 'T', 'Z')

# for i in g_p.matriz_alcancabilidade():
#     print(i)


g_l1 = MeuGrafo()
g_l1.adiciona_vertice("A")
g_l1.adiciona_vertice("B")
g_l1.adiciona_vertice("C")
g_l1.adiciona_vertice("D")
g_l1.adiciona_aresta('a1', 'A', 'A')
g_l1.adiciona_aresta('a2', 'A', 'B')
g_l1.adiciona_aresta('a3', 'A', 'A')


for i in g_l1.matriz_alcancabilidade():
    print(i)

    
