import networkx as nx
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, PULP_CBC_CMD
from complete_dungeon_graph import CompleteDungeonGraph

class MinimumSpanningTree:
    def __init__(self, dungeon_graph: CompleteDungeonGraph):
        self._mst, self._cost = self._calculate_mst(dungeon_graph.graph)

    def _calculate_mst(self, graph: nx.Graph) -> tuple[nx.Graph, float]:
        edges = list(graph.edges(data=True))
        nodes = list(graph.nodes)

        problem = LpProblem("MinimumSpanningTree", LpMinimize)

        edge_vars = {
            (u, v): LpVariable(f"x_{u}_{v}", cat="Binary")
            for u, v, _ in edges
        }

        problem += lpSum(edge_vars[u, v] * data['weight'] for u, v, data in edges)
        problem += lpSum(edge_vars.values()) == len(nodes) - 1

        for i, node in enumerate(nodes):
            problem += (
                lpSum(edge_vars[u, v] for u, v, _ in edges if u == node or v == node) >= 1
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

    def get_mst(self) -> nx.Graph:
        return self._mst

    def get_cost(self) -> float:
        return self._cost
