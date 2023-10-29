import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
players_A = ['Player A1', 'Player A2', 'Player A3', 'Player A4', 'Scorer A']
players_B = ['Player B1', 'Player B2', 'Player B3', 'Player B4', 'Scorer B']
for player in players_A + players_B:
    G.add_node(player, type='Player')

G.add_node('Disc', type='Disc')
G.add_node('End Zone A', type='End Zone')
G.add_node('End Zone B', type='End Zone')

pass_edges_A = [(f'Player A{i}', 'Disc') for i in range(1, 4)] + [('Disc', f'Player A{i}') for i in range(2, 5)]
G.add_edges_from(pass_edges_A, action='Pass')
G.add_edges_from([('Player A4', 'Disc'), ('Disc', 'Scorer A'), ('Scorer A', 'End Zone B')], action='Pass')
G.add_edges_from([('Player A3', 'Disc'), ('Disc', 'Player B1')], action='Interception')
pass_edges_B = [(f'Player B{i}', 'Disc') for i in range(1, 4)] + [('Disc', f'Player B{i}') for i in range(2, 5)]
G.add_edges_from(pass_edges_B, action='Pass')
G.add_edges_from([('Player B4', 'Disc'), ('Disc', 'Scorer B'), ('Scorer B', 'End Zone A')], action='Pass')

pos = {
    **{f'Player A{i}': (i, 1) for i in range(1, 5)},
    **{f'Player B{i}': (i, -1) for i in range(1, 5)},
    'Scorer A': (5.5, 1),
    'Scorer B': (-0.5, -1),
    'Disc': (2.5, 0),
    'End Zone A': (0, 0),
    'End Zone B': (5, 0)
}

nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edge_color='gray', arrowstyle='-|>', arrowsize=50)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
edge_labels = {(u, v): data['action'] for u, v, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title('Ultimate Frisbee Concept Graph')
plt.xlim(-1, 6)
plt.show()
