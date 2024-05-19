import matplotlib.colors as mcolors
from collections import deque
import task_4

def interpolate_color(start_color, end_color, steps):
    start_rgb = mcolors.to_rgb(start_color)
    end_rgb = mcolors.to_rgb(end_color)
    red_step = (end_rgb[0] - start_rgb[0]) / steps
    green_step = (end_rgb[1] - start_rgb[1]) / steps
    blue_step = (end_rgb[2] - start_rgb[2]) / steps
    colors = [mcolors.to_hex((start_rgb[0] + red_step*i, start_rgb[1] + green_step*i, start_rgb[2] + blue_step*i)) for i in range(steps)]
    return colors

def update_node_color(tree_root, order, title):
    start_color = '#000080'  
    end_color = '#87CEFA'    
    steps = len(order)
    colors = interpolate_color(start_color, end_color, steps)
    for i, node in enumerate(order):
        node.color = colors[i]
    task_4.draw_tree(tree_root, title)

def dfs(node, order):
    if node is not None:
        order.append(node)
        dfs(node.left, order)
        dfs(node.right, order)

def bfs(node, order):
    queue = deque([node])
    while queue:
        current = queue.popleft()
        if current:
            order.append(current)
            queue.append(current.left)
            queue.append(current.right)

def visualize_dfs(tree_root):
    order = []
    dfs(tree_root, order)
    update_node_color(tree_root, order, "DFS")

def visualize_bfs(tree_root):
    order = []
    bfs(tree_root, order)
    update_node_color(tree_root, order, "BFS")



if __name__ == "__main__":
    lst = [1, 22, 2, 12, 3, 16, 19, 4, 11, 5, 33, 6, 56, 7, 1]
    tree_root = task_4.heap_tree(lst)
    visualize_dfs(tree_root)
    visualize_bfs(tree_root)
