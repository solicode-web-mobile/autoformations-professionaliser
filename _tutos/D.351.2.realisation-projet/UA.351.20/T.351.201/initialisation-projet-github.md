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
- **Tâche 1 : Initialisation locale :** Créer le projet local, initialiser Git (`git init`), configurer le fichier `.gitignore` standard et créer la branche de travail `sprint1`.
- **Tâche 2 : Publication sur GitHub :** Réaliser le premier commit et publier le dépôt sur votre compte GitHub personnel via GitHub CLI avec la commande `gh repo create`.
- **Tâche 3 : Journalisation :** Consigner l'ensemble des commandes exécutées dans le fichier `commandes.md` et synchroniser sur la branche `sprint1`.

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

3. **Étape 3 — Configuration du fichier `.gitignore` standard :**  
   À la racine du dossier `blog-des-laureats`, créez le fichier `.gitignore` :
   ```gitignore
   # Environnement & Secrets
   .env
   .env.backup
   .env.production

   # Dépendances
   /vendor/
   /node_modules/

   # Système & IDE
   .DS_Store
   Thumbs.db
   .vscode/
   .idea/

   # Fichiers de build & logs
   npm-debug.log*
   yarn-error.log*
   /storage/*.key
   ```

4. **Étape 4 — Création de la branche commune unique de sprint :**  
   Conformément au standard Solicode N3, l'ensemble des travaux et livrables d'un sprint est versionné sur une branche partagée unique :
   ```bash
   git checkout -b sprint1
   ```

5. **Étape 5 — Premier commit local :**  
   Indexez et validez le fichier `.gitignore` sur la branche `sprint1` :
   ```bash
   git add .gitignore
   git commit -m "chore: initialiser le dépôt et configurer .gitignore"
   ```

6. **Étape 6 — Publication sur votre compte GitHub personnel :**  
   Créez et publiez le dépôt distant public sous votre profil GitHub personnel avec GitHub CLI :
   ```bash
   gh repo create blog-des-laureats --public --source=. --remote=origin --push
   ```

7. **Étape 7 — Journalisation des commandes exécutées :**  
   À la racine du projet, créez le fichier `commandes.md` pour consigner l'historique des commandes :
   ```markdown
   # Journal des Commandes d'Initialisation - Sprint 1

   - Date d'exécution : [Date du jour]
   - Apprenant : [Votre Nom et Prénom]
   - URL du dépôt GitHub : https://github.com/[votre-compte-github]/blog-des-laureats

   ## Commandes exécutées :
   ```bash
   gh auth status
   mkdir blog-des-laureats
   cd blog-des-laureats
   git init
   git checkout -b sprint1
   git add .gitignore
   git commit -m "chore: initialiser le dépôt et configurer .gitignore"
   gh repo create blog-des-laureats --public --source=. --remote=origin --push
   ```
   ```

8. **Étape 8 — Sauvegarde du journal sur la branche de sprint :**  
   ```bash
   git add commandes.md
   git commit -m "docs: consigner les commandes d'initialisation"
   git push origin sprint1
   ```

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - Dépôt distant public accessible à l'URL `https://github.com/[votre-compte-github]/blog-des-laureats`.
  - Fichier `commandes.md` à la racine de la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le dépôt distant est créé sous le compte GitHub personnel de l'apprenant.
  - [ ] La branche de travail active est strictement `sprint1`.
  - [ ] Le fichier `commandes.md` retrace fidèlement les commandes exécutées.
