class InstanceMethodEx1:
    def instance_method(self):
        print('\nInstance method called "Instance Method"')

i=InstanceMethodEx1()
i.instance_method()

#Prohgram for Demonstrating Instance Method
#InstanceMethodEx1.py
class Student1:
    def getvals(self):
        print("ID of Current in getvals()=",id(self))


#Main Program
#Create Two Objects
s1=Student1()
s2=Student1()
#Call the Instance Method w.r.t Object
print("\nID of s1 Object in Main Program=",id(s1))
s1.getvals()
print("ID of s2 Object in Main Program=",id(s2))
s2.getvals()

#==========================================================


#Program for Reading the Values of Student by using Instance Method in OOPs
#InstanceMethodEx2.py
class Student2:
    def readstudvals(self,objinfo):
        print("Enter {} Object Information".format(objinfo))
        self.sno=int(input("\tEnter Student Number:"))
        self.name =input("\tEnter Student Name:")
        self.marks=float(input("\tEnter Student Marks:"))
    def dispstuddet(self,objinfo):
        print("-"*50)
        print("{} Student Information".format(objinfo))
        print("-" * 50)
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))
        print("-" * 50)
#Main Program
print("---------------------------------------------------")
s1=Student2()
s2=Student2()
print("Content of s1 before reading=",s1.__dict__)
print("Content of s2 before reading=",s2.__dict__)
print("---------------------------------------------------")
#Call Instance Method readstudvals() for rading the Values of s1
s1.readstudvals("First")
print("---------------------------------------------------")
#Call Instance Method readstudvals() for rading the Values of s2
s2.readstudvals("Second")
print("---------------------------------------------------")
#call instance method dispstudvals() for displying the values of s1
s1.dispstuddet("First")
#call instance method dispstudvals() for displying the values of s2
s2.dispstuddet("Second")

#================================================================

#Program for Reading the Values of Student by using Instance Method in OOPs
#InstanceMethodEx3.py
class Student3:
    def readstudvals(self,objinfo):
        print("Enter {} Object Information".format(objinfo))
        self.sno=int(input("\tEnter Student Number:"))
        self.name =input("\tEnter Student Name:")
        self.marks=float(input("\tEnter Student Marks:"))
    def dispstuddet(self,objinfo):
        print("-"*50)
        print("{} Student Information".format(objinfo))
        print("-" * 50)
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))
        print("-" * 50)
#Main Program
print("---------------------------------------------------")
s1=Student3()
s2=Student3()
print("Content of s1 before reading=",s1.__dict__)
print("Content of s2 before reading=",s2.__dict__)
print("---------------------------------------------------")
#Call Instance Method readstudvals() for rading the Values of s1
s1.readstudvals("First")
#call instance method dispstudvals() for displying the values of s1
s1.dispstuddet("First")
print("---------------------------------------------------")
#Call Instance Method readstudvals() for rading the Values of s2
s2.readstudvals("Second")
print("---------------------------------------------------")
#call instance method dispstudvals() for displying the values of s2
s2.dispstuddet("Second")

#====================================================================================

#Program for Reading the Values of Student by using Instance Method in OOPs
#InstanceMethodEx4.py
class Student4:
    def readstudvals(self,objinfo):
        print("Enter {} Object Information".format(objinfo))
        self.sno=int(input("\tEnter Student Number:"))
        self.name =input("\tEnter Student Name:")
        self.marks=float(input("\tEnter Student Marks:"))
        self.dispstuddet(objinfo) # Calling another instance Method w.r.t self

    def dispstuddet(self,objinfo):
        print("-"*50)
        print("{} Student Information".format(objinfo))
        print("-" * 50)
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))
        print("-" * 50)
#Main Program
print("---------------------------------------------------")
s1=Student4()
s2=Student4()
print("Content of s1 before reading=",s1.__dict__)
print("Content of s2 before reading=",s2.__dict__)
print("---------------------------------------------------")
#Call Instance Method readstudvals() for rading the Values of s1
s1.readstudvals("First")
print("---------------------------------------------------")
#Call Instance Method readstudvals() for rading the Values of s2
s2.readstudvals("Second")
print("---------------------------------------------------")
#call instance method dispstudvals() for displying the values of s2
s2.dispstuddet("Second")

#==================================================================================

#Program for adding  Two Number by using Classes and Objects
class Add:
    def values(self):
        self.a=float(input("Enter a number: "))
        self.b=float(input("Enter another number: "))
    def sum(self):
        self.c=self.a+self.b
    def result(self):
        print("Sum of {} and {} is {}".format(self.a, self.b, self.c))
add=Add()
add.values()
add.sum()
add.result()

#===================================================================================

#Program for adding  Two Number by using Classes and Objects
class Add:
    def values(self):
        self.a=float(input("Enter a number: "))
        self.b=float(input("Enter another number: "))
    def sum(self):
        self.c=self.a+self.b
    def result(self):
        add.values()
        add.sum()
        print("="*25)
        print("Sum of {} and {} is {}".format(self.a, self.b, self.c))

        print("-"*25)

        self.values()
        self.sum()
        print("="*25)
        print("Sum of {} and {} is {}".format(self.a, self.b, self.c))
add=Add()
add.result()

#==============================================================================

#Program for generating Mul table for a Given Number by using Classes and objects
#InstanceMethodEx6.py
class MulTable:
    def getvals(self):
        while(True):
            try:
                self.n=int(input("Enter a Number for generating Mul Table:"))
            except ValueError:
                print("\tDon't enter alnums/strs/symbols-try again")
            else:
                self.table()
                break
    def table(self):
        if(self.n<=0):
            print("\t{} is Invalid Input".format(self.n))
        else:
            print("-"*50)
            print("Mul Table for:{}".format(self.n))
            print("-" * 50)
            for i in range(1,11):
                print("\t{} x {} = {}".format(self.n,i,self.n*i))
            print("-" * 50)

#Main Program
mt=MulTable()
mt.getvals()