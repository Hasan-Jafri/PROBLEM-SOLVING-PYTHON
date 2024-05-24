class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
        else:
            print("One or both vertices not found in the graph.")

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for vertices in self.adjacency_list.values():
                if vertex in vertices:
                    vertices.remove(vertex)
        else:
            print("Vertex not found in the graph.")

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)
        else:
            print("One or both vertices not found in the graph.")

    def __str__(self):
        return str(self.adjacency_list)

    def depth_first_search(self, start_vertex):
        visited = set()

        def dfs(vertex):
            visited.add(vertex)
            print(vertex, end=' ')

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_vertex)

    def breadth_first_search(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


# Example usage:
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'A')

print("Graph:")
print(graph)

print("\nDepth First Search:")
graph.depth_first_search('A')

print("\n\nBreadth First Search:")
graph.breadth_first_search('A')
