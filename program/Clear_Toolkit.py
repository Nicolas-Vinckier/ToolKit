import os

# Le path est le répertoire courant + OutputLog
path = os.path.join(os.getcwd(), "OutputLog")


def delete_output_log():
    # Affiche les éléments du répertoire courant
    # print(os.listdir("."))

    # Vérifier si le dossier  existe
    if os.path.exists(path):
        # Supprimer les fichiers
        for filename in os.listdir(path):
            filepath = os.path.join(path, filename)
            os.remove(filepath)

        # Supprimer le dossier
        os.rmdir(path)
    else:
        print(f"Le dossier {path} n'existe pas.")


def main():
    delete_output_log()


if __name__ == "__main__":
    delete_output_log()
