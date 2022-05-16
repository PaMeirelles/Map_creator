import pygame as pg
from window import Window
from map_generation import Map_generator
from virus import Virus, VirusManager

bg_color = (220, 230, 250)
win = Window(500, 500, (bg_color))


mg = Map_generator(4, 5, (0, 0, 0), win, (155, 155, 100))
vm = VirusManager(mg.land_matrix, mg.window, 0.9, 1, 4)
mg.draw_land()
running = True
while running:  
  win.main_loop()
  for e in pg.event.get():
    if e.type == pg.MOUSEBUTTONDOWN:
      mouse_location = pg.mouse.get_pos()
      if not mg.delete_node(mouse_location, 0.3, bg_color):
        mg.create_node(mouse_location)
    if e.type == pg.QUIT:
      running = False
    if e.type == pg.KEYDOWN:
      if e.key == pg.K_SPACE:
        for node in mg.node_list:
          vm.viruses.append(Virus(node.location[0], node.location[1], 0))
      if e.key == pg.K_r:
          vm.random_start(12)
      if e.key == pg.K_c:
        win.window.fill((bg_color))
        mg = Map_generator(4, 5, (0, 0, 0), win, (155, 155, 100))
        vm = VirusManager(mg.land_matrix, mg.window, 0.93, 1, 4)
  vm.main_cycle()
  pg.display.update()
pg.quit()