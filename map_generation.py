import pygame as pg
from useful_functions import point_distance

class Map_generator():
  def __init__(self, water_ratio, node_size, node_color):
    self.water_ratio = water_ratio
    self.node_size = node_size
    self.node_color = node_color
    self.node_list = []

  def create_node(self, location):
    self.node_list.append(Node(self.node_size, self.node_color, location))
    
  def delete_node(self, location, margin_of_error):
    for node in self.node_list:
      if point_distance(node.location, location) < self.node_size * (1 + margin_of_error):
        self.node_list.remove(node)
        self.delete_node(location, margin_of_error)
        return 1
    return 0
        
  def draw_nodes(self, window):
    for node in self.node_list:
      node.draw(window)

  

class Node():
  def __init__(self, size, color, location):
    self.size = size
    self.color = color
    self.location = location
    self.visible = True;

  def draw(self, window):
    if self.visible:
      pg.draw.circle(window, self.color, self.location, self.size, 2)