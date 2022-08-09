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


class newstudent(student):
    pass

class extstudent(student):

    def __init__(self, name, age, grade, lang, hobbies):
        super().__init__(name, age, grade)
        self.lang = lang
        self.hobbies = hobbies

    def printreport(self):
        super().printreport()
        print('-'*50)
        print('Languages : ', self.lang)
        print('Hobbies   : ', self.hobbies)

    def addlang(self, lang):
        self.lang.append(lang)
    
    def removelang(self, lang):
        if lang in self.lang:
            self.lang.remove(lang)

    def addhobby(self, hobby):
        self.hobbies.append(hobby)
    
    def removehobby(self, hobby):
        if hobby in self.hobbies:
            self.lang.remove(hobby)

# --------------------------------------------------------- Application Developer

s = newstudent('Anil', 13, 5)
s.printreport()
s.setmarks('phy', 97)
s.setmarks('chem', 93)
s.setmarks('bio', 94)
s.setmarks('math', 95)
s.setrank(1)
s.printreport()

# --------------------------------------------------------- Application Developer
print('-' * 100)

s = extstudent('Anil', 13, 5, [], [])
s.printreport()
s.setmarks('phy', 97)
s.setmarks('chem', 93)
s.setmarks('bio', 94)
s.setmarks('math', 95)
s.setrank(1)
s.addhobby('cricket')
s.addlang('English')
s.printreport()

s1 = extstudent('Anil', 13, 5, [], [])
s2 = student('Anil', 13, 5)


print('Number of students -> ', extstudent.nstudents)

# ------------------------------------------------------------ polymorphism

# s = s1
s = s2
s.printreport()