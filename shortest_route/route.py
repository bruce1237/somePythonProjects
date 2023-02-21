import math
import random
import matplotlib.pyplot as plt


class route:
    dot_num = 10
    map_x = 0
    map_y = 0
    map_ratio = 10
    dots = []
    start_dot_key = 0
    start_dot = []
    route = []

    def __init__(self, dots: int):
        self.dot_num = dots
        self.map_x = self.map_y = dots * self.map_ratio
        self.processing()

    def processing(self):
        print("generate dots")
        self.generate_dots()
        print("picking starting dot")
        start_dot = self.get_start_dot()
        print("get near dot")
        self.near_dots(start_dot)
        print("====================")
        self.route.insert(0, self.start_dot)
        print(self.route)

        print("generate chart")
        self.convert_route_to_chart()

    def generate_dots(self):

        for dot in range(self.dot_num):
            new_dot = self.generate_dot(self.dots)
            print("generate dot:", dot, ": ", new_dot)
            self.dots.insert(dot, new_dot)

    def generate_dot(self, dots: list):
        x = random.randint(0, self.map_x)
        y = random.randint(0, self.map_y)
        if self.is_dot_exist(x, y, dots):
            print("dot already exits, regenerating ...")
            self.generate_dot(dots)
        else:
            return [x, y]

    def get_start_dot(self):
        self.start_dot_key = random.randint(0, self.dot_num) - 1

        start_dot = self.dots[self.start_dot_key]
        self.start_dot = start_dot

        print("starting dot:", self.start_dot_key, start_dot)

        self.dots.remove(start_dot)
        print("start dot removed from dots list")
        return start_dot

    def near_dots(self, start_dot: list):
        print("start dot: ", start_dot)
        if start_dot in self.dots:
            print("remove start dot: ", start_dot)
            self.dots.remove(start_dot)

        while self.dots:
            dists = []
            for key, dot in enumerate(self.dots):
                print(key, self.dots[key])
                dst = self.calculate_distance(start_dot, dot)
                print(dst)
                dists.insert(key, dst)

            print(dists)
            sorted_dists = sorted(range(len(dists)), key=lambda k: dists[k])
            print(sorted_dists)

            if len(sorted_dists) > 1:
                next_dot = self.dots[sorted_dists[1]] if self.dots[sorted_dists[0]] == start_dot else self.dots[
                    sorted_dists[0]]
            else:
                next_dot = self.dots[sorted_dists[0]]
            self.route.append(next_dot)

            print("next_dot", next_dot)

            self.near_dots(next_dot)

    def calculate_distance(self, start_dot: list, dot: list):

        x = start_dot[0] - dot[0]
        y = start_dot[1] - dot[1]
        return math.sqrt(pow(x, 2) + pow(y, 2))

    def is_dot_exist(self, x: int, y: int, dots: list):
        if [x, y] in dots:
            return True
        return False

    def convert_route_to_chart(self):
        x = []
        y = []
        for dot in self.route:
            x.append(dot[0])
            y.append(dot[1])

        print(x,y)
        self.generate_chart(x, y)

    def generate_chart(self, x: list, y: list):

        # plotting the points
        plt.plot(x, y)

        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')

        # giving a title to my graph
        plt.title('My first graph!')

        # function to show the plot
        plt.show()
