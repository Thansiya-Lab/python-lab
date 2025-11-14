class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            print(self.name,"got an A grade")
        elif self.marks>=80:
            print(self.name,"got an B grade")
        else:
            print(self.name,"got an C grade")
s1=student("Rahul",92)
s2=student("Rohan",82)
s3=student("Pooja",72)
s1.grade()
s2.grade()
s3.grade()
            
