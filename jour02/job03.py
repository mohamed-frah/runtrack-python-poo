class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre
    
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur
    
    def get_nombre_pages(self):
        return self.__nombre_pages
    
    def set_nombre_pages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self.__nombre_pages = nouveau_nombre_pages
        else:
            print("Le nombre de pages doit être un nombre entier positif.")
    
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")
    
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre est déjà disponible.")

# Exemple d'utilisation
mon_livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1000)

# Vérification de la disponibilité du livre
print("Disponibilité initiale :", mon_livre.verification())

# Emprunt du livre
mon_livre.emprunter()

# Tentative de réemprunt du livre
mon_livre.emprunter()

# Rendre le livre
mon_livre.rendre()

# Vérification de la disponibilité après le rendu
print("Disponibilité après le rendu :", mon_livre.verification())
