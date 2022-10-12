import networkx as nx
import matplotlib.pyplot as plt
import random
from networkx.algorithms import bipartite

B = nx.Graph()
n = [1,2,3,4,5,6,7,8,9,10]
l = [*'abcdefghijkl']
B.add_nodes_from(n, bipartite=0)
B.add_nodes_from(l, bipartite=1)
B.add_edges_from([(1, "a"), (1, "b"), (1, "c"), (1, "d"), (1, "e"), (1, "f"),
				  (2, "a"), (2, "b"), (2, "c"), (2, "d"), (2, "e"), (2, "f"),
				  (3, "e"), (3, "f"), (3, "g"), (3, "h"), (3, "i"), (3, "j"),
				  (4, "e"), (4, "f"), (4, "g"), (4, "h"), (4, "i"), (4, "j"),
				  (5, "h"), (5, "i"), (5, "j"), (5, "k"), (5, "l"), (5, "l"),
				  (6, "h"), (6, "f"), (6, "g"), (6, "h"), (6, "i"), (6, "j"),
				  (6, "h"), (3, "e"), (3, "g"), (3, "h"), (3, "i"), (3, "j"),
				  (6, "h"), (3, "e"), (3, "g"), (3, "h"), (3, "i"), (3, "j"),
				  (6, "h"), (3, "e"), (3, "g"), (3, "h"), (3, "i"), (3, "j"),
				  (6, "h"), (3, "e"), (3, "g"), (3, "h"), (3, "i"), (3, "j"),
				  ])
pos = dict()
pos.update( (n, (1, i)) for i, n in enumerate(n) )
pos.update( (n, (2, i)) for i, n in enumerate(l) )

nx.draw_networkx(B, pos=pos)
nx.draw_networkx_nodes(B, pos=pos, nodelist=n)

plt.axis('off')
plt.show()

B = nx.Graph()

nodes = {}
k = 2
n = 10
ne = 685
e = 229 # since you want total 685 edges, you can have ~229 edges in between two
# adjacent sets of nodes

for i in range(k):
	nodes[i] = list(range(n*i, n*(i+1)))

for i in range(k):
	B.add_nodes_from(nodes[i], bipartite=k)

edges = []
for j in range(k-1):
	for i in range(e):
		edges.append((random.choice(nodes[j]), random.choice(nodes[j+1])))

B.add_edges_from(edges[:ne])

pos = dict()
for j in range(k):
	pos.update( (n, (j, i)) for i, n in enumerate(nodes[j]) )

plt.figure(figsize=(20,40))
nx.draw_networkx(B, pos=pos)

plt.axis('off')
# plt.show()

