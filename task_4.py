import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4()) 

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Heap tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.suptitle(title, fontsize=16, fontweight='bold')
    plt.show()

def heap_tree(lst, index = 0):
    heapq.heapify(lst)
    if index >= len(lst):
        return None
    node = Node(lst[index])
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    node.left = heap_tree(lst, left_index)
    node.right = heap_tree(lst, right_index)
    return node

    

if __name__ == '__main__':
    numbers_list = [12, 3, 7, 2, 9, 25, 63, 13, 19, 44, 2, 6, 1]
    
    heap_tree_root = heap_tree(numbers_list)
    
    draw_tree(heap_tree_root)