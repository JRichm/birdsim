class Bird:
    def __init__(self, pygame_intance, initial_position):
        self.window_instance = window_instance
        self.position = position
        self.sprite = self.gen_sprite()

    def update(self):
        pass

    def calculate_next_move(self):
        pass

    def gen_sprite(self):
        surf = self.window_instance.pygame.Surface((2, 2))
        surf.fill('White')

        return surf