# Class Methods as Alternative Constructors
class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
e1=employee("sujit","15")
print(e1.name)
print(e1.age)
string="Thor - 100"
e2=employee.fromstr(string)
print(e2.name)
print(e2.age)
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_string(cls,string):
        name,age=string.split(",")
        return cls(name , int(age))
person=person.from_string("rishi hero,500")
print(person.name , person.age)