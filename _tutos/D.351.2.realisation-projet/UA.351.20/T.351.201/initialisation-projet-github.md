---
layout: tuto
title: "Initialiser le projet et publier sur GitHub avec GitHub CLI"
sous_titre: "Initialiser le dépôt Git local avec .gitignore vide, créer la branche sprint1 et publier le projet personnel avec gh repo create"
slug: "publication-github"
slug_domaine: "realisation-projet"
slug_ua: "initialisation"
permalink: /tutos/publication-github/
tuto_id: "T.351.201"
version: "normal"
ua: "UA.351.20"
maturite: "projet"
type: "tuto-tache"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Prérequis
- **Base théorique et pratique requise :**
  - Installation et utilisation de GitHub CLI (`gh repo create`).
  - Création et gestion des branches Git (`sprint[N]`).
- **Prérequis de projet :** Présentation et cadrage du projet d'imitation par le formateur référent.
- **Branche Git :** `sprint1`

## 2. Travail à Faire
- **Tâche 1 : Initialisation locale :** Créer le projet local, créer un fichier `.gitignore` vide (`echo "" > .gitignore`), initialiser Git (`git init`) et créer la branche de travail `sprint1`.
- **Tâche 2 : Journalisation des commandes :** Créer l'arborescence et consigner les commandes dans `tutoriels/realisation-projet/initialisation/publication-github/publication-github.command.md`.
- **Tâche 3 : Publication sur GitHub :** Réaliser le premier commit avec `.gitignore` et le fichier journal, puis publier le dépôt sur votre compte GitHub personnel via GitHub CLI avec la commande interactive `gh repo create`.

## 3. Étapes de Réalisation

1. **Étape 1 — Vérification de l'authentification GitHub CLI :**  
   Vérifiez que votre terminal est authentifié sur votre compte GitHub personnel :

```bash
gh auth status
```

   *Si vous n'êtes pas authentifié, exécutez `gh auth login` et choisissez `GitHub.com` > `HTTPS` > `Login with a web browser`.*

2. **Étape 2 — Création du dossier de travail et initialisation Git :**  
   Créez le répertoire local du projet d'imitation, créez un fichier `.gitignore` vide et initialisez le suivi de version :

```bash
mkdir blog-des-laureats
cd blog-des-laureats
echo "" > .gitignore
git init
```

3. **Étape 3 — Création de la branche commune unique de sprint :**  
   Conformément au standard Solicode N3, l'ensemble des travaux et livrables d'un sprint est versionné sur une branche partagée unique :

```bash
git checkout -b sprint1
```

4. **Étape 4 — Création de l'arborescence et du journal de commandes :**  
   Créez le répertoire dédié au tutoriel :

```bash
mkdir tutoriels/realisation-projet/initialisation/publication-github
```

   Créez le fichier `tutoriels/realisation-projet/initialisation/publication-github/publication-github.command.md` pour consigner l'historique des commandes :

```bash
gh auth status
mkdir blog-des-laureats
cd blog-des-laureats
echo "" > .gitignore
git init
git checkout -b sprint1
gh repo create
```

5. **Étape 5 — Premier commit local :**  
   Indexez et validez le fichier `.gitignore` et `publication-github.command.md` sur la branche `sprint1` :

```bash
git add .gitignore tutoriels/realisation-projet/initialisation/publication-github/publication-github.command.md
git commit -m "feat: initialisation du projet et journal des commandes"
```

6. **Étape 6 — Publication interactive sur GitHub :**  
   Lancez la création du dépôt distant sans paramètres :

```bash
gh repo create
```

   Répondez aux questions posées interactivement par GitHub CLI :
   - **What would you like to do?** : `Push an existing local repository to GitHub`
   - **Path to local repository** : `.` *(ou appuyez sur Entrée)*
   - **Repository name** : `blog-des-laureats`
   - **Description** : *(appuyez sur Entrée)*
   - **Visibility** : `Public`
   - **Would you like to add a remote?** : `Yes` *(nom : origin)*
   - **Would you like to push commits from the current branch to "origin"?** : `Yes`

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - Dépôt distant public accessible à l'URL `https://github.com/[votre-compte-github]/blog-des-laureats`.
  - Fichier `.gitignore` vide à la racine du dépôt.
  - Journal des commandes : `tutoriels/realisation-projet/initialisation/publication-github/publication-github.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le dépôt distant est créé et public sous le compte GitHub personnel de l'apprenant.
  - [ ] La branche de travail active est strictement `sprint1`.
  - [ ] Le fichier `.gitignore` est présent à la racine et vide.
  - [ ] Le fichier `publication-github.command.md` est présent dans `tutoriels/realisation-projet/initialisation/publication-github/` et consigne fidèlement les commandes exécutées.
