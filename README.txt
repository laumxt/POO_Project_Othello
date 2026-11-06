# Projet Othello

## Équipe

Nous sommes trois personnes à collaborer sur ce projet :

- Laura
- Sabrina
- Alexia

## Organisation du travail avec Git

Avant de commencer le développement, nous devons nous mettre d'accord sur la stratégie de gestion des branches Git.

Deux possibilités sont envisagées :

### Option 1 : Deux branches communes (`master` et `dev`)

- Une branche `master` contenant les versions stables du projet.
- Une branche `dev` sur laquelle les trois membres de l'équipe travaillent et intègrent leurs modifications.

### Option 2 : Une branche par personne

- Chaque membre travaille sur sa propre branche.
- Les fonctionnalités développées et testées sont ensuite intégrées dans `master`.
- Avant chaque `push`, il faut effectuer un `pull` pour récupérer les dernières modifications et éviter les conflits.

**Décision à prendre collectivement avant de commencer le développement.**

## Environnemenrt virtuel ##
//création
 python3.12 -m venv .venv
 //activation (avant de travailler, à chaque fois)
source .venv/bin/activate
//les paquets à installer sont à noter dans requirements.txt
// création ou mise a jour des requirements
python -m pip freeze >> requirements.txt
// installation des dépendances
python -m pip install -r requirements.txt