from meu_grafo_lista_adj import MeuGrafo


g_p = MeuGrafo()
g_p.adiciona_vertice("A")
g_p.adiciona_vertice("B")
g_p.adiciona_vertice("C")
g_p.adiciona_vertice("D")
g_p.adiciona_vertice("E")

g_p.adiciona_aresta("a1", "A", "B")
g_p.adiciona_aresta("a2", "A", "C")
g_p.adiciona_aresta("a3", "C", "D")
g_p.adiciona_aresta("a5", "B", "D")
g_p.adiciona_aresta("a6", "D", "E")
g_p.adiciona_aresta("a7", "B", "E")
g_p.adiciona_aresta("a8", "C", "B")




