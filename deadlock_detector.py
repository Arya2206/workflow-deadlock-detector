import networkx as nx

def detect_deadlock(graph):

    cycles = list(nx.simple_cycles(graph))

    return cycles