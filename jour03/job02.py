class CompteBancaire : 
    def __init__(self, num_de_compte , nom , prenom, solde, decouvert=False):
        self.__num_de_compte = num_de_compte
        self.__nom = nom 
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher (self):
        print(f"Numéro de compte : {self.__num_de_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde : {self.__solde} euros")

    def affichersolde(self):
        print(f"Le solde du compte est de {self.__solde} euros")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} euros effectué avec succès.")
        self.affichersolde()
    
    def retrait (self, montant ):
        if self.__solde >= montant:
            self.__solde -= montant
            print(f"Retrait de {montant} euros effectué avec succès.")
            self.affichersolde()
        else:
            print("Solde insuffisant. Opération annulée.")

    def agios(self):
        if self.__solde < 0:
            frais = abs(self.__solde) * 0.05  # Exemple d'application d'agios à 5%
            self.__solde -= frais
            print(f"Des agios de {frais} euros ont été appliqués.")
            self.afficherSolde()

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement effectué avec succès.")
        else:
            print("Solde insuffisant pour effectuer le virement.")



compte_normal = CompteBancaire("123456789", "Dupont", "Alice", 500)


compte_normal.afficher()


compte_normal.versement(300)
compte_normal.retrait(200)
compte_normal.agios()


compte_decouvert = CompteBancaire("987654321", "Durand", "Paul", -100, decouvert=True)


compte_normal.virement(compte_decouvert, 400)
        