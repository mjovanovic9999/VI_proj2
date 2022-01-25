from queue import LifoQueue

def answer_graph(graph: dict[str, list[str]]) -> None:
    return

def degree_heuristic(graph: dict[str, list[str]]) -> list[str]:
    nodes = list(graph.keys())
    nodes.sort(key=lambda cvor: len(graph[cvor]), reverse=True)
    return nodes

def forward_checking(graph:dict[str, tuple[list[str], list[str]]], node: str, answer: str, visited_nodes: set[str]) -> bool:
    for neighbor in graph[node][0]:
        if neighbor not in visited_nodes:
            if answer in graph[neighbor][1]:
                if len(graph[neighbor][1]) == 1:
                    restore_answer_options(graph, (node, answer))
                    return False
                graph[neighbor][1].remove(answer)    
    return True

def restore_answer_options(graph:dict[str, tuple[list[str], list[str]]], answered_node: tuple[str,str]) -> None:
    for neighbor in graph[answered_node[0]][0]:
            if answered_node[1] not in graph[neighbor][1]:
                graph[neighbor][1].append(answered_node[1])

def create_graph_with_answer_options(graph: dict[str, list[str]]) -> dict[str, tuple[list[str], list[str]]]:
    graph_with_answer_options = dict[str, tuple[list[str], list[str]]]()
    for node in list(graph.keys()):
        graph_with_answer_options[node] = (graph[node], ["A", "B", "C", "D"])      
    return graph_with_answer_options

def add_answer_nodes_to_stack(stack: LifoQueue, node: str, graph: dict[str, tuple[list[str], list[str]]]):
    for answer in reversed(graph[node][1]):
        stack.put((node, answer))

#def add_prev_nodes_to_dict(prev_nodes : dict[tuple[str, str], list[tuple[str,str]]], prev: tuple[str,str], node: str):
 #   for 


def depth_first_search(graph: dict[str, tuple[list[str], list[str]]], node_order: list[str]):
    
    stack_nodes = LifoQueue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[node_order[0]] = None
    add_answer_nodes_to_stack(stack_nodes, node_order[0], graph)
    graph_answered = False
    
    path = list()

    while not graph_answered and not stack_nodes.empty():
        node = stack_nodes.get()
        
        if forward_checking(graph, node[0], node[1], visited):
            destination = node_order[node_order.index(node[0]) + 1]
            add_answer_nodes_to_stack(stack_nodes, destination, graph)
            prev_nodes[destination] = node

        
        # if found_dest:
        #     path.append(end)
        #     prev = prev_nodes[end]
        #     while prev is not None:
        #         path.append(prev)
        #         prev = prev_nodes[prev]
        #     path.reverse()
    return path
