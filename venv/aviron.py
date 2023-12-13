class Bateau:
    def __init__(self, nom, vitesse):
        self.nom = nom
        self.vitesse = vitesse
        self.distance_parcourue = 0

    def obtenir_distance_parcourue(self):
        return self.distance_parcourue

    def avancer(self):
        self.distance_parcourue += self.vitesse

class Bateau2x(Bateau):
    def __init__(self, nom, vitesse):
        super().__init__(nom, vitesse)

class BateauSkiff(Bateau):
    def __init__(self, nom, vitesse):
        super().__init__(nom, vitesse)

class Course:
    def __init__(self, type_bateau):
        self.type_bateau = type_bateau
        self.bateaux = []
        self.vainqueur_nom = None

    def ajouter_bateau_ligne_depart(self, bateau):
        if isinstance(bateau, Bateau) and type(bateau).__name__ == self.type_bateau:
            self.bateaux.append(bateau)
        else:
            print("Le bateau n'a pas pu être ajouté.")

    def demarrer(self):
        print("La course commence!")

    def est_en_cours(self):
        return any(bateau.obtenir_distance_parcourue() < 2000 for bateau in self.bateaux)

    def prochain_tour(self):
        for bateau in self.bateaux:
            bateau.avancer()

    def afficher_positions(self):
        positions = [f"{bateau.nom},{bateau.obtenir_distance_parcourue()}" for bateau in self.bateaux]
        return "\n".join(positions)

    def obtenir_vainqueur(self):
        if self.bateaux:
            vainqueur = max(self.bateaux, key=lambda bateau: bateau.obtenir_distance_parcourue())
            self.vainqueur_nom = vainqueur.nom
            return self.vainqueur_nom
        else:
            return "Aucun bateau dans la course"

