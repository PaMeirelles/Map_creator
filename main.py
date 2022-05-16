import pygame as pg
from window import Window

win = Window(600, 400, ((0, 0, 0)))

running = True
while running:
  win.main_loop()
  for e in pg.event.get():
    if e.type == pg.QUIT:
      running = False

pg.quit()