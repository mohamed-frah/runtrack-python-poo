class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {} 
        self.__statut = "En cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats_commandes[nom_plat] = {'prix': prix_plat, 'statut': self.__statut}

    def annuler_commande(self):
        self.__statut = "Annulée"
        for plat in self.__plats_commandes:
            self.__plats_commandes[plat]['statut'] = self.__statut

    def __calculer_total(self):
        total = sum(plat['prix'] for plat in self.__plats_commandes.values() if plat['statut'] != "Annulée")
        return total

    def afficher_commande(self):
        total = self.__calculer_total()
        print(f"Numéro de commande : {self.__numero_commande}")
        print("Plats commandés :")
        for plat, details in self.__plats_commandes.items():
            print(f"- {plat} : {details['prix']} $ - Statut : {details['statut']}")
        print(f"Total à payer : {total} $")

    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * (taux_tva / 100)
        return tva


commande1 = Commande("CMD001")
commande1.ajouter_plat("Pizza", 15)
commande1.ajouter_plat("Salade", 6)
commande1.ajouter_plat("Boisson", 2)

commande1.annuler_commande()
commande1.afficher_commande()

tva = commande1.calculer_tva(10)
print(f"TVA à payer : {tva} $")
