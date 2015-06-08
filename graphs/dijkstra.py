import sys

INFINITE = sys.maxint / 4

graph = [[None,2,6,7,None],
         [None,None,None,3,6],
         [None,None,None,None,4],
         [None,None,None,None,5],
         [None,None,None,None,None]]

shortest_path = []
queue = []

start_vertex = 0
end_vertex = 4

for vertex in graph:
    for edge in vertex:
        if edge:
            min_priority_queue.append(edge)

        min_weight = min(min_priority_queue)
while len(min_priority_queue) > 0:
    current_weight = min_priority_queue[0]
    del min_priority_queue[0]

    shortest_path.append()
