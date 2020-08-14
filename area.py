from parameters import *
import pygame


class Area:
    # Area parameters
    AREA_WIDTH, AREA_HEIGHT = ELEMENT_SIZE, ELEMENT_SIZE
    AREA_DIMENSIONS = AREA_WIDTH, AREA_HEIGHT

    # Font sizes
    FONT_SIZE = ELEMENT_SIZE

    pygame.font.init()
    font = pygame.font.SysFont("comicsans", FONT_SIZE)

    def __init__(self, position, number):
        self.position = position
        self.number = number
        self.rect = pygame.Rect(self.position, Area.AREA_DIMENSIONS)

    def get_font_position(self):
        if self.number >= 10:
            return self.position[0] + 15, self.position[1] + 25
        else:
            return self.position[0] + 45, self.position[1] + 25

    def draw(self, screen):
        pygame.draw.rect(screen, ORANGE, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 3)
        number_label = Area.font.render(f"{self.number}", 1, WHITE)
        font_position = self.get_font_position()
        screen.blit(number_label, font_position)

    def is_next_area(self, number):
        return self.number == number
