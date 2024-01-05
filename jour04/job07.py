import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        for couleur in couleurs:
            for valeur in range(2, 11):
                self.paquet.append(Carte(str(valeur), couleur))
            for figure in ['Valet', 'Dame', 'Roi']:
                self.paquet.append(Carte('10', couleur))
            self.paquet.append(Carte('As', couleur))

    def distribuer_cartes(self):
        main_joueur = []
        main_croupier = []
        random.shuffle(self.paquet)
        for _ in range(2):
            main_joueur.append(self.paquet.pop())
            main_croupier.append(self.paquet.pop())
        return main_joueur, main_croupier

    def valeur_carte(self, carte):
        if carte.valeur.isdigit():
            return int(carte.valeur)
        elif carte.valeur != 'As':
            return 10
        else:
            return 11  # Retourne 11 par défaut pour l'As, à moins que cela ne dépasse 21

    def total_main(self, main):
        total = 0
        as_present = False
        for carte in main:
            valeur = self.valeur_carte(carte)
            if carte.valeur == 'As':
                as_present = True
            total += valeur
        if as_present and total > 21:
            total -= 10  # Si un As est présent et que le total dépasse 21, l'As vaut 1 au lieu de 11
        return total

    def jouer(self):
        joueur, croupier = self.distribuer_cartes()
        while True:
            print("Main du joueur:")
            for carte in joueur:
                print(f"{carte.valeur} de {carte.couleur}")
            total_joueur = self.total_main(joueur)
            print(f"Total du joueur: {total_joueur}")

            if total_joueur == 21:
                print("Blackjack ! Le joueur gagne !")
                break
            elif total_joueur > 21:
                print("Le joueur a dépassé 21. Le croupier gagne.")
                break

            choix = input("Prendre une carte ? (Oui/Non) ").lower()
            if choix == 'oui':
                joueur.append(self.paquet.pop())
            else:
                break

        total_croupier = self.total_main(croupier)
        while total_croupier < 17:
            croupier.append(self.paquet.pop())
            total_croupier = self.total_main(croupier)

        print("\nMain du croupier:")
        for carte in croupier:
            print(f"{carte.valeur} de {carte.couleur}")
        print(f"Total du croupier: {total_croupier}")

        if total_croupier > 21:
            print("Le croupier a dépassé 21. Le joueur gagne !")
        elif total_croupier > total_joueur:
            print("Le croupier gagne.")
        elif total_croupier < total_joueur:
            print("tu as gagne !")
        else:
            print("Égalité !")

# Exemple d'utilisation
jeu = Jeu()
jeu.jouer()
