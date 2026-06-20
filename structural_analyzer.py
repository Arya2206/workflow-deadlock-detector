import networkx as nx

def find_unreachable_nodes(graph):

    if "Start" not in graph.nodes():
        return []

    reachable = nx.descendants(graph, "Start")

    reachable.add("Start")

    unreachable = []

    for node in graph.nodes():

        if node not in reachable:
            unreachable.append(node)

    return unreachable


def find_orphan_nodes(graph):

    orphan_nodes = []

    for node in graph.nodes():

        if graph.degree(node) == 0:
            orphan_nodes.append(node)

    return orphan_nodes