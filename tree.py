import pydot

from main import State, bfs


initial_state = State(3, 3, 0)
states = bfs(initial_state)

tree = pydot.Dot("tree", graph_type="digraph", bgcolor="white")

legend = pydot.Cluster(graph_name="legend", label="Legend", fontsize="20", color="black",
                            fontcolor="black", style="filled", fillcolor="white")

legend1 = pydot.Node("Goal Node", shape="plaintext")
legend.add_node(legend1)
legend2 = pydot.Node("Dead Node", shape="plaintext")
legend.add_node(legend2)
legend3 = pydot.Node("Already Generated Node", shape="plaintext")
legend.add_node(legend3)
legend4 = pydot.Node("Live Node", shape="plaintext")
legend.add_node(legend4)
legend5=pydot.Node("""
← Origin to Destination bank
→ Destination to Origin bank
""", shape="plaintext")
legend.add_node(legend5)

node1 = pydot.Node("1", style="filled", fillcolor="green", label="")
legend.add_node(node1)
node2 = pydot.Node("2", style="filled", fillcolor="red", label="")
legend.add_node(node2)
node3 = pydot.Node("3", style="filled", fillcolor="gray", label="")
legend.add_node(node3)
node4 = pydot.Node("4", style="filled", fillcolor="pink", label="")
legend.add_node(node4)

intro = pydot.Cluster(graph_name="intro", label="Cannibals-Missionaries State Space Tree", fontsize="24", color="white",
                            fontcolor="black", style="filled", fillcolor="white")

intro_node = pydot.Node("Shreyam Pokharel (40)", shape="plaintext", fontsize=18)
intro.add_node(intro_node)

tree.add_subgraph(legend)
tree.add_subgraph(intro)
tree.add_edge(pydot.Edge(legend1, legend2, style="invis"))
tree.add_edge(pydot.Edge(legend2, legend3, style="invis"))
tree.add_edge(pydot.Edge(legend3, legend4, style="invis"))
tree.add_edge(pydot.Edge(legend4, legend5, style="invis"))
tree.add_edge(pydot.Edge(node1, node2, style="invis"))
tree.add_edge(pydot.Edge(node2, node3, style="invis"))
tree.add_edge(pydot.Edge(node3, node4, style="invis"))

for state in states:
    node = pydot.Node(str(state)+str(state.parent), label=str(state))
    node.add_style("filled")
    node.set_fillcolor(state.color)
    tree.add_node(node)

    if state.parent:
        edge = pydot.Edge(str(state.parent)+str(state.parent.parent), str(state)+str(state.parent), label=state.operator())
        tree.add_edge(edge)

tree.write_png("output.png")