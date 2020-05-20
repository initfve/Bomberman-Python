# Klasa bazowa naszych obiektow/scian
class SquareWall:
    def __init__(self, file_image, side, rect_x, rect_y):
        super().__init__()
        self.side = side
        self.image = file_image
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)
