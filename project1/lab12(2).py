class Student:
    def __init__(self,number=None,surname=None,sex=None):
        if not number:
            self.number=input('Enter number: ')
        else:
            self.number=number
        if not surname:
            self.surname=input('Enter surname: ')
        else:
            self.surname=surname
        if not sex:
            self.sex=input('Enter sex: ')
        else:
            self.sex=sex

    def output(self):
        print("Пол студента:",self.sex)
        print("Фамилия студента:",self.surname)
        print("Номер студента:",self.number)
class DontSeeStudent(Student):
    def __init__(self,job=None,place=None):
        if not job:
            self.job=input('Enter job: ')
        else:
            self.job=job
        if not place:
            self.place=input('Enter place: ')
        else:
            self.place=place

    def output(self):
        print("Место работы студента:", self.job)
        print("Должность студента:", self.place)

student1=Student(380555555555,'Medvedev','male')
student1.output()
student2=DontSeeStudent()
student2.output()
