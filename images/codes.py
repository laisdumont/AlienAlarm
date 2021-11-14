class Images:
    def __init__(self, param):
        self.tema = param

    def bg(self):
        back = "images/backgrounds/bg_inicial{}.png".format(self.tema)
        return back


