from random import random
import pygame as pg

class Virus():
  def __init__(self, x, y, gen):
    self.x = x
    self.y = y
    self.gen = gen
    
    self.state = "alive"

class VirusManager():
  def __init__(self, lm, window):
    self.lm = lm
    self.window = window
    
    self.viruses = []
    self.survival_chance = 0.97

  def main_cycle(self):
    for n in range(len(self.viruses)):
      virus = self.viruses[n]
      if self.lm[virus.y][virus.x] == 1:
          virus.state = "corpse"
      if virus.state == "alive":
        self.lm[virus.y][virus.x] = 1
        pg.draw.rect(self.window.window, (80, 20, 20), (virus.x, virus.y, 1, 1),)
        self.propagate(virus)
        virus.state = "dead"
      else:
        pg.draw.rect(self.window.window, (155, 155, 100), (virus.x, virus.y, 1, 1))
        virus.state = "corpse"
    self.viruses = [virus for virus in self.viruses if virus.state != "corpse"]
  def propagate(self, virus):
    for i in range(-1, 2):
      for j in range(-1, 2):
        if self.is_legal(virus.x + i, virus.y + j):
          if random() < self.survival_chance ** virus.gen:
            if self.is_legal(virus.x + i, virus.y + j):
              self.viruses.append(Virus(virus.x + i, virus.y + j, virus.gen + 1))
  def is_legal(self, x, y):
    return x > 0 and y > 0 and x < self.window.width and y < self.window.height