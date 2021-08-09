class A:
    __name="Raju" #hidden 
    def Test(self):
        print(__name)

objA=A()

# print(objA.__name) # error
# objA.Test()
print(objA._A__name)
