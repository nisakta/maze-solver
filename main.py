from collections import deque

# 2D Labirent Tanımlaması
grid = [
    ['S', '.', '.', '#', '#', '.'],
    ['#', '.', '#', '#', '.', '.'],
    ['#', '.', '.', '.', '#', '.'],
    ['#', '.', '.', '.', '.', '.'],
    ['.', '.', 'E', '.', '.', '.']
]

def print_maze(maze):
    """Labirenti terminale bastırır."""
    print("\n--- LABİRENT ---")
    for row in maze:
        print(" ".join(row))
    print("----------------\n")


def draw_path_on_maze(maze, path, title="ÇÖZÜM"):
    """
    Bulunan yolu labirent üzerinde '*' sembolü ile gösterir.
    'S' (Start) ve 'E' (End) harflerini bozmaz.
    """
    if not path:
        print(f"\n--- {title}: YOL BULUNAMADI ---")
        return

    # Orijinal labirentin kopyasını oluştur (orijinali bozmamak için)
    maze_copy = [row[:] for row in maze]

    # Yol üzerindeki koordinatları '*' yap (S ve E hariç)
    for r, c in path:
        if maze_copy[r][c] not in ('S', 'E'):
            maze_copy[r][c] = '*'

    print(f"\n--- {title} ---")
    for row in maze_copy:
        print(" ".join(row))
    print("-" * (len(title) + 8))


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

def dfs_solve(maze):
    rows, cols = len(maze), len(maze[0])
    start = find_start(maze)
    
    if not start:
        print("Başlangıç noktası bulunamadı!")
        return None

    # Stack yapısı: Son giren ilk çıkar (LIFO)
    stack = [(start[0], start[1], [start])]
    visited = {start}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        # BFS'ten tek farkı burası: popleft() yerine pop() ile EN SON ekleneni çekiyoruz
        r, c, path = stack.pop()

        # Hedefe ulaştık mı?
        if maze[r][c] == 'E':
            return path

        # 4 yönü kontrol et
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    stack.append((nr, nc, path + [(nr, nc)]))

    return None


if __name__ == "__main__":
    print_maze(grid)
    
    bfs_path = bfs_solve(grid)
    dfs_path = dfs_solve(grid)
    
    # Yeni görselleştirme fonksiyonumuzu çağırıyoruz:
    draw_path_on_maze(grid, bfs_path, "BFS İLE ÇÖZÜM")
    draw_path_on_maze(grid, dfs_path, "DFS İLE ÇÖZÜM")