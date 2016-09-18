import networkx as nx
import matplotlib
import pylab as plt

m = 5
h = 3
interval = h * 2 - 1
N = interval * (m-1)

G=nx.Graph()
G.add_nodes_from(range(N))
G.add_edges_from([(i,(i+1)%N) for i in xrange(N)])
for MEMS_ID in xrange((m-1)/2):
    G.add_edges_from([(i,(i+interval*(MEMS_ID+1))%N) for i in xrange(N)])

nx.draw_circular(G, with_labels=True, node_size=500, node_color='#6ab0de', alpha=1, font_size=14)
mng = plt.get_current_fig_manager()
mng.resize(500,500)
plt.show()
