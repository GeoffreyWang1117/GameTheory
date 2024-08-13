import networkx as nx
import matplotlib.pyplot as plt

# 创建有向图
G = nx.DiGraph()

# 添加节点
G.add_node("Hawk")
G.add_node("Dove")
G.add_node("Mixed")

# 添加边 (转换) 和条件概率
G.add_edge("Hawk", "Dove", label="P(H->D) = P(Dove > Hawk)")
G.add_edge("Hawk", "Mixed", label="P(H->M) = ε")
G.add_edge("Dove", "Hawk", label="P(D->H) = P(Hawk > Dove)")
G.add_edge("Dove", "Mixed", label="P(D->M) = ε")
G.add_edge("Mixed", "Hawk", label="P(M->H) = Q(Hawk)/Q(Hawk + Dove)")
G.add_edge("Mixed", "Dove", label="P(M->D) = Q(Dove)/Q(Hawk + Dove)")

# 绘制图
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=16, font_weight="bold", arrowsize=20)

# 在边上添加条件概率标签
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.title("Strategy State Transition Diagram with Conditional Probabilities")
plt.show()
