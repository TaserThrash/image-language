import pygame
pygame.init()
from math import *
from random import *

width = 500
height = 500
z = 0;

code = ""

print("""insert the code dummy z is the brightness overflow at 256
type "stop" to stop""")

while True:
  c = input("");
  if c == "stop":
    break
  code += c + "\n"

win = pygame.display.set_mode((width,height));

for x in range(width):
  for y in range(height):
    exec(code)
    if z != 0:
      pygame.draw.rect(win, (z % 255, z % 255, z % 255), (x, y, 1, 1));
pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            break
