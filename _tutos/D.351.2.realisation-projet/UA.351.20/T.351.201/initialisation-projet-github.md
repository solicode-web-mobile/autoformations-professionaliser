---
layout: tuto
title: "Initialiser le projet et publier sur GitHub avec GitHub CLI"
sous_titre: "Initialiser le dépôt Git local, créer la branche sprint1 et publier le projet personnel avec gh repo create"
slug: "publication-github"
slug_domaine: "realisation-projet"
slug_ua: "initialisation"
permalink: /tutos/publication-github/
tuto_id: "T.351.201"
version: "normal"
ua: "UA.351.20"
maturite: "UA-Tâche"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
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
- **Tâche 1 : Initialisation locale :** Créer le projet local, initialiser Git (`git init`) et créer la branche de travail `sprint1`.
- **Tâche 2 : Journalisation des commandes :** Créer l'arborescence et consigner les commandes dans `tutoriels/realisation-projet/initialisation/publication-github/publication-github.command.md`.
- **Tâche 3 : Publication sur GitHub :** Réaliser le premier commit avec le fichier journal et publier le dépôt sur votre compte GitHub personnel via GitHub CLI avec la commande `gh repo create`.

## 3. Étapes de Réalisation

1. **Étape 1 — Vérification de l'authentification GitHub CLI :**  
   Vérifiez que votre terminal est authentifié sur votre compte GitHub personnel :
   ```bash
   gh auth status
   ```
   *Si vous n'êtes pas authentifié, exécutez `gh auth login` et choisissez `GitHub.com` > `HTTPS` > `Login with a web browser`.*

2. **Étape 2 — Création du dossier de travail et initialisation Git :**  
   Créez le répertoire local du projet d'imitation et initialisez le suivi de version :
   ```bash
   mkdir blog-des-laureats
   cd blog-des-laureats
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
   mkdir -p tutoriels/realisation-projet/initialisation/publication-github
   ```

   Créez le fichier `tutoriels/realisation-projet/initialisation/publication-github/publication-github.command.md` pour consigner l'historique des commandes :
   ```markdown
   ```bash
   gh auth status
   mkdir blog-des-laureats
   cd blog-des-laureats
   git init
   git checkout -b sprint1
   mkdir -p tutoriels/realisation-projet/initialisation/publication-github
   git add tutoriels/realisation-projet/initialisation/publication-github/publication-github.command.md
   git commit -m "docs: consigner les commandes d'initialisation"
   gh repo create blog-des-laureats --public --source=. --remote=origin --push
   ```
   ```

5. **Étape 5 — Premier commit local :**  
   Indexez et validez le fichier `publication-github.command.md` sur la branche `sprint1` :
   ```bash
   git add tutoriels/realisation-projet/initialisation/publication-github/publication-github.command.md
   git commit -m "docs: consigner les commandes d'initialisation"
   ```

6. **Étape 6 — Publication sur votre compte GitHub personnel :**  
   Créez et publiez le dépôt distant public sous votre profil GitHub personnel avec GitHub CLI :
   ```bash
   gh repo create blog-des-laureats --public --source=. --remote=origin --push
   ```

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - Dépôt distant public accessible à l'URL `https://github.com/[votre-compte-github]/blog-des-laureats`.
  - Journal des commandes : `tutoriels/realisation-projet/initialisation/publication-github/publication-github.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le dépôt distant est créé et public sous le compte GitHub personnel de l'apprenant.
  - [ ] La branche de travail active est strictement `sprint1`.
  - [ ] Le fichier `publication-github.command.md` est présent dans `tutoriels/realisation-projet/initialisation/publication-github/` et consigne fidèlement les commandes exécutées.
