# initiate a class
class employee:
     # special method/magic and method/dunder method - constructor
     def __init__(self):
        print("started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    
     def travel(self,destination):
         print("this travel method was called manually")
         print("Employee is traveling to ",destination)
    
        

    # create an object /instance of the class

sam = employee()

# rpinting the attributes 
 # print(sam.id)

# calling the method
#sam.travel("kerala")

print(type(sam))


