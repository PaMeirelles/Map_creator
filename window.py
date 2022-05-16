import pygame as pg

class Window():
  def __init__(self, width, height, bg_color):
    pg.init()
    self.width = width;
    self.height = height;
    self.bg_color = bg_color
    self.clock = pg.time.Clock()
    self.window = pg.display.set_mode((self.width, self.height))

  def main_loop(self):
    self.clock.tick(60)
    self.window.fill(self.bg_color)
    pg.display.update()

