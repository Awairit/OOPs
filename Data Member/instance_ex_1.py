class InstanceDataMember: pass

s1=InstanceDataMember()
s2=InstanceDataMember()
s1.sno=100
s2.sno=200
print("\nMy Class Name is InstanceDataMember: {} and I'm from Obj 'InstanceDataMember()' of Class with name as s1 Variable".format(s1.sno))
print("My Class Name is InstanceDataMember: {} and I'm from Obj 'InstanceDataMember()' of Class with name as s2 Variable\n".format(s2.__dict__))

#Program for Storing sno,name and marks by using Classes and objects
#InstanceDataMembersEx1.py
class Student:pass

#Main Program
print("-----------------------------------")
#Create Two Object s1 and s2 of type student
s1=Student()
s2=Student()
print("\tID of s1=",id(s1))
print("\tID of s2=",id(s2))
#place sno,name, marks in s1 and they are called Instance Members--through an object
s1.sno=100
s1.name="Rossum"
s1.marks=3.5
#place sno,name, marks in s2 and they are called Instance Members--through an object
s2.stno=200
s2.sname="Travis"
s2.marks=5.6
#display the Instance Data Members of s1 Object
print("-"*50)
print("First Object s1 Data")
print("-"*50)
print("\tStudent Number={}".format(s1.sno))
print("\tStudent Name={}".format(s1.name))
print("\tStudent Marks={}".format(s1.marks))
print("-"*50)
print("Second Object s1 Data")
print("-"*50)
print("\tStudent Number={}".format(s2.stno))
print("\tStudent Name={}".format(s2.sname))
print("\tStudent Marks={}".format(s2.marks))
print("-"*50)
