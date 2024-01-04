class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1
        print(f"Le joueur {self.nom} a marqué un but !")

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        print(f"Le joueur {self.nom} a effectué une passe décisive !")

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        print(f"Le joueur {self.nom} a reçu un carton jaune.")

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        print(f"Le joueur {self.nom} a reçu un carton rouge.")

    def afficherStatistiques(self):
        print(f"Statistiques du joueur {self.nom}:")
        print(f"Buts marqués : {self.buts_marques}")
        print(f"Passes décisives : {self.passes_decisives}")
        print(f"Cartons jaunes : {self.cartons_jaunes}")
        print(f"Cartons rouges : {self.cartons_rouges}")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)
        print(f"Le joueur {joueur.nom} a été ajouté à l'équipe {self.nom}.")

    def AfficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()


# Création des joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("ramos", 4, "Defenseur")
joueur3 = Joueur("leao", 7, "Attaquant")
joueur4 = Joueur("kimmich", 6, "Millieu")

# Création des équipes
equipe1 = Equipe("bayern")
equipe2 = Equipe("marseille")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)

# Affichage des statistiques avant le match
equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

# Simuler un match avec des actions
equipe1.mettreAJourStatistiquesJoueur("Messi", "but")
equipe1.mettreAJourStatistiquesJoueur("kimmich", "passe")
equipe2.mettreAJourStatistiquesJoueur("ramos", "jaune")
equipe2.mettreAJourStatistiquesJoueur("leao", "rouge")

# Affichage des statistiques après le match
equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()
