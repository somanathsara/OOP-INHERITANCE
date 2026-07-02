#create a class attribute "a", create an objet from it & set "a" directly using .a = 0.
#Does tis changes the class attribute.
class Demo():
    a = 10
obj = Demo()
print(obj.a)
obj.a = 0
print(obj.a)
print(Demo.a)