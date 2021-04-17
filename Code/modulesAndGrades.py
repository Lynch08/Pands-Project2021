#A programme to input student names and modules and the grades recieved
#Author Enda Lynch
#REF - Andrew Beatty, Lab Sheet and Video 6.1
#REF - https://www.w3schools.com/python/python_functions.asp


# This is the initial input - asking the user which function to call
def displayMenu():
    print("What would you like to do?")
    print("(a) Add new student")
    print("(v) View students")
    print("(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

#function to add students info that has been inputted
def doAdd():
    currentStudent = {}
    currentStudent ["Name"] = input ("Enter Students Name:")
    currentStudent ["Modules"] = readModules()
    students.append(currentStudent)

#function to  input module information
def readModules():
    modules = []
    moduleName = input("Enter the first module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        #no error handeling
        module["grade"] = int(input("Enter Grade:"))
        modules.append(module)
        #reading in next module
        moduleName = input("Enter next module name (blank to quit):").strip()
        
    return modules
def displayModules(modules):
    print("\tName      \tGrade")
    for module in modules:
        print("\t{}   |t{}".format(module["name"], module["grade"]))

def doView():
    for currentStudent in students: 
        print(currentStudent["Name"])
        displayModules(currentStudent["Modules"])

students = []
choice = displayMenu()
while(choice != 'q'):

    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
    elif choice != "q":
        print ("\n\n please select either 'a'/'v'/'q'")
    choice = displayMenu()

