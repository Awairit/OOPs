class ClassDataMethod:
    @classmethod
    def class_method(cls):
        cls.subject="Python"
        cls.intrest="Programming"
method=ClassDataMethod()
method.class_method()
print("-"*50)
# print("I am learning {} and my intrest in {}".format(cls.subject,cls.intrest)) #NameError: name 'cls' is not defined

print("\nI am learning {} and my intrest is in {}".format(ClassDataMethod.subject,ClassDataMethod.intrest))

#=======================================================================================================================

class ClassDataMethodEx2:
    @classmethod
    def class_method(cls):
        ClassDataMethodEx2.subject="Django"
        ClassDataMethodEx2.intrest="Framework"
method=ClassDataMethodEx2()
method.class_method()
print("-"*50)
print("\nI am learning {} and my intrest is in {}".format(ClassDataMethodEx2.subject,ClassDataMethodEx2.intrest))

#=======================================================================================================================

class ClassDataMethodEx3:
    # 1. Define the class attributes EXPLICITLY to satisfy the IDE
    subject = None  # Explicitly defined class attribute
    intrest = None  # Explicitly defined class attribute

    @classmethod
    def class_method(cls):
        # 2. Assign new values to the existing class attributes
        # We can use 'cls' instead of the full class name for cleaner code
        cls.subject = "Django"
        cls.intrest = "Framework"

method = ClassDataMethodEx3()
method.class_method() # This updates the class attributes

print("-" * 50)
print("\nI am learning {} and my intrest is in {}".format(ClassDataMethodEx3.subject, ClassDataMethodEx3.intrest))