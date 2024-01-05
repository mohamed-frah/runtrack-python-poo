class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def calculerPerimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def calculerSurface(self):
        return self.__longueur * self.__largeur
    
    # Assesseurs et mutateurs
    def getLongueur(self):
        return self.__longueur
    
    def setLongueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur
    
    def getLargeur(self):
        return self.__largeur
    
    def setLargeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def calculerVolume(self):
        return self.__hauteur * self.calculerSurface()


rectangle = Rectangle(5, 3)


print("Périmètre du rectangle :", rectangle.calculerPerimetre())
print("Surface du rectangle :", rectangle.calculerSurface())


