

import pygame as pg
from conway import *
    
def main():
    cell_size = 10
    grid_size = 80, 50
    grid = build_life_grid(*grid_size)

    pg.display.init()
    pg.display.set_mode(([x*cell_size for x in grid_size]), 0, 0)

    surface = pg.display.get_surface()
    clock = pg.time.Clock()
    close = False
    pause = False
    one_frame = False
    speed = 15
    while not close:
        if not pause or one_frame:
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
            if one_frame:
                one_frame = False
        clock.tick(speed)
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                close = True
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3:
                    one_frame = True
                elif event.button == 1:
                    pause = not pause
                elif event.button == 4:
                    speed+=1
                elif event.button == 5:
                    speed-=1
                if speed <= 0:
                    speed = 1
                
        
        
        

if __name__ == "__main__":
    main()
