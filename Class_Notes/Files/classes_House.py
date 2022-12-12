class House:
    name = None
    head = None
    points = 500

    def __init__(self, n, h):
        self.name = n
        self.head = h
        # self.points = p

    def __str__(self):
        return f"{self.name}"

    def get_name(self):
        return self.name
    def get_head(self):
        return self.head
    def get_points(self):
        return self.points

    def set_name(self, n):
        self.name = n
    def set_head(self, h):
        self.head = h
    def set_points(self, p):
        if p >= 0:
            self.points = p
        else:
            print("Points cannot be less than zero")