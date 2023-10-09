import os
import shutil
import tqdm


def lister_fichiers(dossier):
    """Liste tous les fichiers d'un dossier et de ses sous-dossiers."""
    fichiers = []
    for fichier in os.listdir(dossier):
        chemin = os.path.join(dossier, fichier)
        if os.path.isfile(chemin):
            fichiers.append(chemin)
        elif os.path.isdir(chemin):
            fichiers += lister_fichiers(chemin)
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
    # Liste tous les fichiers de l'ordinateur
    fichiers = lister_fichiers(os.getcwd())

    # Vérifie si le dossier "OutputLog" existe
    if not os.path.exists("OutputLog"):
        # Crée le dossier "OutputLog"
        os.makedirs("OutputLog")

    # Créé un fichier texte pour les fichiers trouvés
    with open(os.path.join("OutputLog", "AllFile.txt"), "w") as fichier:
        for fichier in lister_fichiers(os.getcwd()):
            fichier.write(fichier + "\n")

    # Créé un fichier texte pour les fichiers en double
    doublons = detecter_doublons(fichiers)
    with open(os.path.join("OutputLog", "Doublon.txt"), "w") as fichier:
        for fichier, nombre in doublons.items():
            if nombre > 1:
                fichier.write(fichier + "\n")


if __name__ == "__main__":
    # Initialise la barre de progression
    progress = tqdm.tqdm(total=len(fichiers))

    # Parcours tous les fichiers
    for fichier in fichiers:
        progress.update(1)

    # Ferme la barre de progression
    progress.close()
