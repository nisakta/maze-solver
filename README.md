# 🧩 Mini Grid Maze Solver

Python ile geliştirilmiş, ızgara (grid) tabanlı labirentler üzerinde **BFS (Breadth-First Search)** ve **DFS (Depth-First Search)** arama algoritmalarını çalıştıran, performanslarını karşılaştıran ve bulunan alternatif yolları Tkinter GUI arayüzünde görselleştiren bir masaüstü uygulamasıdır.

---

## 🚀 Özellikler

* **Çift Algoritma Desteği:** BFS ile en kısa yol garantisi, DFS (Backtracking) ile derinlemesine yol arama.
* **Çoklu Yol Keşfi:** Labirentteki tüm olası alternatif çözümleri bulma ve listeleme.
* **İnteraktif GUI (Tkinter):** Butonlar aracılığıyla algoritmaları tetikleme ve yollar arasında 🔄 geçiş yapabilme.
* **Performans Analizi:** Her algoritma çalıştırıldığında toplam bulunan yol sayısı, adım sayısı ve çalışma süresi (saniye) takibi.

---

## 🛠️ Teknolojiler ve Veri Yapıları

* **Dil:** Python 3
* **Arayüz:** Tkinter (GUI)
* **Veri Yapıları & Algoritmalar:** 
  * `Queue (deque)` - BFS (FIFO)
  * `Stack / Recursion` - DFS (LIFO & Backtracking)
  * `2D Arrays (Matrix)` - Labirent Izgara Yapısı
  * `Set` - Ziyaret edilen düğümleri $O(1)$ sürede kontrol etme

---

## 💻 Kurulum ve Çalıştırma

1. Repoyu bilgisayarınıza klonlayın:
   ```bash
   git clone [https://github.com/nisakta/maze-solver.git](https://github.com/nisakta/maze-solver.git)
   