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