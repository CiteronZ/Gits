#Creating a List
'''
    List
        - are ordered, mutable(modifiable) and can contain
        elements of different data type(numbers, strings
        or objects)
            - ORDERED 
            - MUTABLE
            - HETEROGENOUS
            - INDEXED
            - SLICING
            - COMMON OPERATIONS
                -- ADD
                -- REMOVE
                -- FIND THE LENGTH
                -- INSERT
                
'''

fruits = ["banana", "apple", "strawberry", "kiwi"]

print(fruits[2])
print(fruits[3])

#negative allos us to acces list from the end
print(fruits[-1])
print(fruits[-3])

print(fruits)
fruits [1] = "mango"
print(fruits)

fruits.append("Pomelo")
print(fruits)

fruits.pop(2)
print(fruits)


#Loop throught the list
'''
    for loop is a control flow statement used for
    iterating over a sequence of items(list, tuple,
    dictionary or object)
    syntax:
        for item in iterable
            code to be executed for each item
            - for  - used to intitiate the loop
            - item - a variable that represents the
            current item in the iteration
            - in - keyword used to specify the 
            iterable or sequence you want to loop 
            through
            - iterable - sequence of items you want to 
            iterate
'''
index=0
for x in fruits:
    index+=1
    if x == "Pomelo":
        print("found at index",index)
        
        
province = ["Laguna", "Cavite", "Pampanga"]
city = ["Sta Rosa", "Dasma", "San Fernando"]

country = city + province
print(country)