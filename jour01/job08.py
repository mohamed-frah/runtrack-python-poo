import math 

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon              

    def changerRayon(self, nv_rayon):
        self.rayon = nv_rayon 
    
    def afficherInfos(self):
        print(f"Diamètre : {self.diametre()}")
        print(f"Aire : {self.aire()}")
        print(f"Rayon = {self.rayon}")
        print(f"Circonférence : {self.circonference()}")
        

    def circonference(self):
        return 2 * math.pi * self.rayon
    
    def aire(self):
        return math.pi * self.rayon ** 2
    
    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

print("Cercle 1 : ")
cercle1.afficherInfos()

print("")

print("Cercle 2 :")
cercle2.afficherInfos()