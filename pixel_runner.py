import os
import sys
import pygame
import random
from pathlib import Path
from data.sprites.Player import Player
from data.sprites.Obstacle import Obstacle


def create_desktop_shortcut():
    try:
        import pythoncom
        import win32com.client

        desktop = Path(os.path.join(os.environ["USERPROFILE"], "Desktop"))
        shortcut_path = desktop / "Pixel Runner.lnk"

        if not shortcut_path.exists():
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortcut(str(shortcut_path))
            shortcut.TargetPath = sys.executable  # full path to .exe
            shortcut.WorkingDirectory = os.getcwd()
            shortcut.IconLocation = sys.executable
            shortcut.save()
    except Exception as e:
        print(f"Shortcut creation failed: {e}")


def display_score():
    time = pygame.time.get_ticks() - start_time
    seconds = int((time // 1000))
    minutes = seconds // 60
    score_surface = font_mid.render(f"{minutes:02d} : {seconds % 60:02d}", False, (64, 64, 64))
    final_score_rect = score_surface.get_rect(center=(400, 80))
    screen.blit(score_surface, final_score_rect)
    return time


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    return True


pygame.init()

# Game Globals
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixel Runner")
window_icon = pygame.image.load("data/graphics/Player/player_stand.png")
pygame.display.set_icon(window_icon)
clock = pygame.time.Clock()
game_active = False
start_time = 0
final_time = 0
bg_music = pygame.mixer.Sound("data/audio/music.wav")
bg_music.play(loops=-1)
bg_music.set_volume(0.5)

# Font
font_big = pygame.font.Font("data/font/Pixeltype.ttf", 50)
font_mid = pygame.font.Font("data/font/Pixeltype.ttf", 40)
font_small = pygame.font.Font("data/font/Pixeltype.ttf", 30)

# Background
sky_surface = pygame.image.load("data/graphics/Sky.png").convert()
ground_surface = pygame.image.load("data/graphics/ground.png").convert()

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Player start screen
player_stand = pygame.image.load("data/graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    create_desktop_shortcut()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True

        if event.type == obstacle_timer and game_active:
            obstacle_group.add(Obstacle(random.choice(["snail", "snail", "snail", "fly"])))

    if game_active:
        # Background
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        final_time = display_score()

        # Groups Draw
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()

        # Game Over statement
        game_active = collision_sprite()
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        if final_time > 0:
            title = font_big.render("You lost :(", 1, "black")
            seconds = int((final_time // 1000)) % 60
            minutes = int((final_time // 1000)) // 60
            score_text = font_small.render(f"Your time is: {minutes:02d}:{seconds:02d}", 1, "black")
            restart_text = font_mid.render(f'Press "Space" to restart the game', 1, "black")
        else:
            title = font_big.render("Welcome to the Pixel Run!", 1, "black")
            score_text = font_big.render("", 1, "black")
            restart_text = font_mid.render(f'Press "Space" to start the game', 1, "black")

        score_rect = score_text.get_rect(center=(400, 80))
        restart_container = restart_text.get_rect(center=(400, 350))
        title_rect = title.get_rect(center=(400, 50))
        screen.blit(restart_text, restart_container)
        screen.blit(title, title_rect)
        screen.blit(score_text, score_rect)
        start_time = pygame.time.get_ticks()

    pygame.display.update()
    clock.tick(60)
