import pygame
from pygame.locals import *
from app import *
from node import *

class Scene:
    id = 0
    bg = pygame.Color('gray')
    def __init__(self, *args, **kwargs):
        App.scenes.append(self)
        App.scene = self
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg
        self.bgFile = kwargs['bgFile']
        self.imgFolder = kwargs['img_folder']
        if self.bgFile != '':
            self.img = pygame.image.load(self.imgFolder+'/'+self.bgFile)
            size = App.screen.get_size()
            self.img = pygame.transform.smoothscale(self.img, size)
    def draw(self):
        App.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()
    def __str__(self):
        return 'Scene {}'.format(self.id)

