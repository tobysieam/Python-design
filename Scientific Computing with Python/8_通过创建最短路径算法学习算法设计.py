my_graph = {
    'A': [('B', 3), ('D', 1)],  # 节点 A 连接到节点 B（距离 3）和节点 D（距离 1）
    'B': [('A', 3), ('C', 4)],  # 节点 B 连接到节点 A（距离 3）和节点 C（距离 4）
    'C': [('B', 4), ('D', 7)],  # 节点 C 连接到节点 B（距离 4）和节点 D（距离 7）
    'D': [('A', 1), ('C', 7)]   # 节点 D 连接到节点 A（距离 1）和节点 C（距离 7）
}

# 修改ABCD为包含元组的列表，表示加权边

def shortest_path(graph, start):
    unvisited = []  # 用于存储未访问节点的列表
    for node in graph:
        unvisited.append(node)  # 将所有节点添加到未访问列表中