import pygame
import numpy as np
from logik import *

pygame.init()

width, height = 1000, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lorenz Attractor Simulation")

x = y = z = 0.0

def control(x, y, z):
    key = pygame.key.get_pressed()
    rotation_speed = 0.1 
    if key[pygame.K_LEFT]:
        y += rotation_speed
    elif key[pygame.K_RIGHT]:
        y -= rotation_speed
    elif key[pygame.K_UP]:
        x += rotation_speed
    elif key[pygame.K_DOWN]:
        x -= rotation_speed
    elif key[pygame.K_SPACE]:
        z += rotation_speed
    elif key[pygame.K_RETURN]:
        z -= rotation_speed
    elif key[pygame.K_r]:
        x = y = z = 0
    elif key[pygame.K_F11]:
        pygame.display.toggle_fullscreen()
    return x, y, z

t = np.linspace(0, 100, 10000)
punkte = projectionMatrixCalculation(*lorenzAttraktor(t))

def drawPoints(points):
    min_x, max_x = np.min(points[:, 0]), np.max(points[:, 0])
    min_y, max_y = np.min(points[:, 1]), np.max(points[:, 1])
    for p in points:
        x, y = p[0], p[1]
        screen_pos = (int(width / 2 + x * 20), int(height / 2 - y * 20))
        if any(screen_pos) <= 0 or any(screen_pos) > width:
            continue
        x_normalized = (x - min_x) / (max_x - min_x)
        y_normalized = (y - min_y) / (max_y - min_y)
        color = (int(x_normalized * 255), int(y_normalized * 255), 100)
        pygame.draw.circle(window, color, screen_pos, 1)

while True:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    x, y, z = control(x, y, z)
    points = rotation(points=punkte, rotX=x, rotY=y, rotZ=z)
    drawPoints(points)
    pygame.display.update()
