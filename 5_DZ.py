# solution.py

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    def intersection(self, other):
        new_x = max(self.x, other.x)
        new_y = max(self.y, other.y)
        new_x2 = min(self.x + self.w, other.x + other.w)
        new_y2 = min(self.y + self.h, other.y + other.h)

        new_w = new_x2 - new_x
        new_h = new_y2 - new_y

        if new_w > 0 and new_h > 0:
            return Rectangle(new_x, new_y, new_w, new_h)
        else:
            return None


rect1 = Rectangle(3, 5, 2, 1)
rect2 = Rectangle(1, 2, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())
