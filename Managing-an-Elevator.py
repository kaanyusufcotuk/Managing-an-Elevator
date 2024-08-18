class Floor:
    def __init__(self, floor_number, called=False, calling=False):
        self.floor_number = floor_number
        self.called = called
        self.calling = calling

class Elevator:
    def __init__(self, floor=0, floors=None):
        self.floor = floor
        self.floors = floors if floors is not None else []
        self.direction = None
        self.set_direction()

    def __str__(self):
        floors_str = ', '.join(str(floor.floor_number) for floor in self.floors)
        direction_str = 'Up' if self.direction else 'Down' if self.direction is not None else 'None'
        return f"Elevator at Floor {self.floor}, Direction: {direction_str}, Floors: [{floors_str}]"
    
    def call_floor(self, target_floor):
        for f in self.floors:
            if f.floor_number == target_floor:
                f.calling = True
                self.set_direction()
                return f"Floor {target_floor} has called the elevator."
        return f"Floor {target_floor} does not exist."
    
    def set_direction(self):
        if any(f.calling or f.called for f in self.floors):
            if self.direction is None:
                for f in self.floors:
                    if f.calling or f.called:
                        self.direction = f.floor_number > self.floor
                        break
        else:
            self.direction = None
    
    def move_elevator(self):
        while self.direction is not None:
            if self.direction:  # Moving up
                for f in sorted(self.floors, key=lambda x: x.floor_number):
                    if f.floor_number > self.floor:
                        self.floor = f.floor_number
                        if f.calling or f.called:
                            f.calling = False
                            f.called = False
                            self.set_direction()
                            print(f"Stopped at Floor {self.floor}")
                            break
            else:  # Moving down
                for f in sorted(self.floors, key=lambda x: -x.floor_number):
                    if f.floor_number < self.floor:
                        self.floor = f.floor_number
                        if f.calling or f.called:
                            f.calling = False
                            f.called = False
                            self.set_direction()
                            print(f"Stopped at Floor {self.floor}")
                            break
            
            # Check if all calls are handled
            if not any(f.calling or f.called for f in self.floors):
                self.direction = None
                print("Elevator has stopped.")
                break
    
    def return_floor_list(self):
        return self.floors


# Example Usage:

# Define floors
floors = [Floor(i) for i in range(1, 6)]  # Floors 1 to 5

# Initialize elevator at floor 1 with the list of floors
elevator = Elevator(floor=1, floors=floors)

# Print the initial state of the elevator
print(elevator)

# Call the elevator to floor 4
print(elevator.call_floor(4))

# Call the elevator to floor 2
print(elevator.call_floor(2))

# Move the elevator to handle the calls
elevator.move_elevator()

# Print the final state of the elevator
print(elevator)
