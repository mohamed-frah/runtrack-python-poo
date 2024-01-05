class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")
    
    def afficherX(self):
        print(f"La coordonnée x du point : {self.x}")
    
    def afficherY(self):
        print(f"La coordonnée y du point : {self.y}")
    
    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x
    
    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y


point = Point(15,2)


point.afficherLesPoints()


point.afficherX()
point.afficherY()


point.changerX(6)
point.changerY(14)


point.afficherLesPoints()
