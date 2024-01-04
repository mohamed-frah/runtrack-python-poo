class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nom(self):
        return self.__nom

    def get_nb_habitants(self):
        return self.__nb_habitants

    def incrementer_habitants(self):
        self.__nb_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville

    def ajouterPopulation(self):
        self.__ville.incrementer_habitants()


ville_paris = Ville("Paris", 1000000)
print(f"Nombre d'habitants à Paris : {ville_paris.get_nb_habitants()}")

ville_marseille = Ville("Marseille", 861635)
print(f"Nombre d'habitants à Marseille : {ville_marseille.get_nb_habitants()}")


john = Personne("John", 45, ville_paris)
john.ajouterPopulation()

myrtille = Personne("Myrtille", 4, ville_paris)
myrtille.ajouterPopulation()

chloe = Personne("Chloé", 18, ville_marseille)
chloe.ajouterPopulation()


print(f"Nombre d'habitants à Paris après ajout : {ville_paris.get_nb_habitants()}")
print(f"Nombre d'habitants à Marseille après ajout : {ville_marseille.get_nb_habitants()}")


