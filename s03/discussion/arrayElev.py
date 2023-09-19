import time
class elev:

    def __init__(self, target, floors, currentf):
        self.floors = floors
        self.currentf = currentf


    def start(self):
        move = int(input(f"What floor would you like to go to? Int only(1-15) Current Level:{self.currentf}\n"))

        if move > 15 or move < 1:
            print("Invalid 1-15 only")
            elev.start(self)

        while self.currentf != move:

            if self.currentf < move:
                self.currentf += 1
                time.sleep(1.5)
                print("Level:",self.currentf)

            elif self.currentf > move:
                self.currentf -= 1
                time.sleep(1.5)
                print("Level:",self.currentf)

        print(f"You have arrived at Level:{move}")

        again = input("Would you like to go again? y/n").lower()

        match(again):
            case "y":
                elev.start(self)
                self.currentf = move
            case "n":
                pass

floors = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15
]

newelev = elev(None,floors,1)
newelev.start()