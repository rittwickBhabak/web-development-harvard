class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point is ({self.x},{self.y})"
p = Point(5,6)
print(p.x)
print(p.y)
print(p)