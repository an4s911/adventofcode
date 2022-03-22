from sys import argv
from typing import Dict, Type

filename = argv[1] if len(argv) > 1 else '12.in'


class Cave:

    caves: Dict[str, Type['Cave']] = {}

    def __init__(self, name):
        self.name: str = name
        self.connections = [] if self.name != 'end' else None
        self.caves[self.name] = self
        self.is_small_cave = self.name.islower() and not self.name.isupper()

    def add_connection(self, next_cave: Type['Cave']):
        if self.connections is not None and next_cave.name != "start":
            self.connections.append(next_cave)

    @classmethod
    def connect(cls, cave1_name, cave2_name):
        if cave1_name not in caves:
            cave1 = Cave(cave1_name)

        if cave2_name not in caves:
            cave2 = Cave(cave2_name)

        cave1 = caves[cave1_name]
        cave2 = caves[cave2_name]

        cave1.add_connection(cave2)
        cave2.add_connection(cave1)


caves: Dict[str, Cave] = Cave.caves

# Part 1


def part1():
    ans = 0
    visited = set()

    def search(cave: Cave):
        nonlocal ans

        if cave.name == 'end':
            ans += 1
            return

        if cave.is_small_cave and cave in visited:
            return

        if cave.is_small_cave:
            visited.add(cave)

        for connection in cave.connections:
            search(connection)

        if cave.is_small_cave:
            visited.remove(cave)

    with open(filename) as file:
        for line in file:
            line = line.strip()

            left, right = line.split('-')
            Cave.connect(left, right)

    search(caves['start'])
    print(ans)


part1()
