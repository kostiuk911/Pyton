from lab4.colorama import Fore, Style, init

# Ініціалізація colorama
init()

class Shape3D:
    def __init__(self, color):
        self.color = color

    def get_2d_representation(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def display_ascii_art(self):
        representation = self.get_2d_representation()
        color_code = self.get_color_code()
        for line in representation:
            print(color_code + line + Style.RESET_ALL)

    def get_color_code(self):
        return Fore.WHITE  # Можна реалізувати логіку для інших кольорів

class Cube(Shape3D):
    def __init__(self, size, color):
        super().__init__(color)
        self.size = size

    def get_2d_representation(self):
        cube_lines = [
            " " * self.size + "+" + "-" * self.size + "+",
            " " * self.size + "/" + " " * self.size + "/|",
            " " * self.size + "+" + "-" * self.size + "+ |",
            " " * self.size + "|" + " " * self.size + "|" + "+",
            " " * self.size + "|" + " " * self.size + "|/",
            " " * self.size + "+" + "-" * self.size + "+"
        ]
        return cube_lines + self.get_shadow_representation()

    def get_shadow_representation(self):
        shadow_lines = [
            " " * (self.size + 1) + "#" * self.size + " ",
            " " * (self.size + 1) + "#" * self.size + " ",
            " " * (self.size + 1) + "#" * self.size + " "
        ]
        return shadow_lines

    def scale(self, factor):
        self.size = max(1, int(self.size * factor))

    def translate(self, offset):
        pass  # Реалізуйте логіку для зберігання координат, якщо потрібно