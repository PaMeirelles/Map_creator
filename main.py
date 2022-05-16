import pygame as pg
from window import Window
from map_generation import Map_generator
win = Window(600, 400, ((220, 230, 250)))


mg = Map_generator(0.5, 2, (0, 0, 0))
mg.create_node((200, 200))

running = True
while running:
  win.main_loop()
  for e in pg.event.get():
    if e.type == pg.MOUSEBUTTONDOWN:
      mouse_location = pg.mouse.get_pos()
      if not mg.delete_node(mouse_location, 0.5):
        mg.create_node(mouse_location)
    if e.type == pg.QUIT:
      running = False
  mg.draw_nodes(win.window)
  pg.display.update()

pg.quit()