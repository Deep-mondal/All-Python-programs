class personal:
    def pri(self):
        self.name=input("Enter your name")
        self.age=int(input("Enter your age"))
        self.add=input("Enter your address")
    def sec(self):
        self.phno=int(input("Enter your Phone number"))
        self.eml=input("Enter your Email address")
class student(personal):
    def academic(self):
        self.standard=input("Enter your Class")
        self.div=input("Entyer your division")
        self.roll=int(input("Enter your roll number"))
class faculty(personal):
    def sub(self):
        self.subject=input("Enter your subject")                #incomplete
stn_name=[]
fac_name=[]
stn_std=[]
s=student()
f=faculty()
n=int(input("Enter the no of students"))
for i in range(1,n):
    s.pri()
    s.academic()
    if(self.div==)
