# Se me solicita
# Crear un juego, que mezcle PACMAN, con SNAKE. 
# Es decir, cuando la culebra choque con un límite, aparecerá en el lado contrario.
# Habrá celdas que representan rocas, y la culebra no podrá atravesar, y el jugador pierde.
# Realizar solamente con modo texto, sin utilizar librerías. 

# Lo imagino en CDM donde 
# 0 es una celda vacía
# # es una roca
# 1 es la culebra  
# $ es la comida.
# Primero debo definir los "limites" del juego, es decir, el grid o la grilla.

class Grid:
    def __init__(self, width,height):
        self.width = width
        self.height = height
        self.grid = [['0' for _ in range(width)] for _ in range(height)]
    def display(self):
        for row in self.grid:
            print(' '.join(row))
    def set_cell(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = value
    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None
    def clear(self):
        self.grid = [['0' for _ in range(self.width)] for _ in range(self.height)]

class Snake:
    def __init__(self, grid):
        self.grid = grid
        self.body = [(grid.width // 2, grid.height // 2)] # La culebra empieza en el centro
        self.direction = (0, 1) # Dirección inicial (derecha)
        self.grow = False
    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % self.grid.width, (head_y + dir_y) % self.grid.height) # Movimiento con wrap-around
        if self.grid.get_cell(*new_head) == '#': # Si choca con una roca
            return False # Juego termina
        if new_head in self.body: # Si choca consigo misma
            return False # Juego termina
        self.body.insert(0, new_head) # Mover la cabeza
        if not self.grow:
            self.body.pop() # Remover la cola si no está creciendo
        else:
            self.grow = False # Resetear crecimiento
        return True
    def change_direction(self, new_direction):
        opposite_directions = { (0,1):(0,-1), (0,-1):(0,1), (1,0):(-1,0), (-1,0):(1,0) }
        if new_direction != opposite_directions.get(self.direction): # No permitir reversa directa
            self.direction = new_direction
    def eat(self):
        self.grow = True
    def draw(self):
        for x, y in self.body:
            self.grid.set_cell(x, y, '1') # Marcar la culebra en la grid
import random
class Food:
    def __init__(self, grid):
        self.grid = grid
        self.position = self.spawn()
    def spawn(self):
        empty_cells = [(x, y) for y in range(self.grid.height) for x in range(self.grid.width) if self.grid.get_cell(x, y) == '0']
        if empty_cells:
            return random.choice(empty_cells)
        return None
    def draw(self):
        if self.position:
            x, y = self.position
            self.grid.set_cell(x, y, '$') # comida 
# Ahora debo definir las rocas
class Rocks:
    def __init__(self, grid, count):
        self.grid = grid
        self.count = count
        self.positions = self.spawn()
    def spawn(self):
        empty_cells = [(x, y) for y in range(self.grid.height) for x in range(self.grid.width) if self.grid.get_cell(x, y) == '0']
        rocks = random.sample(empty_cells, min(self.count, len(empty_cells)))
        for x, y in rocks:
            self.grid.set_cell(x, y, '#') # Marcar las rocas en la grilla
        return rocks
    
# jugar el juego
def main():
    width, height = 20, 10
    grid = Grid(width, height)
    snake = Snake(grid)
    food = Food(grid)
    rocks = Rocks(grid, 30) # Colocar 30 rocas
    game_over = False
    while not game_over:
        grid.clear()
        snake.draw()
        food.draw()
        for rock in rocks.positions:
            grid.set_cell(*rock, '#')
        grid.display()
        move = input("Move (WASD): ").upper()
        if move == 'W':
            snake.change_direction((0, -1))
        elif move == 'S':
            snake.change_direction((0, 1))
        elif move == 'A':
            snake.change_direction((-1, 0))
        elif move == 'D':
            snake.change_direction((1, 0))
        if not snake.move():
            print("Game Over!")
            game_over = True
        if snake.body[0] == food.position:
            snake.eat()
            food.position = food.spawn()

if __name__ == "__main__":
    main()
    