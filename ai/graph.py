import heapq

class Graph:
    def _init_(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_safe(self, v, color, c):
        for i in range(self.vertices):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def backtracking(self, color_set):
        color = [None] * self.vertices
        self.util_backtracking(color_set, color, 0)

        num_colors_used = len(set(color))
        print("Minimum number of colors used (Backtracking):", num_colors_used)
        print("Graph coloring:")
        for i, c in enumerate(color):
            print("Vertex", i, "colored with:", c)

    def util_backtracking(self, color_set, color, v):
        if v == self.vertices:
            return True

        for c in color_set:
            if self.is_safe(v, color, c):
                color[v] = c
                if self.util_backtracking(color_set, color, v + 1):
                    return True
                color[v] = None

    def branch_bound(self, color_set):
        def graph_coloring():
            # Priority queue to store (coloring, vertex) pairs based on the number of used colors
            pq = [(0, [-1] * self.vertices)]

            while pq:
                used_colors, coloring = heapq.heappop(pq)

                # Find the next vertex to color
                v = coloring.index(-1) if -1 in coloring else self.vertices
                if v == self.vertices:
                    return coloring

                for c in color_set:
                    if self.is_safe(v, coloring, c):
                        new_coloring = list(coloring)
                        new_coloring[v] = c
                        heapq.heappush(pq, (used_colors + 1, new_coloring))

        coloring = graph_coloring()
        num_colors_used = len(set(coloring))
        print("Minimum number of colors used (Branch and Bound):", num_colors_used)
        print("Graph coloring:")
        for i, c in enumerate(coloring):
            print("Vertex", i, "colored with:", c)


def main():
    vertices = int(input("Enter the number of vertices in the graph: "))
    g = Graph(vertices)

    print("Enter the adjacency matrix of the graph:")
    for i in range(vertices):
        row = list(map(int, input().split()))
        for j in range(vertices):
            g.graph[i][j] = row[j]
    while True:
        print("\nSelect the method to solve the graph coloring problem:")
        print("1. Backtracking")
        print("2. Branch and Bound")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            color_set = input("Enter the set of colors separated by space: ").split()
            g.backtracking(color_set)
        elif choice == '2':
            color_set = input("Enter the set of colors separated by space: ").split()
            g.branch_bound(color_set)
        else:
            print("Invalid choice. Please enter '1' or '2'.")

        char = input("Do you want to stop? (yes)")
        if char.lower() == "yes":
            break

if _name_ == "_main_":
    main()
