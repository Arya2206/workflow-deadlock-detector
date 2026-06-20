import networkx as nx

def build_graph(nodes, edges):

    G = nx.DiGraph()

    G.add_nodes_from(nodes)

    G.add_edges_from(edges)

    return G
