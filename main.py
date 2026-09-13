import time
from collections import deque

# 2D Labirent Tanımlaması (5x6 Grid)
grid = [
    ['S', '.', '.', '#', '.', '.'],
    ['.', '.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.'],
    ['.', '.', '.', '#', '.', 'E']
]

def find_start(maze):
    """Labirentteki 'S' (Start) noktasının koordinatlarını bulur."""
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                return (r, c)
    return None

def find_all_paths_bfs(maze):
    """Labirentteki tüm olası yolları BFS kullanarak bulur ve en kısadan en uzuna sıralar."""
    start_time = time.time()
    rows, cols = len(maze), len(maze[0])
    start = find_start(maze)
    if not start:
        return [], 0

    queue = deque([(start[0], start[1], [start])])
    all_paths = []

    while queue:
        r, c, path = queue.popleft()

        if maze[r][c] == 'E':
            all_paths.append(path)
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                # Kendi kendini kesmesini önlemek için aynı yoldan tekrar geçmesini engelliyoruz
                if maze[nr][nc] != '#' and (nr, nc) not in path:
                    queue.append((nr, nc, path + [(nr, nc)]))

    exec_time = time.time() - start_time
    all_paths.sort(key=len)  # Yolları adım sayısına göre sırala
    return all_paths, exec_time

def find_all_paths_dfs(maze):
    """Labirentteki tüm olası yolları DFS (Backtracking) kullanarak bulur."""
    start_time = time.time()
    rows, cols = len(maze), len(maze[0])
    start = find_start(maze)
    if not start:
        return [], 0

    all_paths = []

    def backtrack(r, c, current_path, visited):
        if maze[r][c] == 'E':
            all_paths.append(list(current_path))
            return

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    current_path.append((nr, nc))
                    
                    backtrack(nr, nc, current_path, visited)
                    
                    # Backtrack işlemi: Geri dönerken kilidi aç
                    current_path.pop()
                    visited.remove((nr, nc))

    backtrack(start[0], start[1], [start], {start})
    exec_time = time.time() - start_time
    return all_paths, exec_time

def print_maze(maze):
    """Labirent matrisini terminale basar."""
    print("\n--- MEVCUT LABİRENT ---")
    for row in maze:
        print(" ".join(row))
    print("-----------------------\n")

if __name__ == "__main__":
    print_maze(grid)
    bfs_paths, bfs_time = find_all_paths_bfs(grid)
    dfs_paths, dfs_time = find_all_paths_dfs(grid)
    print(f"BFS Toplam Yol: {len(bfs_paths)} | Süre: {bfs_time:.5f} sn")
    print(f"DFS Toplam Yol: {len(dfs_paths)} | Süre: {dfs_time:.5f} sn")