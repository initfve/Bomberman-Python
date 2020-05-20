from models.SquareWall import SquareWall


# Obiekt ktory da sie zniszczyc
class Obstacle(SquareWall):
    def __init__(self, file_image, side, rect_x, rect_y):
        super().__init__(file_image, side, rect_x, rect_y)
        self.destructible = True
