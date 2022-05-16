import pygame as pg

class Map_generator():
  def __init__(self, water_ratio, node_size, node_color):
    self.water_ratio = water_ratio
    self.node_size = node_size
    self.node_color = node_color
    self.node_list = []

  def create_node(self, location):
    self.node_list.append(Node(self.node_size, self.node_color, location))
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