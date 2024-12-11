fichier_taches= "taches.txt"

# Charger les tâches depuis un fichier texte
def charger_taches_txt():
    taches = []
    with open(fichier_taches, "a+", encoding="utf-8") as fichier:
      fichier.seek(0)  
      for i in fichier:
            if i.strip(): 
                titre, description, termine = i.strip().split("|")
                taches.append({
                    "titre": titre,
                    "description": description,
                    "termine": termine == "True"  
                })
    return taches

# Sauvegarder les tâches dans un fichier texte
def sauvegarder_taches_txt(taches):
  with open(fichier_taches, "w", encoding="utf-8") as fichier:
    for j in taches:
            fichier.write(f"{j['titre']}|{j['description']}|{j['termine']}\n")

# Afficher les tâches
def afficher_taches(taches):
    if not taches:
        print("Aucune tâche à afficher.")
        return
    print("=== Liste des tâches ===")
    for i, tache in enumerate(taches, start=1):
         if tache["termine"] :
            statut = "[X]"
         else :statut ="[ ]"
         print(f"{i}. {statut} {tache['titre']} - {tache['description']}")

# ajouter tache
def ajouter_tache(taches):
    titre = input("Entrez le titre de la tâche : ")
    description = input("Entrez une description : ")
    taches.append({"titre": titre, "description": description, "termine": False})
    print("=> Tâche ajoutée avec succès !")

# Marquer une tâche comme terminée
def marquer_terminee(taches):
    afficher_taches(taches)
    choix = input("Entrez le numéro de la tâche à marquer comme terminée : ")
    if (choix.isdigit()):
        choix = int(choix)
        if (1 <= choix <= len(taches)):
            taches[choix - 1]["termine"] = True
            print(f"=> Tâche {choix} marquée comme terminée !")
        else:
            print("Numéro de tâche invalide.")
    else:
        print("Veuillez entrer un numéro valide.")

# Supprimer une tâche
def supprimer(taches):
    afficher_taches(taches)
    choix = input("Entrez le numéro de la tâche pour supprimer : ")
    if (choix.isdigit()):
        choix = int(choix)
        if (1 <= choix <= len(taches)):
            taches.pop(choix - 1)
            print(f"=> Tâche {choix} supprimée avec succès !")
        else:
            print("Numéro de tâche invalide.")
    else:
        print("Veuillez entrer un numéro valide.")

# Menu principal
def menu():
    taches = charger_taches_txt()
    while True:
        print("\n=== Gestionnaire de tâches ===")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Supprimer une tâche")
        print("5. Quitter")
        choix = input("Choix : ")
        if choix == "1":
            ajouter_tache(taches)
        elif choix == "2":
            afficher_taches(taches)
        elif choix == "3":
            marquer_terminee(taches)
        elif choix == "4":
            supprimer(taches)
        elif choix == "5":
            sauvegarder_taches_txt(taches)
            print(f"=> Tâches sauvegardées dans {fichier_taches}. Merci d'avoir utilisé le gestionnaire !")
            break
        else:
            print("Choix invalide.")

# Lancer le programme
if __name__=="__main__":
    menu()


