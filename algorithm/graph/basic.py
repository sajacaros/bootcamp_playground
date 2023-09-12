from collections import deque


def bfs(graph, start_v):  # 재귀
    q1 = deque()
    visited = {start_v: True}

    def bfs_inner(v):
        print(v)
        for node in graph[v]:
            if node not in visited:
                visited[node] = True
                q1.append(node)
        if q1:
            bfs_inner(q1.popleft())
    bfs_inner(start_v)


def bfs2(graph, start_v):  # loop
    visited = {start_v:True}
    q = deque()
    q.append(start_v)
    while q:
        node = q.popleft()
        print(node)
        for child_node in graph[node]:
            if child_node not in visited:
                visited[child_node] = True
                q.append(child_node)


def dfs(graph, start_v):
    visited = {start_v: True}

    def dfs_inner(v):
        print(v)
        for node in graph[v]:
            if node not in visited:
                visited[node] = True
                dfs_inner(node)

    dfs_inner(start_v)

graph = {
    0: [1, 3, 6],
    1: [0, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5],
}

print('--- bfs 재귀 ---')
bfs(graph, start_v=0)
print('-'*10)
print('--- bfs loop ---')
bfs2(graph, start_v=0)
print('-'*10)
print('--- dfs ---')
dfs(graph, start_v=0)
print('-'*10)