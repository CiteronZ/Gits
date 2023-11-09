class task_Manager:
    def __init__(self, MaxSize):
        self.MaxSize = MaxSize
        self.Top = -1
        self.arr = []
        self.tmparr = []

    def is_Full(self):
        return self.Top == self.MaxSize - 1

    def is_Empty(self):
        return self.Top == -1

    def exit(self):
        exit()
    def remove_Task(self):
        if task_Manager.is_Empty(self):
            print("Your currently have no tasks to remove!")
            task_UI.start(self)
        else:
            print(f"\nTask {self.Top + 1} Removed!")
            self.arr.pop(self.Top)
            self.Top -= 1

            task_UI.start(self)

    def mark_Task(self):
        if task_Manager.is_Empty(self):
            print("Your currently have no tasks to mark!")
            task_UI.start(self)
        else:
            mrk = int(input("Enter Task no. to mark"))

            if mrk < 1 or mrk > len(self.arr):
                print(f"Your tasks do not reach no.{mrk}")
                task_UI.start(self)
            else:
                self.arr[mrk-1][2] = True

                print(f"\nTask {mrk} marked Succesfully")

                task_UI.start(self)

    def add_Task(self):
        if task_Manager.is_Full(self):
            print("Too many tasks! Complete them first")
            task_UI.start(self)
        else:
            task = input("\nInput Task: ")
            desc = input("Description: ")

            self.Top += 1
            self.tmparr.append(task)
            self.tmparr.append(desc)
            self.tmparr.append(False)

            tmp = self.tmparr.copy()
            self.arr.append(tmp)
            self.tmparr.clear()

            task_UI.start(self)

    def display_Task(self):
        if task_Manager.is_Empty(self):
            print("Your currently have no tasks to mark!")
            task_UI.start(self)

        else:
            print(f"Tasks {len(self.arr)}/{self.MaxSize}")

            for tasks in range(len(self.arr)):
                print(f"\n-------------------\nTask no. {tasks+1}\nTitle: {self.arr[tasks][0]}\nDescription: "
                      f"{self.arr[tasks][1]}\nComplete: {self.arr[tasks][2]}\n-------------------\n")

            task_UI.start(self)

class task_UI(task_Manager):

    def start(self):
        inp = int(input("\nHello! Welcome to your Task Manager.\n1.Add Task\n2.Mark/Complete Tasks\n3.Display "
                        "Tasks\n4.Remove Task\n5.Exit\n"))
        match inp:
            case 1: task_Manager.add_Task(self)
            case 2: task_Manager.mark_Task(self)
            case 3: task_Manager.display_Task(self)
            case 4: task_Manager.remove_Task(self)
            case 5: task_Manager.exit(self)


new = task_UI(3)
new.start()



