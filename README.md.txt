# Projet de Prédiction des Notes des Étudiants


## Description
Ce projet utilise un modèle de machine learning pour prédire les notes des étudiants en fonction de plusieurs facteurs comme les heures d'étude, la présence en classe, l'implication parentale, etc. L'application a été construite en utilisant Streamlit pour l'interface utilisateur et scikit-learn pour la modélisation.


## Structure du projet
Le projet est structuré comme suit :

project/
├── app.py            # Fichier principal pour l'interface utilisateur
├── backend.py        # Fichier contenant les fonctions de traitement (back-end)
├── last_gbr.pkl      # Modèle sauvegardé
└── requirements.txt  # Liste des dépendances (si nécessaire)


## Prérequis
Avant de commencer, assurez-vous que votre environnement de développement est configuré avec :
- Python 3.x
- Pip (gestionnaire de paquets Python)


### 1. Téléchargez ou extrayez le fichier du projet
Téléchargez ou extrayez le fichier contenant le projet dans un dossier sur votre ordinateur.


### 2. Créer un environnement virtuel (optionnel mais recommandé)
Il est recommandé de travailler dans un environnement virtuel pour gérer les dépendances. Pour ce faire, ouvrez votre terminal (ou invite de commandes) et exécutez les commandes suivantes :

#### Sous Windows :
```bash
python -m venv venv

.\venv\Scripts\activate

### 3. Installer les dépendances

Une fois l'environnement virtuel activé, installez les dépendances nécessaires en exécutant la commande suivante dans le terminal :

pip install -r requirements.txt


### 4. Lancer l'application
Pour lancer l'application Streamlit, exécutez la commande suivante dans le terminal :

streamlit run app.py

Cela ouvrira l'interface Streamlit dans votre navigateur par défaut, où vous pourrez entrer les données des étudiants et obtenir des prédictions sur leurs notes.


Interface Utilisateur

L'interface utilisateur permet à l'utilisateur de saisir les informations suivantes pour chaque étudiant :

Heures d'étude
Taux de présence
Niveau d'implication des parents
Accès aux ressources
Activités parascolaires
Nombre d'heures de sommeil
Notes précédentes
Niveau de motivation
Accès à Internet
Séances de tutorat
Revenu familial
Influence des pairs
Activité physique
Niveau d'éducation des parents
Distance du domicile
Sexe

Après avoir rempli ces informations, l'utilisateur pourra cliquer sur un bouton pour obtenir la prédiction des notes de l'étudiant en fonction de ces facteurs.


Notes

Le modèle utilise un Gradient Boosting Regressor pour prédire les notes des étudiants en fonction des caractéristiques saisies.
Le modèle est sauvegardé dans le fichier last_gbr.pkl et est chargé automatiquement au démarrage de l'application.
Si vous rencontrez des erreurs, assurez-vous que toutes les dépendances sont correctement installées et que vous utilisez la version de Python recommandée.
Auteurs





### Explication de la structure du fichier `README.md` :
- **Introduction** : Un résumé du projet, des objectifs et des outils utilisés.
- **Structure du projet** : Une vue d'ensemble des fichiers présents dans le projet.
- **Prérequis** : Les prérequis nécessaires à l'exécution du projet.
- **Installation et Exécution** : Des instructions détaillées pour installer les dépendances et lancer l'application.
- **Interface Utilisateur** : Explication des champs que l'utilisateur devra remplir dans l'interface.
- **Notes** : Informations supplémentaires concernant le modèle utilisé, le fichier de sauvegarde et des conseils pour résoudre d'éventuels problèmes.


Merci de tester ce projet ! Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter(yassine.zouguari.58@edu.uiz.ac.ma).




