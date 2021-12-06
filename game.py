import time

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
                x_min = max(x - 1, 0)
                y_min = max(y - 1, 0)
                x_max = min(x + 1, self.width-1)
                y_max = min(y + 1, self.height-1)
                # self.neighbors[(x, y)] = tuple((x2, y2) for x2 in range(x_min, x_max) for y2 in range(y_min, y_max))
                self.neighbors[(x, y)] = []
                for x2 in range(x_min, x_max):
                    for y2 in range(y_min, y_max):
                        if x != x2 and y != y2:
                            self.neighbors[(x, y)].append((x2, y2))
        if DEBUG:
            for (x, y) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
                self.scenario[(x, y)] = 1

    def evaluate_neighborhood(self, x, y):
        n_alive = 0
        for (x_n, y_n) in self.neighbors[(x, y)]:
            n_alive += self.scenario[(x_n, y_n)]
        if n_alive > 0:
            print(n_alive)
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
                else:
                    pyxel.pset(x, y, 7)
        time.sleep(1)


if __name__ == '__main__':
    App()
