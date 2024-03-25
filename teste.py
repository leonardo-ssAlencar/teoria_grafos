import meu_grafo_lista_adj


g_p = meu_grafo_lista_adj.MeuGrafo()
# g_p.adiciona_vertice("A")
# g_p.adiciona_vertice("B")
# g_p.adiciona_vertice("C")
# g_p.adiciona_vertice("D")
# g_p.adiciona_vertice("E")
# g_p.adiciona_vertice("F")
# g_p.adiciona_aresta('a1', 'A', 'B')
# g_p.adiciona_aresta('a2', 'B', 'C')
# g_p.adiciona_aresta('a3', 'C', 'D')
# g_p.adiciona_aresta('a4', 'D', 'B')
# g_p.adiciona_aresta('a5', 'D', 'E')
# g_p.adiciona_aresta('a6', 'B', 'F')

g_p.adiciona_vertice("J")
g_p.adiciona_vertice("C")
g_p.adiciona_vertice("E")
g_p.adiciona_vertice("P")
g_p.adiciona_vertice("M")
g_p.adiciona_vertice("T")
g_p.adiciona_vertice("Z")
g_p.adiciona_aresta('a1', 'J', 'C')
g_p.adiciona_aresta('a2', 'C', 'E')
g_p.adiciona_aresta('a3', 'C', 'E')
g_p.adiciona_aresta('a4', 'P', 'C')
g_p.adiciona_aresta('a5', 'P', 'C')
g_p.adiciona_aresta('a6', 'T', 'C')
g_p.adiciona_aresta('a7', 'M', 'C')
g_p.adiciona_aresta('a8', 'M', 'T')
g_p.adiciona_aresta('a9', 'T', 'Z')



# g_l1 = meu_grafo_lista_adj.MeuGrafo()
# g_l1.adiciona_vertice("A")
# g_l1.adiciona_vertice("B")
# g_l1.adiciona_vertice("C")
# g_l1.adiciona_vertice("D")
# g_l1.adiciona_aresta('a1', 'A', 'A')
# g_l1.adiciona_aresta('a2', 'A', 'B')
# g_l1.adiciona_aresta('a3', 'A', 'A')

v, a = g_p.caminho_entre_vertices("J", "Z")

print(v)
print(a)