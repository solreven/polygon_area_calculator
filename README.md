# Polygon Area Calculator

## User Stories

1. You should create a `Rectangle` class.
2. When a `Rectangle` object is created, it should be initialized with `width` and `height` attributes. The class should also contain the following methods:
   - `set_width`: Sets the width of the rectangle.
   - `set_height`: Sets the height of the rectangle.
   - `get_area`: Returns the area ($\text{width} \times \text{height}$).
   - `get_perimeter`: Returns the perimeter ($2 \times (\text{width} + \text{height})$).
   - `get_diagonal`: Returns the diagonal ($\sqrt{\text{width}^2 + \text{height}^2}$).
   - `get_picture`: Returns a string that represents the shape using lines of `*`. The number of lines should be equal to the height and the number of `*` in each line should be equal to the width. There should be a new line (`\n`) at the end of each line. If the width or height is larger than 50, this should return the string: `"Too big for picture."`.
   - `get_amount_inside`: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed-in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.