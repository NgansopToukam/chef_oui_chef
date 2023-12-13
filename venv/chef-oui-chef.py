from check_salute import verifier_salutations
from aviron import Bateau, Bateau2x, BateauSkiff, Course

# Utilisez les fonctions et les classes ici
course_cadets = Course('2x')
bateau_1_2x = Bateau2x('mickey', 500)
bateau_2_2x = Bateau2x('minnie', 70)
bateau_3_skiff = BateauSkiff('picsou', 120)
course_cadets.ajouter_bateau_ligne_depart(bateau_1_2x)
course_cadets.ajouter_bateau_ligne_depart(bateau_2_2x)
course_cadets.ajouter_bateau_ligne_depart(bateau_3_skiff)

course_cadets.demarrer()
while course_cadets.est_en_cours():
    course_cadets.prochain_tour()

print(course_cadets.afficher_positions())
print(course_cadets.obtenir_vainqueur())

print(verifier_salutations("-->>----<<--"))  # Réponse attendue : 4
print(verifier_salutations("--->--->----->--"))  # Réponse attendue : 0
print(verifier_salutations("--->>----<<---"))  # Réponse attendue : 4