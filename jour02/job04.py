class Student:
    def __init__(self, prenom, nom, studentid):
        self.__prenom = prenom
        self.__nom = nom
        self.__studentid = studentid
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Identifiant étudiant: {self.__studentid}")
        print(f"Niveau: {self.__level}")


leo_messi = Student("leo", "messi", 165)

# Ajout de crédits à trois reprises
leo_messi.add_credits(50)
leo_messi.add_credits(56)
leo_messi.add_credits(30)


leo_messi.studentInfo()
