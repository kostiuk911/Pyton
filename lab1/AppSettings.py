import lab1.constants.constants as const

class AppSettings:
    def __init__(self):
        self.decimal_places = const.DECIMALS
        self.console_color = "white"

    def change_decimals(self, decimals):
        self.decimal_places = decimals

    def change_color(self, color):
        self.console_color = color
