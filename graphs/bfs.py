adjacency_list = [[5,6],[2,7],[1,4,5],[5],[2],[0,2,3],[0],[1]]

travel, queue = [], []

# Init graph
for i in xrange(0, len(adjacency_list)):
    travel.append('unvisited')

# Which vertex to start
start = 3

# Set start to gray and enqueue it
travel[start] = 'gray'
queue.append(start)

# While has vertices to analyze
while len(queue) > 0:
    # dequeue
    current = queue[0]
    del queue[0]

    # For all adjacencies of current vertex
    for adjacent in adjacency_list[current]:
        # If not visited yet
        if travel[adjacent] == 'unvisited':
            # Mark as visiting
            travel[adjacent] = 'visited'

            queue.append(adjacent)

    travel[current] = 'visited'

    print current
