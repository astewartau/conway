

import pygame as pg
from conway import *
    
def main():
    cell_size = 5
    grid_size = 270, 200
    grid = build_life_grid(*grid_size)

    pg.display.init()
    pg.display.set_mode(([x*cell_size for x in grid_size]), 0, 0)

    surface = pg.display.get_surface()
    clock = pg.time.Clock()
    close = False
    while not close:
        surface.fill((20, 20, 20))
        y_pos = 0
        for row in grid:
            x_pos = 0
            for cell in row:
                if cell:
                    surface.fill(
                        (125, 125, 125),
                        pg.Rect(x_pos, y_pos, cell_size, cell_size)
                    )
                x_pos += cell_size
            y_pos += cell_size
        pg.display.flip()
        conway(grid)
        clock.tick(50)
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                close = True
                break
        
        
        

if __name__ == "__main__":
    main()
