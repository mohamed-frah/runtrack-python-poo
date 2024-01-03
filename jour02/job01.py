class rectangle:
    def __init__(self, longueur , largeur):
        self.__longueur = longueur 
        self.__largeur = largeur
        
    def get_largeur(self):
        return self.__largeur
    def set_largeur(self, nouv_largeur):
        self.__largeur = nouv_largeur

    def get_longueur(self):
        return self.__longueur
    def set_longueur(self, nouv_longueur):
        self.__longueur = nouv_longueur

mon_rectangle = rectangle(10,8)

print(f"la largeur est {mon_rectangle.get_largeur}")
print(f"la longueur est {mon_rectangle.get_longueur}")

mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(7)


print("Nouvelle longueur :", mon_rectangle.get_longueur())
print("Nouvelle largeur :", mon_rectangle.get_largeur())


