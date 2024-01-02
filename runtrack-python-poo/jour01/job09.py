class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.prixHT + (self.prixHT * self.TVA / 100)
    
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom 

    def afficher(self):
        return (self.nom, self.prixHT, self.TVA, self.CalculerPrixTTC())
    
    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
    
   
    
    def getPrixHT(self):
        return self.prixHT
    
    def getTVA(self):
        return self.TVA
    
    def getnom(self):
        return self.nom 