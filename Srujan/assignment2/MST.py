import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
G = nx.Graph()
for i in range(1, 6):
    G.add_node(i)

G.add_edge(1, 2, weight=3)
G.add_edge(1, 3, weight=1)
G.add_edge(2, 3, weight=3)
G.add_edge(2, 4, weight=1)
G.add_edge(3, 4, weight=1)
G.add_edge(4, 5, weight=2)
G.add_edge(3, 5, weight=4)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

MST_Kruskal = nx.tree.minimum_spanning_edges(G, algorithm='kruskal', data=False)
edgelist = list(MST_Kruskal)
print(f"Edges in MST using Kruskal's algorithm: {edgelist}")

MST_Prim = nx.tree.minimum_spanning_edges(G, algorithm='prim', data=False)
edgelist = list(MST_Prim)
print(f"Edges in MST using Prim's algorithm: {edgelist}")


def draw_graph(graph, pos, mst_edges, title):
    plt.clf()
    plt.title(title)
    nx.draw(graph, pos, with_labels=True, edgelist=[e for e in graph.edges if e not in mst_edges])
    nx.draw_networkx_edges(graph, pos, edgelist=mst_edges, edge_color='r', width=2)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)


mst_edges_kruskal = []
mst_edges_prim = []

for edge in nx.tree.minimum_spanning_edges(G, algorithm='kruskal', data=False):
    mst_edges_kruskal.append(edge)

for edge in nx.tree.minimum_spanning_edges(G, algorithm='prim', data=False):
    mst_edges_prim.append(edge)

def update(num):
    if num < len(mst_edges_kruskal):
        draw_graph(G, pos, mst_edges_kruskal[:num + 1], "Kruskal's Algorithm in progress")
    elif num < len(mst_edges_kruskal) + len(mst_edges_prim):
        draw_graph(G, pos, mst_edges_prim[:num - len(mst_edges_kruskal) + 1], "Prim's Algorithm in progress")
    else:
        draw_graph(G, pos, mst_edges_prim, "Algorithm finished")
        plt.close()

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=len(mst_edges_kruskal) + len(mst_edges_prim) + 1, repeat=False, interval=1000)
ani.save('mst_animation.gif', writer=PillowWriter(fps=1))
plt.show()