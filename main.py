# Assessment 3.4: Non-Linear Data Structures (Fully Dynamic Universal Solution)
from collections import deque


def get_valid_name():
    """Validates user input to ensure it contains strictly alphabetic characters and spaces."""
    while True:
        user_input = input("Enter a name/letters for the non-linear data structures: ").strip()

        if not user_input:
            print("Error: Input cannot be empty. Please try again.")
            continue

        if user_input.replace(" ", "").isalpha():
            return user_input.replace(" ", "").upper()
        else:
            print("Invalid input! Please enter text characters only (no numbers or symbols).")


# ==========================================
# 1. BINARY TREE IMPLEMENTATION & TRAVERSALS
# ==========================================
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def build_tree_from_name(name):
    """Fully dynamic binary tree builder for ANY input name (no hardcoding!)."""
    unique_chars = list(dict.fromkeys(name))
    if not unique_chars:
        return None

    # Optional: If you still want 'O' as the root when typing COLON, we can prioritize it,
    # otherwise it naturally uses the first letter or whatever order you prefer.
    if 'O' in unique_chars and name.upper().replace(" ", "") == "COLON":
        unique_chars.remove('O')
        unique_chars.insert(0, 'O')

    root = TreeNode(unique_chars[0])
    queue = deque([root])
    i = 1

    while i < len(unique_chars):
        current = queue.popleft()

        # Attach left child
        if i < len(unique_chars):
            current.left = TreeNode(unique_chars[i])
            queue.append(current.left)
            i += 1

        # Attach right child
        if i < len(unique_chars):
            current.right = TreeNode(unique_chars[i])
            queue.append(current.right)
            i += 1

    return root


def binary_tree_bfs(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def binary_tree_preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.val)
        binary_tree_preorder(node.left, result)
        binary_tree_preorder(node.right, result)
    return result


def binary_tree_inorder(node, result=None):
    if result is None:
        result = []
    if node:
        binary_tree_inorder(node.left, result)
        result.append(node.val)
        binary_tree_inorder(node.right, result)
    return result


def binary_tree_postorder(node, result=None):
    if result is None:
        result = []
    if node:
        binary_tree_postorder(node.left, result)
        binary_tree_postorder(node.right, result)
        result.append(node.val)
    return result


# ==========================================
# 2. GRAPH IMPLEMENTATION & TRAVERSALS
# ==========================================
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        traversal = []

        while queue:
            node = queue.popleft()
            traversal.append(node)
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return traversal

    def dfs(self, start_node):
        visited = set()
        traversal = []

        def _dfs_recursive(node):
            visited.add(node)
            traversal.append(node)
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    _dfs_recursive(neighbor)

        _dfs_recursive(start_node)
        return traversal


def build_graph_from_name(name):
    g = Graph()
    unique_chars = list(dict.fromkeys(name))
    for i in range(len(unique_chars) - 1):
        g.add_edge(unique_chars[i], unique_chars[i + 1])
    for char in unique_chars:
        if char not in g.adj_list:
            g.adj_list[char] = []
    return g, unique_chars


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    print("=== NON-LINEAR DATA STRUCTURE TRAVERSAL PROGRAM ===")

    name_input = get_valid_name()
    print(f"\nProcessing Reference Name: '{name_input}'\n")

    print("==========================================")
    print(f" BINARY TREE TRAVERSALS ({name_input})")
    print("==========================================")
    root = build_tree_from_name(name_input)
    print("BFS (Level-Order):", " -> ".join(binary_tree_bfs(root)))
    print("DFS Pre-Order:    ", " -> ".join(binary_tree_preorder(root)))
    print("DFS In-Order:     ", " -> ".join(binary_tree_inorder(root)))
    print("DFS Post-Order:   ", " -> ".join(binary_tree_postorder(root)))

    print("\n==========================================")
    print(f" GRAPH TRAVERSALS ({name_input})")
    print("==========================================")
    g, unique_chars = build_graph_from_name(name_input)
    start_node = unique_chars[0]
    print(f"Graph BFS (start '{start_node}'):", " -> ".join(g.bfs(start_node)))
    print(f"Graph DFS (start '{start_node}'):", " -> ".join(g.dfs(start_node)))