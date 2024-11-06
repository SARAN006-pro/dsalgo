IN = 9999
Max = 10

def dijkstra(graph, n, start_node):
    cost = [[IN] * n for _ in range(n)]
    distance = [IN] * n
    pred = [-1] * n
    visited = [False] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                cost[i][j] = IN
            else:
                cost[i][j] = graph[i][j]

    for i in range(n):
        distance[i] = cost[start_node][i]
        pred[i] = start_node
    distance[start_node] = 0
    visited[start_node] = True
    count = 1

    while count < n:
        min_distance = IN
        next_node = None

        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                next_node = i

        if next_node is None:
            break

        visited[next_node] = True

        for i in range(n):
            if not visited[i]:
                new_distance = min_distance + cost[next_node][i]
                if new_distance < distance[i]:
                    distance[i] = new_distance  
                    pred[i] = next_node

        count += 1

    for i in range(n):
        if i != start_node:
            print(f"\nDistance of node {i} = {distance[i]}")
            print(f"Path = {i}", end=" ")
            j = i
            while j != start_node:
                j = pred[j]
                print(f"<- {j}", end=" ")
            print()

n = int(input("Enter the number of nodes: "))
print("Enter the adjacency matrix:")
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
start_node = int(input("Enter the start node: "))
dijkstra(graph, n, start_node)  