class InstanceMethodEx1:
    def instance_method(self):
        print('\nInstance method called "Instance Method"')

i=InstanceMethodEx1()
i.instance_method()

#Prohgram for Demonstrating Instance Method
#InstanceMethodEx1.py
class Student:
    def getvals(self):
        print("ID of Current in getvals()=",id(self))


#Main Program
#Create Two Objects
s1=Student()
s2=Student()
#Call the Instance Method w.r.t Object
print("\nID of s1 Object in Main Program=",id(s1))
s1.getvals()
print("ID of s2 Object in Main Program=",id(s2))
s2.getvals()

#==========================================================


#Program for Reading the Values of Student by using Instance Method in OOPs
#InstanceMethodEx2.py
class Student:
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
s1=Student()
s2=Student()
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