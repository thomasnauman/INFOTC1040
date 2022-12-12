class Animal:
    animal_type = None
    name = None
    mood = None

    def __init__(self, a, n, m):
        if type(a) == str:
            self.animal_type = a
        else:
            raise Exception("Animal type must be a string")
        if type(n) == str:
            self.name = n
        else:
            raise Exception("Name must be a string")
        if type(m) == str:
            self.mood = m
        else:
            raise Exception("Mood must be a string")

    def get_animal_type(self):
        return self.animal_type
    def get_name(self):
        return self.name
    def get_mood(self):
        return self.mood

    def set_animal_type(self, a):
        if type(a) == str:
            self.animal_type = a
        else:
            raise Exception("Animal type must be a string")
    def set_name(self, n):
        if type(n) == str:
            self.name = n
        else:
            raise Exception("Name must be a string")

    def set_mood(self, m):
        if type(m) == str:
            self.mood = m
        else:
            raise Exception("Mood must be a string")