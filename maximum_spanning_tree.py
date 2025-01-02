import networkx as nx
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, PULP_CBC_CMD
from itertools import combinations
from complete_dungeon_graph import CompleteDungeonGraph

class MaximumSpanningTree:
    def __init__(self, dungeon_graph):
        self._mst, self._cost = self._calculate_mst(dungeon_graph.graph)

    def _calculate_mst(self, graph):
        edges = list(graph.edges(data=True))
        nodes = list(graph.nodes(data=True))

        max_weight = max(data['weight'] for _, _, data in edges)
        aux_weights = {(u, v): max_weight - data['weight'] for u, v, data in edges}

        problem = LpProblem("MaximumSpanningTree", LpMinimize)

        edge_vars = {
            (u, v): LpVariable(f"x_{u}_{v}", cat="Binary")
            for u, v, _ in edges
        }

        problem += lpSum(edge_vars[u, v] * aux_weights[u, v] for u, v in aux_weights)
        problem += lpSum(edge_vars.values()) == len(nodes) - 1

        for node in graph.nodes:
            problem += (
                lpSum(edge_vars[u, v] for u, v, _ in edges if u == node or v == node) >= 1
            )

        for subset_size in range(2, len(nodes)):
            for subset in combinations(graph.nodes, subset_size):
                subset_edges = [(u, v) for u, v, _ in edges if u in subset and v in subset]
                problem += (
                    lpSum(edge_vars[u, v] for u, v in subset_edges) <= subset_size - 1
                )

        solver = PULP_CBC_CMD(msg=False)
        problem.solve(solver)

        mst_edges = [
            (u, v, data)
            for u, v, data in edges
            if edge_vars[u, v].value() == 1
        ]

        mst_graph = nx.Graph()
        mst_graph.add_nodes_from(nodes)
        mst_graph.add_edges_from((u, v, {"weight": data["weight"]}) for u, v, data in mst_edges)

        total_cost = sum(data["weight"] for _, _, data in mst_edges)

        return mst_graph, total_cost

    def get_mst(self):
        return self._mst

    def get_cost(self):
        return self._cost
    
    def debug_print_edges(self):
        print("Edges in the MST:")
        for u, v, data in self._mst.edges(data=True):
            print(f"Edge ({u+1}, {v+1}) with weight {data['weight']}")
