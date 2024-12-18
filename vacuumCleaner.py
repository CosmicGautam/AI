import time

class VacuumCleaner:
    CLEAN = 'Clean'
    DIRTY = 'Dirty'

    def __init__(self):
        # Initialize user input variables
        self.room_a_status = self.DIRTY
        self.room_b_status = self.DIRTY
        self.current_location = 'A'

    def draw_environment(self):
        print(f"Room A: {self.room_a_status}  Room B: {self.room_b_status}")

    def scan_and_clean(self, room):
        status = getattr(self, f"room_{room.lower()}_status")
        if status == self.DIRTY:
            setattr(self, f"room_{room.lower()}_status", self.CLEAN)
            return True
        else:
            return False

    def move_left(self):
        self.current_location = 'A'

    def move_right(self):
        self.current_location = 'B'

    def run(self):
        print("Initial environment (Before cleaning):")
        self.draw_environment()
        while any(status == self.DIRTY for status in [self.room_a_status, self.room_b_status]):
            while self.scan_and_clean(self.current_location):
                print(f"\nCleaning in Room {self.current_location}...")
                time.sleep(1)
                self.draw_environment()
            if self.current_location == 'A':
                self.move_right()
            else:
                self.move_left()
            print(f"\nMoving to Room {self.current_location}...")
            time.sleep(1)
            self.draw_environment()
        print("\nFinal environment (After cleaning):")
        self.draw_environment()
        print("\nAll rooms are clean. Task completed.")

if __name__ == "__main__":
    vacuum = VacuumCleaner()
    vacuum.run()
