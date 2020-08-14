from parameters import *
from area import Area
import pygame
import random


class Game:
    # Game parameters
    FPS = 60
    GAME_WIDTH, GAME_HEIGHT = NUMBER_X * ELEMENT_SIZE, NUMBER_Y * ELEMENT_SIZE
    RESOLUTION = GAME_WIDTH, GAME_HEIGHT
    pygame.init()

    @staticmethod
    def get_board():
        numbers = []
        for i in range(1, NUMBER_X * NUMBER_Y + 1):
            numbers.append(i)
        board = []
        for i in range(NUMBER_X):
            areas = []
            for j in range(NUMBER_Y):
                x = random.randint(0, len(numbers) - 1)
                position = i * ELEMENT_SIZE, j * ELEMENT_SIZE
                areas.append(Area(position, numbers[x]))
                numbers.pop(x)
            board.append(areas)
        return board

    def __init__(self):
        self.screen = pygame.display.set_mode(Game.RESOLUTION)
        self.clock = pygame.time.Clock()
        self.run = True
        self.board = Game.get_board()
        self.next_number = 1

        self.execute()

    def execute(self):
        while self.run:
            self.handle_events()
            self.ticking()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_click_event()

    def ticking(self):
        self.clock.tick(Game.FPS)

    def draw(self):
        self.screen.fill(BLACK)
        for areas in self.board:
            for area in areas:
                if area:
                    area.draw(self.screen)
        pygame.display.update()

    def handle_click_event(self):
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            position = position[0] // ELEMENT_SIZE, position[1] // ELEMENT_SIZE
            if self.board[position[0]][position[1]] and \
                    self.board[position[0]][position[1]].is_next_area(self.next_number):
                self.next_number += 1
                self.board[position[0]][position[1]] = None
                if self.is_win():
                    self.run = False
                    print(pygame.time.get_ticks() / 1000)

    def is_win(self):
        return self.next_number == NUMBER_X * NUMBER_Y + 1
