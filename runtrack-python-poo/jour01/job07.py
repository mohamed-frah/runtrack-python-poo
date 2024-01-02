class Personnage :
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def droite(self):
        self.x += 1

    def bas(self):
        self.y += 1

    def gauche(self):
        self.x -= 1

    def haut(self):
        self.y -= 1

    def position(self):
        return (self.x, self.y)
    
personnage_dejeu = Personnage(0, 0)

personnage_dejeu.gauche()
personnage_dejeu.haut()
print(personnage_dejeu.position())
personnage_dejeu.droite()
personnage_dejeu.droite()
personnage_dejeu.bas()
print(personnage_dejeu.position())