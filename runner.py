class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def run(self):
        self.distance += self.speed

    def walk(self):
        self.distance += self.speed / 2

class Tournament:
    def __init__(self, distance):
        self.distance = distance
        self.runners = []

    def add_runner(self, runner):
        self.runners.append(runner)

    def start(self):
        while any(runner.distance < self.distance for runner in self.runners):
            for runner in self.runners:
                if runner.distance < self.distance:
                    runner.run()
                else:
                    runner.walk()

        results = sorted(self.runners, key=lambda runner: runner.distance, reverse=True)
        return {i + 1: runner.name for i, runner in enumerate(results)}