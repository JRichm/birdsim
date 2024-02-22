from window import Window
from sim import Simulation

screen_width = 800
screen_height = 600

window = Window(screen_height, screen_width)

simulation = Simulation(window)

running = True
while running:
    window.update()

    simulation.update()

window.quit()


