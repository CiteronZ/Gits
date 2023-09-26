#FinalGrades = [#pass,fail]

class Grading:

    def __init__(self, Name, Q1, Q2, Q3, Fe, CPa, Remark, GridOne, GridTwo, GridThree):
        self.Name = Name
        self.Q1 = Q1
        self.Q2 = Q2
        self.Q3 = Q3
        self.Fe = Fe
        self.CPa = CPa
        self.Remark = Remark
        self.GridOne = GridOne
        self.GridTwo = GridTwo
        self.GridThree = GridThree


    def askGrade(self):
        #Intialize input

        self.Name = input("Please Enter your name\n")
        self.GridOne.append(self.Name)

        self.Q1 = int(input("Enter your Quiz 1 score.\n"))
        self.GridOne.append(self.Q1)

        self.Q2 = int(input("Enter your Quiz 2 score.\n"))
        self.GridOne.append(self.Q2)

        self.Q3 = int(input("Enter your Quiz 3 score.\n"))
        self.GridOne.append(self.Q3)

        self.Fe = int(input("Enter your Final Exam score.\n"))
        self.GridOne.append(self.Fe)

        self.CPa = int(input("Enter your Class Participation score.\n"))
        self.GridOne.append(self.CPa)

        self.GridTwo = self.GridOne.copy()

        self.GridThree.append(self.GridTwo)

        Grading.askAgain(self)


    def askAgain(self):
        #ask Again
        usercho = input("Would you like to input grade again? y/n").lower()

        match usercho:
            case 'y' : self.GridOne.clear(), Grading.askGrade(self)
            case 'n' : Grading.printGrade(self)
            case _: print("Invalid Input (Y/N)"), Grading.askAgain(self)

    def printGrade(self):
        print("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format('Name','\t','Q1','\t','Q2','\t','Q3','\t','CP','\t','Final Exam','\t','Grade','\t','Status'))

        for x in self.GridThree:
            newq = (x[1]+x[2]+x[3])/3
            newFe = x[5] * 0.40
            newCp = x[4] * 0.20
            
            final = newq+newFe+newCp
            
            if final < 75:
                self.Remark = "Failed"
            else:
                self.Remark = "Passed"
            print("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5],'\t',final,'\t',self.Remark))





GridOne = []
GridTwo = []
GridThree = []
Gradings = Grading(None, None, None, None, None, None, None, GridOne, GridTwo, GridThree)
Gradings.askGrade()
