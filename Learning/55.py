class point:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")
        

    def draw(self):
        print("draw")



point = point(11, 30)
point.x = 13 
print(point.x)