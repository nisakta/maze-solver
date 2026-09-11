from collections import deque

# 2D Labirent Tanımlaması
grid = [
    ['S', '.', '.', '#', '.', '.'],
    ['#', '.', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '.', '.', '.'],
    ['.', '.', '.', '#', '.', 'E']
]

def print_maze(maze):
    """Labirenti terminale bastırır."""
    print("\n--- LABİRENT ---")
    for row in maze:
        print(" ".join(row))
    print("----------------\n")

def find_start(maze):
    """Labirentteki 'S' (Start) noktasının koordinatlarını bulur."""
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                return (r, c)
    return None

def bfs_solve(maze):
    """BFS kullanarak labirenti çözer ve en kısa yolu döndürür."""
    rows, cols = len(maze), len(maze[0])
    start = find_start(maze)
    
    if not start:
        print("Başlangıç noktası bulunamadı!")
        return None

    # Kuyruk: (satır, sütun, izlenen_yol)
    queue = deque([(start[0], start[1], [start])])
    visited = {start}

    # Hareket yönleri: Yukarı, Aşağı, Sol, Sağ
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, path = queue.popleft()

        # Hedefe vardık mı?
        if maze[r][c] == 'E':
            return path

        # 4 yöne bak
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Sınırlar içinde mi, duvar değil mi ve ziyaret edilmedi mi?
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, path + [(nr, nc)]))

    return None  # Yol bulunamadıysa

if __name__ == "__main__":
    print_maze(grid)
    
    path = bfs_solve(grid)
    
    if path:
        print(f"✅ Yol Bulundu! Adım sayısı: {len(path) - 1}")
        print("İzlenen Koordinatlar:", path)
    else:
        print("❌ Yol bulunamadı!")
        