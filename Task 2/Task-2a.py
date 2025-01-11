import networkx as nx
import matplotlib.pyplot as mp

# Create a graph object
G = nx.Graph()

# Add nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Z']
G.add_nodes_from(nodes)

# Add edges sorted by weight
edges = [
    ('A', 'B', 1),
    ('D', 'F', 1),
    ('E', 'Z', 1),
    ('B', 'D', 3),
    ('E', 'G', 3),
    ('A', 'C', 5),
    ('F', 'Z', 6),
    ('C', 'E', 6),
    ('C', 'D', 8),
    ('C', 'Z', 9),
    ('A', 'G', 10),
]

G.add_weighted_edges_from(edges)

# Define layout
pos = nx.spring_layout(G)

# Draw the graph with node labels
nx.draw(G, pos, with_labels=True, font_color="black", node_color="green", node_size=2000)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

mp.show()
