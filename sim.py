
import pygame
import random
from bird import Bird

class Simulation:
    def __init__(self, window_instance):
        self.window_instance = window_instance
        self.num_birds = 100
        self.sim_birds = []

        self.spawn_birds()

    def update(self):
        self.draw_birds()

    def spawn_birds(self):
            for bird in range(self.num_birds):
                print("spawning new bird " + str(bird))

                random_x = random.randint(0, self.window_instance.screen.get_width())
                random_y = random.randint(0, self.window_instance.screen.get_height())

                print("\t@pos (" + str(random_x) + ", " + str(random_y) + ")")

                spawn_position = (random_x, random_y)

                new_bird = Bird(self.window_instance, spawn_position)  # Assuming Bird takes a window_instance parameter

                self.sim_birds.append(new_bird)


    def draw_birds(self):
        for bird in self.sim_birds:
            bird.update()
            bird.draw()