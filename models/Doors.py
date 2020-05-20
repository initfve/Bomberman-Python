from models.SquareWall import SquareWall


class Doors(SquareWall):
    def __init__(self, file_image, side, rect_x, rect_y):
        super().__init__(file_image, side, rect_x, rect_y)
        self.opened = False
