import os
import datetime

print(f"Lancement du programme {__file__}")

def list_files(path):
    """
    Renvoie une liste de tous les fichiers dans un répertoire, y compris les fichiers des sous-répertoires.

    Args:
      path: Le chemin du répertoire à lister.

    Returns:
      Une liste de chemins de fichiers.
    """

    files = []
    for root, dirs, _ in os.walk(path):
        for file in dirs:
            files.append(os.path.join(root, file))
        for file in os.listdir(root):
            files.append(os.path.join(root, file))
    return files


def get_file_info(file):
    """
    Renvoie des informations sur un fichier, notamment son extension, son répertoire parent et son nom.

    Args:
      file: Le chemin du fichier.

    Returns:
      Un dictionnaire contenant les informations suivantes :
        * extension: L'extension du fichier, sans le point.
        * parent: Le répertoire parent du fichier.
        * name: Le nom du fichier.
    """

    extension = os.path.splitext(file)[1]
    parent = os.path.dirname(file)
    name = os.path.basename(file)
    return {
        "extension": extension,
        "parent": parent,
        "name": name,
    }


def main():
    """
    Exécute le programme.
    """

    # Obtenir la date et l'heure actuelles.
    now = datetime.datetime.now()

    # Créer le nom du fichier de sortie.
    filename = "SearchFile" + "-" + now.strftime("%Y-%m-%d-%H-%M-%S") + ".txt"

    # Créer le répertoire de sortie si il n'existe pas.
    if not os.path.exists("OutputLog"):
        os.mkdir("OutputLog")

    # Lister tous les fichiers dans le répertoire courant.
    files = list_files(".")

    # Enregistrer les informations sur les fichiers dans un fichier.
    with open(os.path.join("OutputLog", filename), "w") as f:
        for file in files:
            info = get_file_info(file)
            f.write(f"{info['extension']}\t{info['parent']}\t{info['name']}\n")


if __name__ == "__main__":
    main()
