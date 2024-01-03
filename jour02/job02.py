class livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

    def get_titre(self):
        return self.__titre
    def set_titre(self, nouv_titre):
        self.__titre = nouv_titre
    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, nouv_auteur):
        self.__auteur = nouv_auteur
    def get_pages(self):
        return self.__pages
    def set_pages(self, nouv_pages):
        if isinstance(nouv_pages, int) and nouv_pages > 0:
            self.__pages = nouv_pages
        else:
            print("Le nombre de pages doit être un nombre entier positif.")

mon_livre=livre("Voyage au bout de la nuit", "Louis-Ferdinand Céline" , 625)

print("Titre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_pages())

mon_livre.set_titre("Les Âmes mortes")
mon_livre.set_auteur("Nikolai Gogol")
mon_livre.set_pages(856)

print("Nouveau titre :", mon_livre.get_titre())
print("Nouvel auteur :", mon_livre.get_auteur())
print("Nouveau nombre de pages :", mon_livre.get_pages())

