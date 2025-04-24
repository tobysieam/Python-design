my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):  # 添加 target 参数，默认值为空字符串
    unvisited = list(graph)  # 使用 list() 构造函数将 graph 的键转换为列表
    distances = {node: 0 if node == start else float('inf') for node in graph}  # 初始化距离字典
    paths = {node: [] for node in graph}  # 初始化每个节点的路径为空列表
    paths[start].append(start)  # 将起始节点添加到其自身的路径列表中

    # 主循环：当未访问节点列表不为空时继续运行
    while unvisited:
        current = min(unvisited, key=distances.get)  # 根据距离选择当前要访问的节点

        # 遍历当前节点的邻居
        for neighbor, weight in graph[current]:
            # 检查通过当前节点到达邻居节点的距离是否更短
            if distances[current] + weight < distances[neighbor]:
                distances[neighbor] = distances[current] + weight  # 更新邻居节点的距离

                # 检查路径中最后一个元素是否等于当前节点
                if paths[neighbor] and paths[neighbor][-1] == neighbor:  # 确保路径不为空
                    paths[neighbor] = paths[current][:]  # 使用切片创建路径的副本
                else:
                    paths[neighbor].extend(paths[current])  # 将当前节点路径扩展到邻居节点路径
                    paths[neighbor].append(neighbor)  # 将邻居节点本身添加到路径中

        unvisited.remove(current)  # 从未访问列表中移除当前节点

    # 使用三元语法设置 targets_to_print
    targets_to_print = [target] if target else graph

    # 打印目标节点的路径和距离
    for node in targets_to_print:
        if node == start:
            continue
            print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
            return distances, paths

# 调用 shortest_path 函数
shortest_path(my_graph, 'A', 'F')  # 示例：查找从 A 到 C 的最短路径