from collections import deque

n, m, v = map(int, input().split())  # n: 정점 수, m: 간선 수, v: 시작 정점
g = [[] for _ in range(n + 1)]  # 정점 번호 맞추기 위해 1번부터 시작

# 간선 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)  # 양방향 간선 처리

# 정점별 연결 리스트 정렬 (작은 번호부터 방문하기 위해)
for i in range(1, n + 1):
    g[i].sort()

# DFS 구현
def dfs(v):
    visited[v] = True
    print(v, end=' ')  # 현재 정점 출력
    for i in g[v]:
        if not visited[i]:  # 방문하지 않은 정점 탐색
            dfs(i)

# BFS 구현
def bfs(v):
    que = deque([v])  # 시작 정점 추가
    visited[v] = True  # 방문 처리
    while que:
        v = que.popleft()  # 큐에서 정점 하나 제거
        print(v, end=' ')
        for i in g[v]:
            if not visited[i]:  # 방문하지 않은 정점 탐색
                visited[i] = True
                que.append(i)

# 방문 확인 배열 초기화
visited = [False] * (n + 1)

# DFS 탐색
dfs(v)
print()  # 줄바꿈

# 방문 확인 배열 초기화
visited = [False] * (n + 1)

# BFS 탐색
bfs(v)
