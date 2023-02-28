class Student:
    def __init__(self, name, family_name, num_etudiant):
        self.__name = name
        self.__family_name = family_name
        self.__nb_credit = 0
        self.__num_etudiant = num_etudiant
        self.__grade = ""

    def add_credit(self, credit):
        self.__nb_credit += credit

    def get_credit(self):
        self.__student_eval()
        return "le nombre de credit de " + str(self.__name) + " " + str(self.__family_name) + " est de " + str(self.__nb_credit) + " points"

    def get_grade(self):
        self.__student_eval()
        return "le grade de " + str(self.__name) + " " + str(self.__family_name) + " est " + str(self.__grade)
    def student_info(self):
        self.__student_eval()
        return "\nNom : " + str(self.__family_name) + "\n" + "Prenom : " + str(self.__name) + "\nId : " + str(self.__num_etudiant) + "\nCredit : " + str(self.__nb_credit) + "\nNiveau : " + str(self.__grade) + " "
    def __student_eval(self):
        if self.__nb_credit >= 90:
            self.__grade = "Excellent"
        elif self.__nb_credit >= 80:
            self.__grade = "Très bien"
        elif self.__nb_credit >= 70:
            self.__grade = "Bien"
        elif self.__nb_credit >= 60:
            self.__grade = "Passable"
        else:
            self.__grade = "Insuffisant"

student1 = Student("John", "Doe", 145)
student1.add_credit(30)
print(student1.get_credit())
student1.add_credit(60)
print(student1.student_info())
