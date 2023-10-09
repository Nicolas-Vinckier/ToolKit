import os
import shutil
import tqdm


def lister_fichiers(dossier):
    """Liste tous les fichiers d'un dossier et de ses sous-dossiers."""
    fichiers = []
    try:
        for fichier in os.listdir(dossier):
            chemin = os.path.join(dossier, fichier)
            if os.path.isfile(chemin):
                fichiers.append(chemin)
            elif os.path.isdir(chemin):
                fichiers += lister_fichiers(chemin)
    except PermissionError as e:
        print(f"Erreur de permission : {e}")
    return fichiers


def detecter_doublons(fichiers):
    """Détection des fichiers en double."""
    doublons = {}
    for fichier in fichiers:
        if fichier in doublons:
            doublons[fichier] += 1
        else:
            doublons[fichier] = 1
    return doublons


def main():
    """Programme principal."""
    # Spécifiez le chemin du dossier racine (par exemple, C:)
    dossier_racine = "C:\\Users\\mrcan"

    print("Recherche des fichiers...")
    fichiers = lister_fichiers(dossier_racine)
    print(f"Nombre total de fichiers trouvés : {len(fichiers)}")

    # Vérifie si le dossier "OutputLog" existe
    if not os.path.exists("OutputLog"):
        print("Création du dossier 'OutputLog'...")
        # Crée le dossier "OutputLog"
        os.makedirs("OutputLog")

    # Crée un fichier texte pour les fichiers trouvés
    print("Création du fichier 'AllFile.txt'...")
    with open(
        os.path.join("OutputLog", "AllFile.txt"), "w", encoding="utf-8"
    ) as fichier_sortie:
        for fichier_path in fichiers:
            fichier_sortie.write(fichier_path + "\n")

    # Crée un fichier texte pour les fichiers en double
    print("Recherche des fichiers en double...")
    doublons = detecter_doublons(fichiers)
    with open(os.path.join("OutputLog", "Doublon.txt"), "w") as fichier_sortie:
        for fichier_path, nombre in doublons.items():
            if nombre > 1:
                fichier_sortie.write(fichier_path + "\n")

    print("Terminé !")


if __name__ == "__main__":
    # Initialise la barre de progression
    progress = tqdm.tqdm(total=len(fichiers))

    # Parcours tous les fichiers
    for fichier in fichiers:
        progress.update(1)

    # Ferme la barre de progression
    progress.close()
