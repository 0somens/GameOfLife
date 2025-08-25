import pygame, sys 
from grid import Grid
from simulation import Simulation
WIDTH, HEIGHT = 750, 750
FPS = 3
CELL_SIZE = 25

# colors 
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

grid = Grid(WIDTH, HEIGHT, CELL_SIZE)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of life")

clock = pygame.time.Clock()

simulation = Simulation(WIDTH, HEIGHT, CELL_SIZE)


# simulation loop
while True:
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            column = pos[0] // CELL_SIZE
            simulation.toggle_cell(row,column)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Game of life - Running")
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of life - Paused")
            elif event.key == pygame.K_r:
                simulation.create_random_state()
                pygame.display.set_caption("Game of life - Reset")
            elif event.key == pygame.K_c:
                simulation.clear()
                pygame.display.set_caption("Game of life - Cleared")
            elif event.key == pygame.K_w:
                FPS += 1
            elif event.key == pygame.K_s:
                FPS -= 1
                if FPS > 15:
                    FPS -= 13
            

    # Actualizar estado
    simulation.update()
    
        
    # Drawing

    window.fill(GREY)
    simulation.draw(window)    
    pygame.display.flip()
    clock.tick(FPS)
    
    
    # Podria agregar el sistema de reproducción de los conejos, el que sale en este video:
    # https://www.youtube.com/watch?v=EOvLhZPevm0