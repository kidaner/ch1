class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def __str__(self):
        return f"Current floor: {self.current}"

    def up(self):
        """Makes the elevator go up one floor."""
        self.current += 1
        if self.current >= 10:
            self.current = 10
        return self.current

    def down(self):
        """Makes the elevator go down one floor."""
        self.current -= 1
        if self.current <= -1:
            self.current = -1
        return self.current

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        if self.current <= -1:
            self.current = -1
        if self.current >= 10:
            self.current = 10
        return self.current


elevator = Elevator(-1, 10, 0)
elevator.go_to(5)
print(elevator)
