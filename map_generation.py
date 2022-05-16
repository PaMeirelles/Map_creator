import pygame as pg
from useful_functions import point_distance

class Map_generator():
  def __init__(self, cell_size, node_size, node_color, window, land_color):
    self.cell_size = cell_size
    self.node_size = node_size
    self.node_color = node_color
    self.land_color = land_color
    self.window = window
    self.node_list = []
    self.land_matrix = [[0 for _ in range(window.width// cell_size)] for _ in range(window.height // cell_size)]

  def create_node(self, location):
    node = Node(self.node_size, self.node_color, location)
    self.node_list.append(node)
    node.draw(self.window)
    
    
  def delete_node(self, location, margin_of_error, bg_color):
    for node in self.node_list:
      if point_distance(node.location, location) < self.node_size * (1 + margin_of_error):
        pg.draw.circle(self.window.window, bg_color, node.location, node.size)
        self.node_list.remove(node)
        self.delete_node(location, margin_of_error, bg_color)
        return 1
    return 0
        
  def draw_nodes(self):
    for node in self.node_list:
      node.draw(self.window)

  def draw_land(self):
    for y, line in enumerate(self.land_matrix):
      for x, cell in enumerate(line):
        if cell == 1:
          pg.draw.rect(self.window.window, self.land_color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
  def fill_holes(self):
   for y in range(1, len(self.land_matrix) - 1):
      for x in range(1, len(self.land_matrix[0]) - 1):
          if (self.land_matrix[y-1][x] == self.land_matrix[y+1][x] == 1) or (self.land_matrix[y][x-1] == self.land_matrix[y][x+1] == 1):
              self.land_matrix[y][x] = 1
              
class Node():
  def __init__(self, size, color, location):
    self.size = size
    self.color = color
    self.location = location
    self.visible = True;

  def draw(self, window):
    if self.visible:
      pg.draw.circle(window.window, self.color, self.location, self.size, 2)