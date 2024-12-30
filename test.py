import matplotlib.pyplot as plt
import networkx as nx
from complete_dungeon_graph import CompleteDungeonGraph
from minimum_spanning_tree import MinimumSpanningTree
from maximum_spanning_tree import MaximumSpanningTree

def draw_graph_with_mst(graph: nx.Graph, mst: nx.Graph, title: str) -> None:
    pos = nx.spring_layout(graph, seed=42)

    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color='lightblue',
        node_size=700,
        edge_color='gray',
        width=1,
    )

    nx.draw_networkx_edges(
        mst,
        pos,
        edge_color='red',
        width=2,
    )

    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.title(title)

def main():
    num_nodes = 10
    dungeon_graph = CompleteDungeonGraph(num_nodes=num_nodes)

    #mst_calculator = MinimumSpanningTree(dungeon_graph)
    original_graph = dungeon_graph.graph
    #mst_graph = mst_calculator.get_mst()

    mst_calculator = MaximumSpanningTree(dungeon_graph)
    mst_graph = mst_calculator.get_mst()

    plt.figure(figsize=(12, 6))
    draw_graph_with_mst(original_graph, mst_graph, "Graph with Minimum Spanning Tree Highlighted")
    plt.show()

    if nx.is_tree(mst_graph):
        print("The resulting MST is a tree.")
    else:
        print("The resulting MST is not a tree.")

if __name__ == "__main__":
    main()
