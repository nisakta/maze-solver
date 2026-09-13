import tkinter as tk
from main import bfs_solve, dfs_solve

class MazeUI:
    def __init__(self, root, grid):
        self.root = root
        self.root.title("Mini Maze Solver - GUI")
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.cell_size = 50  # Her kare 50x50 piksel olacak

        # Üst Kısım: Butonlar Paneli
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        self.bfs_btn = tk.Button(self.btn_frame, text="BFS ile Çöz", command=self.run_bfs, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.bfs_btn.pack(side=tk.LEFT, padx=5)

        self.dfs_btn = tk.Button(self.btn_frame, text="DFS ile Çöz", command=self.run_dfs, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        self.dfs_btn.pack(side=tk.LEFT, padx=5)

        self.reset_btn = tk.Button(self.btn_frame, text="Sıfırla", command=self.draw_grid, bg="#f44336", fg="white", font=("Arial", 10, "bold"))
        self.reset_btn.pack(side=tk.LEFT, padx=5)

        # Alt Kısım: Labirent Tuvali (Canvas)
        self.canvas = tk.Canvas(root, width=self.cols * self.cell_size, height=self.rows * self.cell_size, bg="white")
        self.canvas.pack(padx=20, pady=10)

        self.draw_grid()

    def draw_grid(self):
        """Labirenti ekrana çizer."""
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                val = self.grid[r][c]
                color = "white"
                if val == '#':
                    color = "#333333"  # Duvar: Koyu gri
                elif val == 'S':
                    color = "#FFD700"  # Başlangıç: Altın/Sarı
                elif val == 'E':
                    color = "#FF5722"  # Bitiş: Turuncu/Kırmızı

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#cccccc")
                if val in ('S', 'E'):
                    self.canvas.create_text(x1 + 25, y1 + 25, text=val, font=("Arial", 16, "bold"), fill="black")

    def animate_path(self, path, path_color):
        """Bulunan yolu ekranda renklendirir."""
        self.draw_grid()
        if not path:
            return

        for r, c in path:
            if self.grid[r][c] not in ('S', 'E'):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=path_color, outline="#cccccc")

    def run_bfs(self):
        path = bfs_solve(self.grid)
        self.animate_path(path, "#8BC34A")  # Yeşil yol

    def run_dfs(self):
        path = dfs_solve(self.grid)
        self.animate_path(path, "#03A9F4")  # Mavi yol

if __name__ == "__main__":
    from main import grid
    root = tk.Tk()
    app = MazeUI(root, grid)
    root.mainloop()