
class LanguageStudent:

    def __init__(self):
        self.language = []

    def add_language(self, language):
        self.language.append(language)

    def languages(self):
        return self.language

class LanguageTeacher:
    def __init__(self):
        self.language = []

    def add_language(self, language):
        self.language.append(language)

    def teach(self,student,language):
        student.add_language(language)


# To see the output, uncomment the lines below:
teacher = LanguageTeacher()
teacher.add_language('English')
student = LanguageStudent()
teacher.teach(student, 'English')
print(student.languages())