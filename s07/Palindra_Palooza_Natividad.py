class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.OGWord = ""
        self.REVWord = ""

    #Function to remove special characters and push to LL
    def extract(self,sentence):
        exclude = [" ", ",", "!"]
        extracted = ""
        for x in sentence:
            if x in exclude:
                x = ""
            extracted += x

        for x in extracted:
            s.push(x.lower())

    #Pushes Letters in LL
    def push(self, x):
        new = Node(x)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new

    def originalLL(self):
        if self.top is None:
            print("Stack Empty!!!")

        else:
            temp = self.top
            while temp:
                self.REVWord += temp.data
                temp = temp.next

    #Reverses the LL
    def reverseLL(self):
        if self.top is None:
            print("Stack Empty!!!")
        else:
            prev = None
            current = self.top
            while current is not None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.top = prev

        # Constructs reversed LL to REVWord Variable as string
        temp = self.top
        while temp:
            self.OGWord += temp.data
            temp = temp.next

    #Checks if REVWord var and OGWord var are the same
    def checker(self):
        if self.OGWord == self.REVWord:
            print(f"Sentence is a Palindrome!")
        else:
            print("Sentence is NOT a Palindrome!")

        print(f"\nOriginal Sentence: {self.OGWord}\nReversed Sentence: {self.REVWord}")



s = Stack()
sentence = "A man, a plan, a canal, Panama!"

s.extract(sentence)
s.originalLL()
s.reverseLL()
s.checker()



