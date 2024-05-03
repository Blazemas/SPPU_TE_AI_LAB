import heapq

INF = float('inf')

# A* search algorithm implementation
def AStar(graph, heuristic, start, goal):
    n = len(graph)
    distance = [INF] * n
    parent = [-1] * n
    visited = [False] * n

    pq = []  # priority queue

    distance[start] = 0
    heapq.heappush(pq, (heuristic[start], start))

    while pq:
        _, curr = heapq.heappop(pq)

        if curr == goal:
            break

        if visited[curr]:
            continue

        visited[curr] = True

        for i in range(n):
            if graph[curr][i] != INF:
                new_distance = distance[curr] + graph[curr][i]
                if new_distance < distance[i]:
                    distance[i] = new_distance
                    parent[i] = curr
                    heapq.heappush(pq, (new_distance + heuristic[i], i))

    path = []
    a = goal
    while a != -1:
        path.append(a)
        a = parent[a]

    path.reverse()

    return path

if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        # A   B    C    D    E    F    G    H
        [  0 , 11 , 14 , 7  , INF, INF, INF, INF],  # A
        [ 11 , 0  , INF, INF, 15 , INF, INF, INF],  # B
        [ 14 , INF, 0  , INF,  8 , 10 , INF, INF],  # C
        [  7 , INF, INF,  0 , INF, 25 , INF, INF],  # D
        [ INF, 15 , 8  , INF, 0  , INF, INF, 9  ],  # E
        [ INF, INF, 10 , 25 , INF,  0 , 20 , INF],  # F
        [ INF, INF, INF, INF, INF, 20 ,  0 , 10 ],  # G
        [ INF, INF, INF, INF,  9 , INF, 10 , 0  ]   # H
    ]

    # Heuristic values for each node
    heuristic = [40 , 32 , 25 , 35 , 19 , 17 , 0 , 10]

    start = 0
    goal = 6

    path = AStar(graph, heuristic, start, goal)

    # Printing the shortest path
    print("Shortest path from node", start, "to node", goal, ": ", end="")
    for node in path:
        print(chr(node + 65), end=" ")
    print()