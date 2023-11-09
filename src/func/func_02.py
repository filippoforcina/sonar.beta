
def calc_rect_area(width, height):
    """Return the area of the rectangle."""
    return width * height

print (calc_rect_area(3, 5))
#15
print (calc_rect_area(width=3, height=5))
#15
print (calc_rect_area(height=5, width=3))
#15
print (calc_rect_area(3, height=5))
#15

size = (3, 5)
print (calc_rect_area(*size))
#15
size = {'width': 3, 'height': 5}
print (calc_rect_area(**size))
#15
