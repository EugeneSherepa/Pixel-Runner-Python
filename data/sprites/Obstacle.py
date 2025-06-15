import pygame
import random


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle_type):
        super().__init__()
        self.obstacle_type = obstacle_type
        if self.obstacle_type == "snail":
            snail_1 = pygame.image.load("data/graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("data/graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
        else:
            fly_1 = pygame.image.load("data/graphics/Fly/Fly1.png")
            fly_2 = pygame.image.load("data/graphics/Fly/Fly2.png")
            self.frames = [fly_1, fly_2]
            y_pos = 210

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y_pos))

    def animation_state(self):
        if self.obstacle_type == "snail":
            self.animation_index += 0.05
            if self.animation_index > len(self.frames):
                self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]
            self.rect.x -= 5
        else:
            self.animation_index += 0.2
            if self.animation_index > len(self.frames):
                self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]
            self.rect.x -= 7

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.destroy()