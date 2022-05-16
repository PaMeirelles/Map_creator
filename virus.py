    self.x = x
    self.y = y
    self.gen = gen
    
    self.state = "alive"

class VirusManager():
  def __init__(self, lm, window, sc, pr, cell_size):
    self.lm = lm
    self.window = window
    self.survival_chance = sc
    self.propagation_radius = pr
    self.cell_size = cell_size
    
    self.viruses = []

  def main_cycle(self):
    for n in range(len(self.viruses)):
      virus = self.viruses[n]
      if self.lm[virus.y // self.cell_size][virus.x // self.cell_size] == 1:
          virus.state = "corpse"
      if virus.state == "alive":
        self.lm[virus.y // self.cell_size][virus.x // self.cell_size] = 1
        pg.draw.rect(self.window.window, (80, 20, 20), (virus.x, virus.y, self.cell_size, self.cell_size),)
        self.propagate(virus)
        virus.state = "dead"
      else:
        pg.draw.rect(self.window.window, (155, 155, 100), (virus.x, virus.y, self.cell_size, self.cell_size))
        virus.state = "corpse"
    self.viruses = [virus for virus in self.viruses if virus.state != "corpse"]
  def propagate(self, virus):
    for i in range(-self.propagation_radius * self.cell_size, self.propagation_radius*self.cell_size+1, self.cell_size):
      for j in range(-self.propagation_radius * self.cell_size, self.propagation_radius*self.cell_size+1, self.cell_size):
        if self.is_legal(virus.x + i, virus.y + j):
          if random() < self.survival_chance ** virus.gen:
            if self.is_legal(virus.x + i, virus.y + j):
              self.viruses.append(Virus(virus.x + i, virus.y + j, virus.gen + 1))
  def is_legal(self, x, y):
    return x > 0 and y > 0 and x < self.window.width and y < self.window.height

  def random_start(self, n):
    for i in range(n):
      self.viruses.append(Virus(randint(0, self.window.width), randint(0, self.window.height), 0))