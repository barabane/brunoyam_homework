# Бинарный поиск
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(arr, item):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = round((last + first) / 2)
        guess = arr[mid]

        if guess == item:
            return guess

        if guess > item:
            last = mid - 1
        elif guess < item:
            first = mid + 1
    return None


print(binary_search(arr, 2))


# Сортировка вставками
arr = [5, 2, 2, 4, 3, 6, 5, 8, 13, 0]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while (j >= 0 and temp < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
    return arr


print(insertion_sort(arr))

# Поиск в ширину
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
queue = []


def bfs(visited, graph, node):
    global queue
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(visited, graph, 'A')
