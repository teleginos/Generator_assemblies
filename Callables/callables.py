class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

    def __str__(self):
        return f"Прямоугольник со сторонами {self.a} и {self.b}"
