from parameters import *
from game import Game
import pygame
import time


class Menu:
    def __init__(self):
        self.run = True
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.time_result = None

        self.execute()

    def execute(self):
        title_font = pygame.font.SysFont("comicsans", 50)
        while self.run:
            self.draw(title_font)
            self.handle_events()

    def draw(self, title_font):
        self.screen.fill(BLACK)
        title_label = title_font.render("Press the mouse to begin game...", 1, WHITE)
        position = (GAME_WIDTH / 2 - title_label.get_width() / 2, ELEMENT_SIZE)
        self.screen.blit(title_label, position)
        if self.time_result:
            title_label = title_font.render(f"{self.time_result}", 1, WHITE)
            position = (GAME_WIDTH / 2 - title_label.get_width() / 2, 2 * ELEMENT_SIZE)
            self.screen.blit(title_label, position)
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.time_result = time.time()
                Game(self.screen)
                self.time_result = round(time.time() - self.time_result, 2)
