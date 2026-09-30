import math
class Rectangle:
    """Defines a rectangle with width and height attributes."""
    def __init__(self, width:int, height:int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width:int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return math.sqrt(self.width * self.width + self.height * self.height)

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture_width = '*' * self.width + '\n'
        # First we define how width should be printed, and set up a newline for height.
        picture_height = picture_width * self.height
        # Multiplying width by height gets us our picture, so we just print that.
        return picture_height

    def get_amount_inside(self, shape:'Rectangle') -> int:
        '''A rectangle with a width of 4 and a height of 8 could fit into two squares with sides of 4'''
        cut_height = math.floor(self.height / shape.height)
        # What doesn't fit, we're going to cut off and round down. 
        # A height of 8 vs. height of 4 is going to fit at least 2 times if width allows for it.
        cut_width = math.floor(self.width / shape.width)
        # Same principle, cut off what doesn't fit. Width of 4 vs. 4 is going to fit at least once.
        # If height allows for it.
        return cut_height * cut_width
        #In the above example, the height fits twice and the width fits once. So the shape fits twice.
class Square(Rectangle):
    def __init__(self, side: int) -> None:
        super().__init__(side, side)
    def __str__(self) -> str:
        return f"Square(side={self.height})"
    def set_width(self, width:int) -> None:
        self.width = width
        self.height = width
    def set_height(self, height:int) -> None:
        self.width = height
        self.height = height
    def set_side(self, side: int):
        self.set_width(side)