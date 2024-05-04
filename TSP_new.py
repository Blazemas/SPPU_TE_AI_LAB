import sys

def nearest_neighbor(graph, source): #O(n^2)
  
  n = len(graph)
  visited = [False] * n
  tour = [source]  # Start from source city
  visited[source] = True
  current = source

  for _ in range(n - 1):
    min_distance = float('inf') #infinity distance
    nearest = None

    for i in range(n):
      if not visited[i] and graph[current][i] < min_distance:
        min_distance = graph[current][i]
        nearest = i

    tour.append(nearest)
    visited[nearest] = True
    current = nearest

  # Calculate total cost by summing costs between consecutive cities in the tour
  min_cost = 0
  for i in range(n - 1):
    min_cost += graph[tour[i]][tour[i + 1]]
  min_cost += graph[tour[-1]][source]  # Cost to return to starting city

  return min_cost, tour

if __name__ == "__main__":
  print("Enter number of vertices:")
  n = int(input())
  graph = []

  for i in range(n):
    row = []
    for j in range(n):
        if(i!=j):
            
            print("Enter cost of", i, "to", j)
            e = int(input())
            row.append(e)
        else:
            row.append(0)    
    graph.append(row)

  print("Enter source vertex:")
  source = int(input())
  #tour.append(source)

  min_cost, tour = nearest_neighbor(graph, source)

  tour.append(source)
  print("Minimum Cost of tour: ",min_cost)
  print("Tour Path:", tour)
