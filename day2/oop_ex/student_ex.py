class student:

    nstudents = 0 # Class variable

    # Data 
    # name, age, grade
    # subject marks, average, rank
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = { 'phy':0, 'chem':0, 'math':0, 'bio':0 }
        self.avg = 0
        self.rank = 0
        student.nstudents += 1

    # Functions

    def printreport(self):
        print('Name of the student : ', self.name)
        print('Age                 : ', self.age)
        print('Grade               : ', self.grade)
        print('-'*50)
        print('Physics       : ', self.marks['phy'])
        print('Chemistry     : ', self.marks['chem'])
        print('Maths         : ', self.marks['math'])
        print('Biology       : ', self.marks['bio'])
        print('-'*50)
        print('AVERAGE       : ', self.avg)
        print('RANK ', self.rank)

    def setmarks(self, subj, marks):
        if subj in self.marks.keys():
            self.marks[subj] = marks
        self.calcavg()

    def calcavg(self):
        self.avg = sum(self.marks.values())/4

    def setrank(self, rank):
        self.rank = rank

# --------------------------------------------------------- Application Developer

s = student('Anil', 13, 5)
s.printreport()
s.setmarks('phy', 97)
s.setmarks('chem', 93)
s.setmarks('bio', 94)
s.setmarks('math', 95)
s.setrank(1)
s.printreport()
