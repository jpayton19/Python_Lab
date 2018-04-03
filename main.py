# Program Name: Python Bonus Lab
# Student Names: Duncan Scott Martinson & John Payton
# Semester: Spring 2017
# Class: COSC 30403
# Instructor: Dr.James Comer
# Due Date: 5/2/2017
# Program Overview:
#   This python program uses a text file to input data into a linked list of
#   Employees and execute commands in order to manipulate the list. After every
#   command, the program writes information about the execution to a separate text file.
#   After all the data from the file has been read, the program terminates.
#
# Input:
#   The program requires formatted data in a text file entitled "Lab6Data.txt"
#
# Output:
#   The program outputs a data file entitled "Lab6Ans.txt" containing information
#   about the program's execution.
#
# Program Limitations:
#   1) The program does not allow for real time user interaction, and the output file
#  is overwritten after every execution.
#
#
# Significant Program Variables:
#   inFile - the identifier for the input file
#   outFile - the identifier for the output file
#   cmd - a string that stores the first three characters read from a line of input. This is used to
#       determine the appropriate subroutine to execute.
#   data - The linked list
#   current- an Employee "pointer" used in almost every procedure. Is used to traverse the list and
#           analyze data, manipulating it if need be.

# The employee class is used to store data from the input file in nodes of the linked list.
# It has numerous get and set functions for each of its variables
class Employee(object):
    # Constructor
    def __init__(self, num=0, name="Head", dept="", title="", pay="", nextEmp=None):
        self.num = num
        self.name = name
        self.dept = dept
        self.title = title
        self.pay = pay
        self.nextEmp = nextEmp

    def getID(self):
        return self.num

    def getName(self):
        return self.name

    def getDept(self):
        return self.dept

    def getTitle(self):
        return self.title

    def getPay(self):
        return self.pay

    def getNext(self):
        return self.nextEmp

    def setID(self, num):
        self.num = num
        return

    def setName(self, name):
        self.name = name
        return

    def setDept(self, dept):
        self.dept = dept
        return

    def setTitle(self, title):
        self.title = title
        return

    def setPay(self, pay):
        self.pay = pay
        return

    def setNext(self, nextEmp):
        self.nextEmp = nextEmp
        return

# The LinkedList class stores Employee objects in a linked list. It has the insert, delete, and update
# functions as methods, and is initialized with a head node.
class LinkedList(object):
    def __init__(self):
        self.head = Employee()

    def getHead(self):
        return self.head

# The insert function takes an Employee and inserts it into the linked list.
# It uses a temporary Employee called "current" to access information from
# the list. It looks down the list one when finding the correct spot to insert in order to
# conserve memory rather than using a doubly linked list. First, it checks to see if current is
# at the end of the list. If it is, then it inserts at the end of the list. Otherwise, it compares the
# id’s of the current node and the new one, and inserts if the new id is a lower number. Otherwise,
# it goes to the next node and repeats.
    def insert(self, newEmp):
        current = self.getHead()
        while True:
            if current.getNext() is None:
                current.nextEmp = newEmp
                return
            elif newEmp.getID() < current.getNext().getID():
                newEmp.nextEmp = current.getNext()
                current.nextEmp = newEmp
                return
            else:
                current = current.getNext()

# The delete function deletes the node with the id matching "num" from
# the list. It uses the same traversal as insert, looking one down the line to
# make it easier to connect around the deleted node. Since Python has garbage collection,
# the node is left to be collected. It uses a temporary Employee called "current"
# to access data from the nodes. If current is at the end of the list, then we didn't
# find the specified id, so we notify the user and exit. Otherwise, if the id of current.next
# matches target, we delete it from the list and exit. Otherwise, we go to the next node and repeat
    def delete(self, num):
        current = self.getHead()
        while True:
            if current.getNext() is None:
                return 1
            elif current.getNext().getID() == num:
                current.nextEmp = current.getNext().getNext()
                return 0
            else:
                current = current.getNext()
# The traverse method is a helper method for the update methods. It iterates through the list, looking for the Employee
# with id = num. IF it finds it, it returns it, otherwise, it returns a 1 to signify that the Employee doesn't exist.
    def traverse(self, num):
        current = self.getHead()
        while True:
            if current is None:
                return 1
            elif current.getID() == num:
                return current
            else:
                current = current.getNext()
# The uName, uDept, uTitle, and uRate methods update the name, department, title, and payrate respectively of an
# Employee with id = num. If the value passed by traverse() is 1, then it passes the 1 along by returning it. This
# is used for error handling. Otherwise, it updates the information of the employee.
    def uName(self, num, name):
        target = self.traverse(num)
        if target == 1:
            return 1
        else:
            target.setName(name)
            return

    def uDept(self, num, dept):
        target = self.traverse(num)
        if target == 1:
            return 1
        else:
            target.setDept(dept)
            return

    def uTitle(self, num, title):
        target = self.traverse(num)
        if target == 1:
            return 1
        else:
            target.setTitle(title)
            return

    def uRate(self, num, pay):
        target = self.traverse(num)
        if target == 1:
            return 1
        else:
            target.setPay(pay)
            return

# Prepare the I/O
inFile = open("Lab6Data.txt", encoding='utf-8')
outFile = open("Lab6Ans.txt", 'w')

# The printEmp method is a helper method that takes an Employee and prints out its info to the output file.
def printEmp(emp):
    print(str(emp.getID()).zfill(8), emp.getName(), emp.getDept(), emp.getTitle(),
          '{:0,.2f}'.format(float(emp.getPay())), file=outFile)
    return

# The printAll function traverses the list and prints out the information of each node. It uses a temporary Employee
# "current" to access data from #the nodes. If current is null, we're at the end of the list, and we break out of the
#  loop. Otherwise, we print the information out of current and then go to the next node, repeating until we hit the
# end.
def printAll(linkedList):
    current = linkedList.getHead()
    current = current.getNext()
    print("BEGIN PRINT ALL:", file=outFile)
    while True:
        if current is None:
            break
        else:
            printEmp(current)
            current = current.getNext()
    print("END PRINT ALL", file=outFile)
    return

# The printDept function works similarly to the printAll function, except it
# only prints out the employees from a specified department.
def printDept(linkedList, dept):
    current = linkedList.getHead()
    current = current.getNext()
    found = False
    print("BEGIN PRINT DEPARTMENT: {}".format(dept.strip()), file=outFile)
    while True:
        if current is None:
            break
        elif current.getDept().strip() == dept.strip():
            found = True
            printEmp(current)
            current = current.getNext()
        else:
            current = current.getNext()
    if not found:
        print("No employees in {} department.".format(dept.strip()), file=outFile)
    print("END PRINT DEPARTMENT", file=outFile)
    return

# The printID function looks for the employee with the id that matches ”num" and prints out all of its
# information. It uses a temporary Employee "current" to access the information in the nodes. It checks to see
#  if current is at the end of the list and exits the loop if it is, notifying #the user before the function
# terminates. Otherwise it checks to see if current's id matches target, printing it out and returning if it does
# and iterating if it doesnt
def printID(linkedList, num):
    current = linkedList.getHead()
    current = current.getNext()
    while True:
        if current is None:
            print("Employee #{} not found.".format(str(num).zfill(8)), file=outFile)
            return
        elif current.getID() == num:
            printEmp(current)
            return
        else:
            current = current.getNext()

# Initialize the list
data = LinkedList()
# Main loop: iterates until we hit the end of the file
while True:
    cmd = inFile.read(3)
    if cmd == '':
        break
    print(cmd.strip(), ":", sep="", end=" ", file=outFile)
# Since Python doesn't support switch statements, we had to use nested if elses to execute the proper functions
# for each command.
    if cmd == "PA ":
        printAll(data)
    elif cmd == "PI ":
        printID(data, int(inFile.read(8)))
    elif cmd == "PD ":
        printDept(data, inFile.read(15))
    elif cmd == "IN ":
        num = int(inFile.read(9))
        newEmp = Employee(num, inFile.read(12), inFile.read(16), inFile.read(16),
                          '{:0,.2f}'.format(float(inFile.read(5))))
        data.insert(newEmp)
        print("Employee #{} inserted".format(str(num).zfill(8)), file=outFile)
    elif cmd == "DE ":
        num = int(inFile.read(9))
        if data.delete(num) == 1:
            print("ERROR: Employee #{} not found.".format(str(num).zfill(8)), file=outFile)
        else:
            print("Employee #{} deleted".format(str(num).zfill(8)), file=outFile)
    elif cmd == "UN ":
        num = int(inFile.read(8))
        inFile.read(29)
        name = inFile.read(12)
        if data.uName(num, name) == 1:
            print("ERROR: Employee #{} not found.".format(str(num).zfill(8)), file=outFile)
        else:
            print("Employee #{} name updated to {}".format(str(num).zfill(8), name.strip()), file=outFile)
    elif cmd == "UD ":
        num = int(inFile.read(8))
        inFile.read(29)
        dept = inFile.read(16)
        if data.uDept(num, dept) == 1:
            print("ERROR: Employee #{} not found.".format(str(num).zfill(8)), file=outFile)
        else:
            print("Employee #{} department updated to {}".format(str(num).zfill(8), dept.strip()), file=outFile)
    elif cmd == "UT ":
        num = int(inFile.read(8))
        inFile.read(29)
        title = inFile.read(16)
        if data.uTitle(num, title) == 1:
            print("ERROR: Employee #{} not found.".format(str(num).zfill(8)), file=outFile)
        else:
            print("Employee #{} title updated to {}".format(str(num).zfill(8), title.strip()), file=outFile)
    elif cmd == "UR ":
        num = int(inFile.read(8))
        inFile.read(29)
        pay = inFile.read(5)
        if data.uRate(num, pay) == 1:
            print("ERROR: Employee #{} not found.".format(str(num).zfill(8)), file=outFile)
        else:
            print("Employee #{} payrate updated to {}".format(str(num).zfill(8), '{:0,.2f}'.format(float(pay.strip()))),
                  file=outFile)
    # Set the file pointer to the next line
    inFile.readline()
# Close the I/O
outFile.flush()
inFile.close()
outFile.close()
# End of program
