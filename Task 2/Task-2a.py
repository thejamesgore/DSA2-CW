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

def visualise_graph(G, title="Original Graph"):
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

# Keeps track of which nodes are connected
class TreeTracker:
    def __init__(self, nodes):
        # setup empty tracking dicts 
        self.connections = {}
        self.grp_ranks = {}  # bigger number = bigger group
        
        # start with everything separate
        for node in nodes:
            self.connections[node] = node  # points to itself at start
            self.grp_ranks[node] = 0  # all groups size 0 initially
    
    # traces up through parents to find the main root node
    def find_root(self, n):
        current = n
        
        # keep going until we hit a node that points to itself
        while self.connections[current] != current:
            # skip the middle men - point straight to grandparent
            # this makes it faster next time we check
            self.connections[current] = self.connections[self.connections[current]]
            current = self.connections[current]
            
        return current
    
    # tries to merge two separate groups of nodes
    def merge_groups(self, n1, n2):
        # figure out which groups they're in
        root1 = self.find_root(n1) 
        root2 = self.find_root(n2)
        
        # already in same group? nothing to do
        if root1 == root2:
            return
            
        # merge smaller group into bigger one
        # this keeps the tree flatter and faster to search
        if self.grp_ranks[root1] > self.grp_ranks[root2]:
            # group 1 bigger, absorb group 2
            self.connections[root2] = root1
        elif self.grp_ranks[root1] < self.grp_ranks[root2]:
            # group 2 bigger, absorb group 1
            self.connections[root1] = root2
        else:
            # same size, just pick one
            # make group 1 slightly bigger since it absorbed group 2
            self.connections[root2] = root1
            self.grp_ranks[root1] += 1

# function to find minimum spanning tree
def find_mst_edges(G, edges):
    # sort edges by weight first 
    edges_by_weight = sorted(edges, key=lambda x: x[2])  # x[2] gets the weight
    
    # keep track of which nodes are connected
    node_tracker = TreeTracker(G.nodes())
    
    # edges we're keeping for our minimum tree
    final_edges = []
    # save each step so we can show it later
    construction_steps = []
    
    print("Starting to build MST...")  # helpful to see it's working
    
    # check each edge from smallest weight to biggest
    for edge in edges_by_weight:
        start_node = edge[0]
        end_node = edge[1]
        weight = edge[2]
        
        # see if these nodes are already connected somehow
        if node_tracker.find_root(start_node) != node_tracker.find_root(end_node):
            # not connected, so this is a good edge to add
            print(f"Adding edge {start_node}-{end_node} with weight {weight}")  # debug info
            node_tracker.merge_groups(start_node, end_node)
            final_edges.append(edge)
            
            # save this step so we can visualize it
            temp_graph = nx.Graph()
            temp_graph.add_nodes_from(G.nodes())
            temp_graph.add_weighted_edges_from(final_edges)
            construction_steps.append((temp_graph, f"Added edge {start_node}-{end_node} (weight: {weight})"))
    
    # see what we ended up with
    total_weight = sum(e[2] for e in final_edges)
    print(f"\nDone! MST total weight: {total_weight}")
    
    return construction_steps, final_edges

# Create initial graph
G, edges = create_base_graph()
print("Original graph:")
visualise_graph(G)

# Find and show the MST
print("\nFinding minimum spanning tree...")
steps, mst_edges = find_mst_edges(G, edges)

# Show each step of building the MST
for i, (step_graph, title) in enumerate(steps, 1):
    print(f"\nStep {i}/{len(steps)}")
    visualise_graph(step_graph, title)