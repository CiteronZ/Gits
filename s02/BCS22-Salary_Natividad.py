class bonus_Calc:

    def __init__(self, Salary, Year):
        self.Salary = Salary #O(1)
        self.Year = Year #O(1)
        self.Final = None #O(1)
        self.O = 0 #O(1)


    def in_Emp(self):
        self.Salary = float(input("Input your monthly salary:\n")) #O(1)
        self.Year = int(input("Input your years of service\n")) #O(1)

    def calc(self):

        if self.Year == 5:
            x = self.Salary * (5/100)
            self.Final = x + self.Salary
        elif self.Year == 10:
            x = self.Salary * (100/100)
            self.Final = x + self.Salary
        elif self.Year == 15:
            x = self.Salary * (150/100)
            self.Final = x + self.Salary
        elif self.Year >= 20:
            x = self.Salary * (200/100)
            self.Final = x + self.Salary
        elif self.Year < 5:
            print("Not qualified for Bonus")

        self.O = 4

        return print(f"The Longevity of the bonus: {x}, the final salary being: {self.Final}")

    #def findO(self):





newEmp = bonus_Calc(None,None)
newEmp.in_Emp()
newEmp.calc()




