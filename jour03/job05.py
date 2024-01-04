import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))

    def lancerJeu(self):
        niveaux_vie = {1: 100, 2: 150, 3: 200}
        vie_joueur = niveaux_vie[self.niveau]
        vie_ennemi = niveaux_vie[self.niveau]

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        print(f"Un ennemi redoutable apparaît avec {vie_ennemi} points de vie !")

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} est vaincu ! Félicitations, vous avez gagné !")
                break
            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu. Vous avez perdu.")
                break

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
