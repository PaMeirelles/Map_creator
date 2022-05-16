from random import random

class Virus():
  def __init__(self, x, y, lm, generation):
    self.x = x
    self.y = y
    self.lm = lm
    self.generation = generation
    
    self.death_chance = .996
    
    lm[x][y] = 1

    if random() < self.death_chance ** generation:
      self.propagate()

  def propagate(self):
    if self.x > 0 and self.lm[self.x-1][self.y] == 0:
      Virus(self.x - 1, self.y, self.lm, self.generation + 1)
    if self.x < len(self.lm[0]) and self.lm[self.x+1][self.y] == 0:
      Virus(self.x + 1, self.y, self.lm, self.generation + 1)
    if self.y > 0 and self.lm[self.x][self.y-1] == 0:
      Virus(self.x, self.y-1, self.lm, self.generation + 1)
    if self.x < len(self.lm) and self.lm[self.x][self.y+1] == 0:
      Virus(self.x, self.y+1, self.lm, self.generation + 1)
        
      