graph = [[1,2,6,7],[0,2,7],[0,1,3],[2,4],[3,5],[4,6],[0,5,7],[0,1,6]]

solution = []
visited = []

visited = visited + [False]*len(graph)

start = 7
visited[start] = True

solution.append(start)

def hamiltonian_cycles(vertex):
    if start in graph[solution[len(solution)-1]] and \
        len(solution)-1 == len(graph)-1:
        solution.append(vertex)
        return True

    for neighbour in graph[solution[len(solution)-1]]:
        if not visited[neighbour]:
            visited[neighbour] = True
            solution.append(neighbour)

            return True if hamiltonian_cycles(vertex) else False

print "It's true that this graph is hamiltonian?: " + str(hamiltonian_cycles(start))
print "This is the path: " + str(solution)
