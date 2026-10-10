"""
Task 4.2: Hub-to-Hub Route Cost (Floyd-Warshall Algorithm)
"""
INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

if __name__ == "__main__":
    print("--- TASK 4.2: FLOYD-WARSHALL ROUTING ---")
    # Hubs: Manila (0), Batangas (1), Iloilo (2), Cebu (3), Davao (4)
    graph = [
        [0,   4,   8,  12, INF],
        [4,   0,   6, INF,   8],
        [8,   6,   0,   3,  10],
        [12, INF,   3,   0,   5],
        [INF,  8,  10,   5,   0]
    ]
    
    dist_matrix = floyd_warshall(graph)
    print("Shortest path cost from Manila (0) to Davao (4): PHP", dist_matrix[0][4], "thousand")
    print("Task 4.2 executed successfully.\n")
