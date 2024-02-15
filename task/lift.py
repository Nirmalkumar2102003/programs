class Elevator:
    def __init__(self, total_floors):
        self.total_floors = total_floors
        self.current_floor = 0

    def move(self, reach_floor):
        if reach_floor < 0 or reach_floor > self.total_floors:
            print("Invalid floor number.")
            return

        if self.current_floor < reach_floor:
            print("Elevator is going up from floor", self.current_floor, "to", reach_floor)
        elif self.current_floor > reach_floor:
            print("Elevator is going down from floor", self.current_floor, "to", reach_floor)
        else:
            print("Elevator is already on floor", reach_floor)

        self.current_floor = reach_floor


total_floors = 10
lift = Elevator(total_floors)

while True:
    destination = int(input("Enter the destination floor (0 to {}): ".format(total_floors)))
    lift.move(destination)
    if destination < 0 or destination > total_floors:
        print("Invalid input. Please enter a valid floor number.")
    else:
        break
