import pygame as pg
from enemy import Enemy
import constants as c


#initialise pygame
pg.init()

#create clocl
clock = pg.time.Clock()


#create game window
Screen = pg.display.set_mode((c.WIDTH,c.HEIGHT))
pg.display.set_caption("A tower defense gane without a name")

#load image
enemy_image = pg.image.load("assets/images/enemies/enemy_1.png").convert_alpha()


#create groups
enemy_group = pg.sprite.Group()

waypoints = [
    (100,100),
    (400,200),
    (400,100),
    (200,300)
]

enemy = Enemy(waypoints, enemy_image)
enemy_group.add(enemy)

#game loop
run = True
while run:
    
    clock.tick(c.FPS)
    
    Screen.fill("grey100")
    
    #draw enemy path
    pg.draw.lines(Screen, "grey0", False, waypoints)
    
    #update groups
    enemy_group.update()
    
    #draw groups
    enemy_group.draw(Screen)
    
    #event handler
    for event in pg.event.get():
        #quit progam
        if event.type == pg.QUIT:
            run = False
    #update display
    pg.display.flip()
           
pg.quit()