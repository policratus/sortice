adjacency_list = [[5,6],[2,7],[1,4,5],[5],[2],[0,2,3],[0],[1]]

travel, queue = [], []

# Init travel list
for i in xrange(0, len(adjacency_list)):
    travel.append('unvisited')

# Which vertex to start
start = 7

# Enqueue start vertex
# It takes O(1)
queue.append(start)

# While has vertices to analyze
while len(queue) > 0:
    # Dequeue
    # It takes O(1)
    current = queue[0]
    del queue[0]

    # For all adjacencies of current vertex
    for vertex in adjacency_list[current]:
        # If not visited yet
        if travel[vertex] == 'unvisited':
            # Mark as visited
            travel[vertex] = 'visited'

            # Every vertex of the graph
            # will be in the queue in some
            # moment. Hence, this traversing
            # will take O(V+E)
            queue.append(vertex)

    travel[current] = 'visited'

    print current

# Time complexity
# Since we've O(V+E) + O(1) + O(1), we came up
# with O(V+E), which proves that breadth-first search
# runs in linear time, or O(V+E)
