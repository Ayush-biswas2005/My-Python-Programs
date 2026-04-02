class Box:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def volume(self):
        return self.l * self.w * self.h

l = int(input("Enter length: "))
w = int(input("Enter width: "))
h = int(input("Enter height: "))

b = Box(l, w, h)
print("Volume =", b.volume())