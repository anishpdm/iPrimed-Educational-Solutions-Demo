import validationModule

class Student:
    def __init__(self):
        self.name=''
        self.roll=''
    def setName(self,name):
        self.name=name
    def setRoll(self,roll):
        self.roll=roll
    def getName(self):
        return self.name
    def getRoll(self):
        return self.roll  

class Marks(Student):
    def __init__(self):
        self.eng=''
        self.maths=''
        

    def setEnglish(self,eng):
        self.eng=eng 
    def setMaths(self,maths):
        self.maths=maths
    def getEnglish(self):
        return self.eng
    def getMaths(self):
        return self.maths                 

studentdata=[]
obj=Marks()

n=input("Enter a name")
r=input("Enter a Rollnumber")
m=input("Enter Maths marks")
e=input("Enter English marks ")

#***********  Setting Values  *********#
obj.setName(n)
obj.setRoll(r)
obj.setMaths(m)
obj.setEnglish(e)
#***********  Setting Values  *********#


#***********  Create Dictionary  *********#

dict={"name":obj.getName(),"roll":obj.getRoll(),"eng":obj.getEnglish(),"maths":obj.getMaths()}

#***********  Create Dictionary  *********#


studentdata.append(dict)

print(studentdata)


           

   

    
    
