class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

 
    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
        else:
            print("Le réservoir est trop bas pour démarrer la voiture.")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir > 5

    def get_reservoir(self):
        return self.__reservoir

# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture("bmw", "m8", 2023, 11500)
ma_voiture.set_kilometrage(15000)

ma_voiture.demarrer()
print(f"La voiture est en marche : {ma_voiture.get_en_marche()}")

ma_voiture.arreter()
print(f"La voiture est en marche : {ma_voiture.get_en_marche()}")
