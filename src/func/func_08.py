
def midpoint(x1, y1, x2, y2):
    """Return the midpoint between (x1; y1) and (x2; y2)."""
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2
    return xm, ym

x, y = midpoint(2, 4, 8, 12)
print (x, y)
#5.0, 8.0
