class Repository:
    def __init__(self):
        self.packages = {}

    def add_package(self, package):
        self.packages[package.name] = package

    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result

# two different classes are related but no inheritance involved this is composition


repo = Repository()

repo.add_package(numpy)
repo.add_package(sololearn)
repo.add_package(heapq)
repo.add_package(astroid)

print(repo.total_size())
