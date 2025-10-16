class ClassDataMember:
    subject= "Python"

print("The class level data member 'student' value is {} of class 'ClassDataMember'".format(ClassDataMember.subject))

#=======================================================================================================================


#ClassLevelDataMembersEx1.py
class Student:
    crs="PYTHON" # Here crs is called Class Level Data Member

#main Program
print("Course name=",Student.crs)

#=======================================================================================================================

#ClassLevelDataMembersEx2.py
class Student:pass


#main Program
Student.crs="PYTHON" # Here crs is called Class Level Data Member
print("Course name={}".format(Student.crs))