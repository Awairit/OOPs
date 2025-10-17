# class ClassDataMethod:
#     @classmethod
#     def class_method(cls):
#         cls.subject="Python"
#         cls.intrest="Programming"
# method=ClassDataMethod()
# method.class_method()
# print("-"*50)
# # print("I am learning {} and my intrest in {}".format(cls.subject,cls.intrest)) #NameError: name 'cls' is not defined
#
# print("\nI am learning {} and my intrest is in {}".format(ClassDataMethod.subject,ClassDataMethod.intrest))
#
# #=======================================================================================================================
#
# class ClassDataMethodEx2:
#     @classmethod
#     def class_method(cls):
#         ClassDataMethodEx2.subject="Django"
#         ClassDataMethodEx2.intrest="Framework"
# method=ClassDataMethodEx2()
# method.class_method()
# print("-"*50)
# print("\nI am learning {} and my intrest is in {}".format(ClassDataMethodEx2.subject,ClassDataMethodEx2.intrest))
#
# #=======================================================================================================================
#
# class ClassDataMethodEx3:
#     # 1. Define the class attributes EXPLICITLY to satisfy the IDE
#     subject = None  # Explicitly defined class attribute
#     intrest = None  # Explicitly defined class attribute
#
#     @classmethod
#     def class_method(cls):
#         # 2. Assign new values to the existing class attributes
#         # We can use 'cls' instead of the full class name for cleaner code
#         cls.subject = "Django"
#         cls.intrest = "Framework"
#
# method = ClassDataMethodEx3()
# method.class_method() # This updates the class attributes
#
# print("-" * 50)
# print("\nI am learning {} and my intrest is in {}".format(ClassDataMethodEx3.subject, ClassDataMethodEx3.intrest))

#=======================================================================================================================

class ClassDataMethodEx4:

    # city = None

    @classmethod
    def subject(cls):
        cls.subject2="Python"
        specialist = "Dr. Irshad"
        try:
            cls.rollnumber = int(input("Enter the Roll Number: "))
            cls.name=input("Enter the Student Name: ")
            # ClassDataMethodEx4.rollnumber= int(input("Enter the Roll Number: ")) #ClassDataMethodEx4.rollnumber = cls.rollnumber
        except Exception as e:
            print(e)
        else:
            print("The Name is: {}".format(cls.name))
            print("Roll Number is: {}".format(cls.rollnumber))
            # print("Roll Number =",ClassDataMethodEx4.rollnumber)

        finally:
            print("The Subject is: {}".format(cls.subject2))

            print("The FrameWork is: {}" .format("Django"))

        cls.framework(specialist)

    @classmethod
    def framework(cls, instructor):
        print("The Framework is Taught by: {} specialist".format(instructor))
        ClassDataMethodEx4.city = "HYD"  # OR cls.city="HYD"


obj_call=ClassDataMethodEx4()
obj_call.subject()
print("Student City=",ClassDataMethodEx4.city)

print("Eager to learn {}" .format(obj_call.subject2))


# ClassDataMethodEx4.subject("Swift")

