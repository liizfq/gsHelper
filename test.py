class A:
    def __init__(self):
        self.a=1
        self.b=3
    def calc(self):
        return self.a*self.b


class B:
    def __init__(self,a):
        self.a=a
        self.c=a.a
        self.d=a.b

    def set(self,value):
        self.a.a=value

a=A()
b=B(a)
print(a.calc())
b.set(4)

print(b.c)