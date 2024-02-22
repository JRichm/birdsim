import pygame

class Window:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("sim")
        self.running = True
        
        self.draw_surface = pygame.Surface((self.width, self.height))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.screen.blit(self.draw_surface, (0, 0))

        self.draw_surface.fill((0,0,0,0))

        pygame.display.flip()


    def quit(self):
        pygame.quit()