import pyxel


class Engine:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.engine = Engine(pyxel.width, pyxel.height)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        # pyxel.pset(x, y, 2)


if __name__ == '__main__':
    App()
