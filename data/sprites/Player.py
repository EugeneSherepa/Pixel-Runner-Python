import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_walk_1 = pygame.image.load("data/graphics/Player/player_walk_1.png").convert_alpha()
        image_walk_2 = pygame.image.load("data/graphics/Player/player_walk_2.png").convert_alpha()
        self.image_walk = [image_walk_1, image_walk_2]
        self.image_jump = pygame.image.load("data/graphics/Player/jump.png").convert_alpha()
        self.index = 0
        self.image = self.image_walk[self.index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        self.index = 0

        self.jump_sound = pygame.mixer.Sound("data/audio/jump.mp3")
        self.jump_sound.set_volume(0.2)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_sound.play()
            self.gravity = -15

    def apply_gravity(self):
        self.gravity += 0.5
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation(self):
        if self.rect.bottom < 300:
            self.image = self.image_jump
        else:
            self.index += 0.1
            if self.index > len(self.image_walk):
                self.index = 0
            self.image = self.image_walk[int(self.index)]

    def update(self, *args, **kwargs):
        self.player_input()
        self.apply_gravity()
        self.animation()