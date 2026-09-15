import random
import time
import tkinter as tk


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)

        self.cell_size = 20
        self.grid_size = 20
        self.width = self.cell_size * self.grid_size
        self.height = self.cell_size * self.grid_size

        self.canvas = tk.Canvas(
            self.root,
            width=self.width,
            height=self.height,
            bg="black",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.root.bind("<KeyPress>", self.on_key_press)

        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.score = 0
        self.speed = 0.12

        self.coin = self.spawn_coin()
        self.running = True
        self.game_loop()

    def spawn_coin(self):
        free_cells = [
            (x, y)
            for x in range(self.grid_size)
            for y in range(self.grid_size)
            if (x, y) not in self.snake
        ]
        if not free_cells:
            return None
        return random.choice(free_cells)

    def on_key_press(self, event):
        if not self.running:
            return

        key_map = {
            "Up": (0, -1),
            "Down": (0, 1),
            "Left": (-1, 0),
            "Right": (1, 0),
        }
        if event.keysym in key_map:
            new_dir = key_map[event.keysym]
            if not (
                new_dir[0] == -self.direction[0]
                and new_dir[1] == -self.direction[1]
            ):
                self.next_direction = new_dir

    def move(self):
        if not self.running:
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % self.grid_size, (head_y + dy) % self.grid_size)

        if new_head in self.snake:
            self.running = False
            self.show_game_over()
            return

        self.snake.insert(0, new_head)

        if self.coin and new_head == self.coin:
            self.score += 1
            self.coin = self.spawn_coin()
            self.speed = max(0.04, self.speed - 0.005)
        else:
            self.snake.pop()

        self.draw()

    def draw(self):
        self.canvas.delete("all")

        # Draw grid
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                self.canvas.create_rectangle(
                    x * self.cell_size,
                    y * self.cell_size,
                    (x + 1) * self.cell_size,
                    (y + 1) * self.cell_size,
                    fill="dark green" if (x + y) % 2 == 0 else "green",
                    outline="",
                )

        # Draw snake
        for x, y in self.snake:
            self.canvas.create_rectangle(
                x * self.cell_size,
                y * self.cell_size,
                (x + 1) * self.cell_size,
                (y + 1) * self.cell_size,
                fill="lime",
                outline="dark green",
            )

        # Draw coin
        if self.coin:
            cx, cy = self.coin
            self.canvas.create_oval(
                cx * self.cell_size + 4,
                cy * self.cell_size + 4,
                (cx + 1) * self.cell_size - 4,
                (cy + 1) * self.cell_size - 4,
                fill="gold",
                outline="orange",
                width=2,
            )

        self.canvas.create_text(
            self.width / 2,
            10,
            text=f"Score: {self.score}",
            fill="white",
            font=("Arial", 12, "bold"),
        )

    def show_game_over(self):
        self.canvas.create_text(
            self.width / 2,
            self.height / 2,
            text="Game Over\nPress R to restart",
            fill="white",
            font=("Arial", 18, "bold"),
            justify="center",
        )
        self.root.bind("<KeyPress>", self.restart_if_needed)

    def restart_if_needed(self, event):
        if event.keysym == "r":
            self.root.unbind("<KeyPress>")
            self.root.bind("<KeyPress>", self.on_key_press)
            self.__init__(self.root)

    def game_loop(self):
        if self.running:
            self.move()
        self.root.after(int(self.speed * 1000), self.game_loop)


if __name__ == "__main__":
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()
