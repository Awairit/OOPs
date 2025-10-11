#Program for Storing sno,name ,marks and Course  by using Classes and objects
#InstanceClassLevelMembersEx1.py
class Student:
    crs="PYTHON" # Here crs is called Class Level Data Members

#Main Program
print("-----------------------------------")
#Create Two Object s1 and s2 of type student
s1=Student()
s2=Student()
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
print("Student Course=",Student.crs)
print("-"*50)
print("Second Object s2 Data")
print("-"*50)
print("Content of s2 after adding=",s2.__dict__) # {}
print("Number of Values in s2 Object after adding=",len(s2.__dict__))
for idmn,idmv in s2.__dict__.items():
    print("\t{}--->{}".format(idmn,idmv))
print("Student Course=",Student.crs)
print("-"*50)