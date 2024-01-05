class personne:
    def __init__(self, age=14):
        self.age = age 

    def affichage (self):
        print(f"l'age de la persson est {self.age} ans")

    def bonjour(self):
        print("hello")
    
    def modifierage (self, nouvel_age):
        self.age = nouvel_age


class eleve (personne):

    def allerecours (self):
        print ("je vais en cours")
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans.")

class professeur(personne):

    def __init__(self, matiereenseignee, age=14):
        super().__init__(age)
        self.matiereenseignee = matiereenseignee
    
    def enseigner(self):
        print("Le cours va commencer")

eleve = eleve()


eleve.bonjour()
eleve.allerEnCours()


eleve.modifierage(15)


professeur = professeur("Mathématiques", age=40)


professeur.bonjour()
professeur.enseigner()
