import networkx as nx
import matplotlib.pyplot as mp

def create_base_graph():
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
    return G, edges

def visualize_graph(G, title="Original Graph"):
    # Define layout with better spacing
    pos = nx.spring_layout(G, k=2, iterations=100, seed=42)

    # Create figure
    mp.figure(figsize=(10, 8))
    mp.title(title)
    
    # Remove the box
    mp.axis('off')

    # Draw the graph with node labels
    nx.draw(G, pos, with_labels=True, font_color="black", 
            node_color="lightgreen", node_size=2000)

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    mp.show()

# Create and visualize the graph
G, edges = create_base_graph()
visualize_graph(G)