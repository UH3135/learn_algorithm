import heapq


def dijkstra(length):
    heap = []
    heapq.heappush(heap, (0, 0))

    distances = [float("Inf")]*(length+1)
    distances[0] = 0

    while heap:
        distance, position = heapq.heappop(heap)
        is_next = True
        if distance > distances[position]:
            continue
        for s, e, l in graph:
            if position != s:
                continue
            next_distance = distance + l
            if distances[e] > next_distance:
                distances[e] = next_distance
                heapq.heappush(heap, (next_distance, e))
                is_next = False
        if is_next and position < length:
            heapq.heappush(heap, (distance+1, position+1))

    return distances[-1]


N, D = map(int, input().split())
graph = []

for _ in range(N):
    a, b, c = map(int, input().split())
    if b > D:
        continue
    graph.append((a, b, c))

print(dijkstra(D))
