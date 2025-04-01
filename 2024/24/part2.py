from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt

gates = {}

def mkwire(pref, n):
    return f"{pref}{n:02}"


def get_gates_till(n_s, n_l):
    return set(get_gates_till_impl(n_l)) - set(get_gates_till_impl(n_s))

def get_gates_till_impl(n):
    q = Queue()
    for i in range(n+1):
        q.put(mkwire("z", i))
    l = []

    while not q.empty():
        wire = q.get()
        if wire[0] in "xy":
            continue

        wire1, wire2, gate = gates[wire]
        l.append(f"{wire1} {gate} {wire2} -> {wire}")
        q.put(wire1)
        q.put(wire2)
    return l

def add_node(G, node):
    if node[0] == "x" or node[0] == "y":
        G.add_node(node, label=node, color='yellow')
    elif node[0] == "z":
        G.add_node(node, label=node, color='orange')
    else:
        G.add_node(node, label=node, color='green')

def make_grapth(nodes_):
    node_cnt = 0
    G = nx.DiGraph()

    for wr in nodes_:
        if wr in gates:
            w1, w2, g = gates[wr]
            add_node(G, w1)
            add_node(G, w2)
            add_node(G, wr)
            gate_node = f"{g}{node_cnt}"
            if g == "AND":
                G.add_node(gate_node, color = "purple")
            if g == "OR":
                G.add_node(gate_node, color = "pink")
            if g == "XOR":
                G.add_node(gate_node, color = "red")
            node_cnt += 1
            G.add_edge(w1, gate_node)
            G.add_edge(w2, gate_node)
            G.add_edge(gate_node, wr)


    node_colors = [ G.nodes[node]['color'] for node in G.nodes]


    # Draw the graph using matplotlib
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Use spring layout for better spacing
    pos = nx.nx_agraph.graphviz_layout(G, prog='dot', args='-Grankdir=TB')  # Top to Bottom flow
    nx.draw(G, pos, node_color=node_colors, with_labels=True, node_size=2000, font_size=12, font_weight='bold', arrows=True)
    plt.title("Logical Relationships Visualization")
    plt.show()



def main(filename):
    lines = open(filename).read().splitlines()


    sp = [ i for i in range(len(lines)) if lines[i] == '' ][0]
    for line in lines[sp + 1:]:
        wire1, gate, wire2, _, wire_res = line.split(' ')
        gates[wire_res] = (wire1, wire2, gate)

        #
    l = get_gates_till(15, 17)
    # print(l)
    nodes = set()
    for node in l:
        x, g, y, ar, z = node.split(' ')
        nodes.add(x)
        nodes.add(y)
        nodes.add(z)
    make_grapth(nodes)


Z_MAX = 45
main("input")

"""
16
23
36
45
"""

# X = 0b100110011011100110101010011010111111011001101
# Y = 0b110011100110110111000110001001100100000011001
# Z = X + Y
# Z_RES = 49430469426918
# print (f"{Z ^ Z_RES:b}")
# 1 1111 0000 0000 0000 0000 0000 0000 0000 0000 0000
     # 36

# qff qnw
# qqp z23
# fbq z36
# pbv z16
