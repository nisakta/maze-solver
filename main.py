# 2D Labirent Tanımlaması (Grid)
# 5x6 boyutlarında örnek bir labirent
grid = [
    ['S', '.', '.', '#', '.', '.'],
    ['#', '.', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '.', '.', '.'],
    ['.', '.', '.', '#', '.', 'E']
]

def print_maze(maze):
    """
    Labirent matrisini terminale düzenli ve okunabilir şekilde bastırır.
    """
    print("\n--- MEVCUT LABİRENT ---")
    for row in maze:
        print(" ".join(row))
    print("-----------------------\n")

if __name__ == "__main__":
    print_maze(grid)