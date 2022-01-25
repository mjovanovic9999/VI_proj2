from queue import LifoQueue


def answer_graph(graph: dict[str, tuple[int, int, str, str, tuple[str, str, str]]]) -> list[tuple[tuple[int,int,int],str]]:
    return depth_first_search(create_graph_with_answer_options(graph), degree_heuristic(graph))


def degree_heuristic(graph: dict[str, tuple[int, int, str, str, tuple[str, str, str]]]) -> list[tuple[int, int, int]]:
    nodes = list(graph.keys())
    nodes.sort(key=lambda node: len(graph[node]), reverse=True)
    return nodes


def forward_checking(graph: dict[tuple[int,int,int], tuple[list[tuple[int,int,int]], list[str]]], node: tuple[int,int,int], answer: str, visited_nodes: set[tuple[int,int,int]]) -> bool:
    for neighbor in graph[node][0]:
        if neighbor not in visited_nodes:
            if answer in graph[neighbor][1]:
                if len(graph[neighbor][1]) == 1:
                    restore_answer_options(graph, (node, answer))
                    return False
                graph[neighbor][1].remove(answer)
    return True


def restore_answer_options(graph: dict[tuple[int,int,int], tuple[list[tuple[int,int,int]], list[str]]], answered_node: tuple[tuple[int,int,int], str]) -> None:
    for neighbor in graph[answered_node[0]][0]:
        if answered_node[1] not in graph[neighbor][1]:
            graph[neighbor][1].append(answered_node[1])


def create_graph_with_answer_options(graph: dict[str, tuple[int, int, str, str, tuple[str, str, str]]]) -> dict[tuple[int,int,int], tuple[list[tuple[int,int,int]], list[str]]]:
    graph_with_answer_options = {}
    for node in list(graph.keys()):
        graph_with_answer_options[node] = (graph[node], ["A", "B", "C", "D"])
    return graph_with_answer_options


def add_answer_nodes_to_stack(stack: LifoQueue, node: tuple[int,int,int], graph: dict[tuple[int,int,int], tuple[list[tuple[int,int,int]], list[str]]]) -> None:
    for answer in reversed(graph[node][1]):
        stack.put((node, answer))


def depth_first_search(graph:  dict[tuple[int,int,int], tuple[list[tuple[int,int,int]], list[str]]], node_order: list[str]) -> list[tuple[tuple[int,int,int],str]]:

    stack_nodes = LifoQueue()
    visited = set()
    prev_nodes = dict()
    prev_nodes[node_order[0]] = None
    add_answer_nodes_to_stack(stack_nodes, node_order[0], graph)
    graph_answered = False

    path = list()
    node = None
    while not graph_answered and not stack_nodes.empty():
        node = stack_nodes.get()

        if forward_checking(graph, node[0], node[1], visited):
            visited.add(node[0])
            if node_order.index(node[0]) < len(node_order) - 1:
                destination = node_order[node_order.index(node[0]) + 1]
                prev_nodes[destination] = node
                add_answer_nodes_to_stack(stack_nodes, destination, graph)
            else:
                graph_answered = True

    if graph_answered:
        path.append(node)
        prev = prev_nodes[node[0]]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev[0]]
        path.reverse()
    return path
