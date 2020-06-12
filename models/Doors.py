from models.SquareWall import SquareWall


class Doors(SquareWall):
    def __init__(self, file_image, side, rect_x, rect_y):
        side = side - 14
        rect_x = rect_x + 7
        rect_y = rect_y + 7
        super().__init__(file_image, side, rect_x, rect_y)
        self.opened = False
