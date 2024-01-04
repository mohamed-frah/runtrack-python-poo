class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - Statut: {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tâche '{titre}' supprimée avec succès.")
                return
        print(f"Tâche '{titre}' introuvable.")

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Terminée"
                print(f"Tâche '{titre}' marquée comme terminée.")
                return
        print(f"Tâche '{titre}' introuvable.")

    def afficherListe(self):
        if not self.taches:
            print("La liste de tâches est vide.")
        else:
            print("Liste de tâches:")
            for tache in self.taches:
                print(tache)

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        if not filtered_list:
            print(f"Aucune tâche avec le statut '{statut}'.")
        else:
            print(f"Tâches avec le statut '{statut}':")
            for tache in filtered_list:
                print(tache)

# Création des tâches
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Répondre aux emails", "Répondre aux emails professionnels")
tache3 = Tache("Faire du sport", "Faire une séance de jogging")

# Création de la liste de tâches
liste_taches = ListeDeTaches()

# Ajout des tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Affichage de la liste de tâches
liste_taches.afficherListe()

# Marquer une tâche comme terminée
liste_taches.marquerCommeFinie("Faire les courses")

# Affichage des tâches restantes à faire
liste_taches.filterListe("À faire")

# Supprimer une tâche de la liste
liste_taches.supprimerTache("Répondre aux emails")

# Affichage final de la liste de tâches
liste_taches.afficherListe()
