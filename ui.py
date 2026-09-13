import tkinter as tk
from main import find_all_paths_bfs, find_all_paths_dfs, grid

class MazeUI:
    def __init__(self, root, grid):
        self.root = root
        self.root.title("Mini Maze Solver - Çoklu Yol & Performans")
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.cell_size = 50

        # Yol Geçmişi ve İndeks Hafızası
        self.current_paths = []
        self.path_index = 0
        self.current_algo_name = ""
        self.exec_time = 0.0
        self.color = "#8BC34A"

        # Üst Kısım: Butonlar Paneli
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        self.bfs_btn = tk.Button(self.btn_frame, text="BFS ile Çöz", command=self.run_bfs, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.bfs_btn.pack(side=tk.LEFT, padx=5)

        self.dfs_btn = tk.Button(self.btn_frame, text="DFS ile Çöz", command=self.run_dfs, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        self.dfs_btn.pack(side=tk.LEFT, padx=5)

        self.next_btn = tk.Button(self.btn_frame, text="Diğer Yolu Göster 🔄", command=self.show_next_path, bg="#FF9800", fg="white", font=("Arial", 10, "bold"))
        self.next_btn.pack(side=tk.LEFT, padx=5)

        # Alt Bilgi Etiketi (Performans ve Yol Bilgisi)
        self.info_label = tk.Label(root, text="Bir algoritma seçin...", font=("Arial", 11, "bold"), fg="#333333")
        self.info_label.pack(pady=5)

        # Labirent Tuvali (Canvas)
        self.canvas = tk.Canvas(root, width=self.cols * self.cell_size, height=self.rows * self.cell_size, bg="white")
        self.canvas.pack(padx=20, pady=10)

        self.draw_grid()

    def draw_grid(self):
        """Labirent karelerini tuvale çizer."""
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                x1, y1 = c * self.cell_size, r * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                val = self.grid[r][c]
                
                color = "#333333" if val == '#' else ("#FFD700" if val == 'S' else ("#FF5722" if val == 'E' else "white"))
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#cccccc")
                
                if val in ('S', 'E'):
                    self.canvas.create_text(x1 + 25, y1 + 25, text=val, font=("Arial", 16, "bold"), fill="black")

    def animate_path(self, path, color):
        """Çözüm yolunu ekranda renklendirir."""
        self.draw_grid()
        if not path:
            return
        for r, c in path:
            if self.grid[r][c] not in ('S', 'E'):
                x1, y1 = c * self.cell_size, r * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#cccccc")

    def run_bfs(self):
        paths, exec_time = find_all_paths_bfs(self.grid)
        self.setup_paths("BFS", paths, exec_time, "#8BC34A")

    def run_dfs(self):
        paths, exec_time = find_all_paths_dfs(self.grid)
        self.setup_paths("DFS", paths, exec_time, "#03A9F4")

    def setup_paths(self, algo_name, paths, exec_time, color):
        self.current_algo_name = algo_name
        self.current_paths = paths
        self.path_index = 0
        self.color = color
        self.exec_time = exec_time

        if not paths:
            self.info_label.config(text=f"❌ {algo_name}: Hiç yol bulunamadı!")
            self.draw_grid()
        else:
            self.render_current_path()

    def show_next_path(self):
        if not self.current_paths:
            return
        # Bir sonraki yola geç (Döngüsel)
        self.path_index = (self.path_index + 1) % len(self.current_paths)
        self.render_current_path()

    def render_current_path(self):
        path = self.current_paths[self.path_index]
        total = len(self.current_paths)
        steps = len(path) - 1
        msg = f"📊 {self.current_algo_name} | Yol {self.path_index + 1}/{total} | Adım: {steps} | Süre: {self.exec_time:.5f} sn"
        self.info_label.config(text=msg)
        self.animate_path(path, self.color)

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeUI(root, grid)
    root.mainloop()