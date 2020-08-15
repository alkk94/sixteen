from parameters import *
from area import Area
import pygame
import random


class Game:
    # Sounds
    pygame.mixer.init()
    CORRECT_AREA_SOUND = pygame.mixer.Sound("correct_area.wav")

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

    def __init__(self, screen):
        self.screen = screen
        self.run = True
        self.board = Game.get_board()
        self.next_number = 1

        self.execute()

    def execute(self):
        while self.run:
            self.handle_events()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_click_event()

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
            scaled_position = position[0] // ELEMENT_SIZE, position[1] // ELEMENT_SIZE
            if self.board[scaled_position[0]][scaled_position[1]] and \
                    self.board[scaled_position[0]][scaled_position[1]].is_next_area(self.next_number):
                Game.CORRECT_AREA_SOUND.play()
                self.next_number += 1
                self.board[scaled_position[0]][scaled_position[1]] = None
                if self.is_win():
                    self.run = False

    def is_win(self):
        return self.next_number == NUMBER_X * NUMBER_Y + 1
