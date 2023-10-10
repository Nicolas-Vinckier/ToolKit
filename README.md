# ToolKit

## Installation

Pour installer le toolkit, clonez ce dépôt sur votre ordinateur et exécutez les commandes suivantes :

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
py .\Application.py
```

## Description

Ce dépôt contient un toolkit de programmes Python pour diverses tâches, notamment :

* Lister tous les fichiers d'un dossier et de ses sous-dossiers (program/AllFile.py)
* Rechercher tous les fichiers dans un répertoire, y compris les fichiers des sous-répertoires (program/Search.py)
* Générer un mot de passe fort et aléatoire (program/Password.py)
* Supprimer tous les fichiers du dossier OutputLog (program/Clear_Toolkit.py)

## Utilisation

Pour utiliser le toolkit, clonez ce dépôt sur votre ordinateur et exécutez le programme Application.py. Cela affichera un menu avec une liste de tous les programmes disponibles. Sélectionnez le programme que vous souhaitez exécuter et suivez les instructions à l'écran.

## Exemples

### Lister tous les fichiers d'un dossier et de ses sous-dossiers

Pour lister tous les fichiers d'un dossier et de ses sous-dossiers, exécutez le programme AllFile.py. Cela créera un fichier texte nommé AllFile.txt dans le dossier OutputLog, qui contiendra une liste de tous les fichiers trouvés.

### Rechercher tous les fichiers dans un répertoire, y compris les fichiers des sous-répertoires

Pour rechercher tous les fichiers dans un répertoire, y compris les fichiers des sous-répertoires, exécutez le programme Search.py. Cela créera un fichier texte nommé SearchFile.txt dans le dossier OutputLog, qui contiendra une liste de tous les fichiers trouvés, ainsi que des informations sur chaque fichier, telles que son extension, son répertoire parent et son nom.

### Générer un mot de passe fort et aléatoire

Pour générer un mot de passe fort et aléatoire, exécutez le programme Password.py. Cela vous demandera de spécifier la longueur du mot de passe et si vous souhaitez utiliser des majuscules, des minuscules, des chiffres et des caractères spéciaux. Une fois que vous avez entré vos préférences, le programme générera un mot de passe fort et aléatoire, qu'il affichera à l'écran et écrira dans un fichier texte dans le dossier OutputLog.

### Supprimer tous les fichiers du dossier OutputLog

Pour supprimer tous les fichiers du dossier OutputLog, exécutez le programme Clear_Toolkit.py. Cela supprimera tous les fichiers du dossier, y compris les fichiers créés par les autres programmes du toolkit.

## Remarques

* Les programmes de ce toolkit nécessitent Python 3.6 ou supérieur.
* Le dossier OutputLog est créé automatiquement si nécessaire.
* Les mots de passe générés par le programme Password.py sont très forts et difficiles à deviner. Cependant, il est important de ne pas partager votre mot de passe avec qui que ce soit et de le changer régulièrement.
