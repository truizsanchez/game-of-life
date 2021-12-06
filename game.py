import pyxel

from settings import DEBUG


class Engine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scenario = dict()
        self.neighbors = dict()

    def initialize(self):
        for x in range(self.width):
            for y in range(self.height):
                self.scenario[(x, y)] = 0
                self.neighbors[(x, y)] = []
                neighbors = [(x-1, y-1), (x-1, y), (x-1, y+1),
                             (x, y-1), (x, y+1),
                             (x+1, y-1), (x+1, y), (x+1, y+1)]
                for n in neighbors:
                    if 0 <= n[0] < self.width and 0 <= n[1] < self.height:
                        self.neighbors[(x, y)].append(n)
        if DEBUG:
            self.add_glider(0, 0)

    def add_glider(self, x, y):
        live_cells = [(x+2, y), (x, y+1), (x+2, y+1), (x+1, y+2), (x+2, y+2)]
        for cell in live_cells:
            self.scenario[cell] = 1

    def evaluate_neighborhood(self, x, y):
        n_alive = 0
        for (x_n, y_n) in self.neighbors[(x, y)]:
            n_alive += self.scenario[(x_n, y_n)]
        return n_alive

    def generate_frame(self):
        scenario = dict()
        for x in range(self.width):
            for y in range(self.height):
                n_alive = self.evaluate_neighborhood(x, y)
                if self.scenario[(x, y)] == 0 and n_alive == 3:
                    scenario[(x, y)] = 1
                elif self.scenario[(x, y)] == 1 and 2 <= n_alive <= 3:
                    scenario[(x, y)] = 1
                else:
                    scenario[(x, y)] = 0
        return scenario


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.engine = Engine(pyxel.width, pyxel.height)
        self.engine.initialize()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.engine.scenario = self.engine.generate_frame()

    def draw(self):
        pyxel.cls(0)
        for y in range(self.engine.height):
            for x in range(self.engine.width):
                if self.engine.scenario[(x, y)] == 1:
                    pyxel.pset(x, y, 2)


if __name__ == '__main__':
    App()
