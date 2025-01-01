import random
import networkx as nx
from globals import VALID_TAG_COMBINATIONS
from meta_room import MetaRoom
from measures import compatibility

class CompleteDungeonGraph:
    def __init__(self, num_nodes):
        self.num_nodes: int = num_nodes
        self.graph: nx.Graph = nx.complete_graph(num_nodes)
        self.generate_graph()

    def generate_graph(self):
        for node in self.graph.nodes():
            characteristics = random.choice(VALID_TAG_COMBINATIONS)
            self.graph.nodes[node]['room'] = MetaRoom(*characteristics)

        for u, v in self.graph.edges():
            room_u = self.graph.nodes[u]['room']
            room_v = self.graph.nodes[v]['room']
            self.graph.edges[u, v]['weight'] = compatibility(room_u, room_v)

    def get_node_data(self, node):
        return self.graph.nodes[node]['room']

    def get_edge_weight(self, u, v):
        return self.graph.edges[u, v]['weight']
