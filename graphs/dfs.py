adjacency_list = [[5,6],[2,7],[1,4,5],[5],[2],[0,2,3],[0],[1]]

travel = []

# Init travel list
for i in xrange(0, len(adjacency_list)):
    travel.append('unvisited')

# Which vertex to start searching
start = 0

# As this vertex is part of the solution,
# print it
print start

# The first vertex is the start vertex
vertex = start

def dfs(vertex):
    # Mark as visited
    travel[vertex] = 'visited'

    # Iterate over all adjacencies of
    # vertex. It takes Θ(E).
    for node in adjacency_list[vertex]:
        if travel[node] == 'unvisited':
            # The next step of traveling
            print node

            # Call dfs recursively
            # It takes Θ(V+E)
            dfs(node)

dfs(vertex)

# Time Complexity
# Since the algorithm iterates over every edge
# of the graph, so it takes Θ(E). The recursive call
# dfs(node) is passed E times for V vertices, so the total
# complexity is Θ(V+E)
