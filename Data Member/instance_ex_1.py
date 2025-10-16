class InstanceDataMember: pass

s1=InstanceDataMember()
s2=InstanceDataMember()
s1.sno=100
s2.sno=200
print("\nMy Class Name is InstanceDataMember: {} and I'm from Obj 'InstanceDataMember()' of Class with name as s1 Variable".format(s1.sno))
print("My Class Name is InstanceDataMember: {} and I'm from Obj 'InstanceDataMember()' of Class with name as s2 Variable\n".format(s2.__dict__))

#================================================================================================================================================

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

#=======================================================================================================================


#Program for Storing sno,name and marks by using Classes and objects
#InstanceDataMembersEx2.py
class StudentDictionary:pass

#Main Program
print("-----------------------------------")
#Create Two Object s1 and s2 of type student
s1=StudentDictionary()
s2=StudentDictionary()
print("Content of s1 before adding=",s1.__dict__) # {}
print("Content of s2 before adding=",s2.__dict__) # {}
print("Number of Values in s1 Object before adding=",len(s1.__dict__))
print("Number of Values in s2 Object before adding=",len(s2.__dict__))
#place sno,name, marks in s1 and they are called Instance Members--through an object
s1.sno=100
s1.name="Rossum"
s1.marks=3.5
#place sno,name, marks in s2 and they are called Instance Members--through an object
s2.stno=200
s2.sname="Travis"
s2.marks=5.6
s2.cname="JNTU"
#display the Instance Data Members of s1 Object
print("-"*50)
print("First Object s1 Data")
print("-"*50)
print("Content of s1 after adding=",s1.__dict__) # {}
print("Number of Values in s1 Object after adding=",len(s1.__dict__))
for idmn,idmv in s1.__dict__.items():
    print("\t{}--->{}".format(idmn,idmv))
print("-"*50)
print("Second Object s2 Data")
print("-"*50)
print("Content of s2 after adding=",s2.__dict__) # {}
print("Number of Values in s2 Object after adding=",len(s2.__dict__))

for idmn,idmv in s2.__dict__.items(): #The items() function (or technically, a method) in Python dictionaries returns all key-value pairs as a view object —/
    print("\t{}--->{}".format(idmn, idmv))  # meaning it shows you the contents of the dictionary as (key, value) tuples.
print("-"*50)