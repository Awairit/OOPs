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
print("\n\nID of s1 Object in Main Program=",id(s1))
s1.getvals()
print("ID of s2 Object in Main Program=",id(s2))
s2.getvals()