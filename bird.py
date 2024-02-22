import pygame
import random
import math

class Bird:
    def __init__(self, window_instance, initial_position):
        self.window_instance = window_instance
        self.position = initial_position
        self.sprite = self.gen_sprite()

        self.speed = 1
        self.direction = random.uniform(0, 2 * math.pi)

    def update(self):
        self.move()

    def move(self):

        print("direction: ", self.direction)

        self.position[0] += self.speed * math.cos(self.direction[0])
        self.position[1] += self.speed * math.sin(self.direction[1])

    def draw(self):
        # Draw the bird
        self.window_instance.screen.blit(self.sprite, self.position)

        # Draw the direction line
        direction_length = 20  # You can adjust the length of the direction line
        end_point = (
            self.position[0] + direction_length * math.cos(self.direction),
            self.position[1] + direction_length * math.sin(self.direction)
        )

        pygame.draw.line(self.window_instance.screen, 'Red', self.position, end_point, 2)



    def gen_sprite(self):
        surf = pygame.Surface((5, 5))
        surf.fill('White')

        return surf