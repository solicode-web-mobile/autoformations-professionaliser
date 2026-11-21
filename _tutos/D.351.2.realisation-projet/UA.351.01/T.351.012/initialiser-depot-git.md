---
layout: tuto
title: "Initialiser le dépôt Git et l'espace projet vitrine"
sous_titre: "Configurer l'espace de travail local, le suivi de version Git et la documentation vitrine du projet"
slug: "initialiser-depot-git"
slug_domaine: "realisation-projet"
slug_ua: "depot-cadrage-stack-backlog"
permalink: /tutos/initialiser-depot-git/
tuto_id: "T.351.012"
version: "normal"
ua: "UA.351.01"
type: "tuto-tache"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
livrables:
  - chemin: "README.md"
    version: "0.1.0"
---

## 1. Travail à faire
Initialisez l'espace de travail officiel du *Blog des Lauréats* :
1. **Étape 1 — Initialiser le dépôt local :** Configurez le suivi de version Git dans le répertoire racine du projet.
2. **Étape 2 — Mettre en place le `.gitignore` :** Créez un fichier `.gitignore` standard adapté à l'environnement Windows PowerShell, Composer et Node.js.
3. **Étape 3 — Créer l'organisation standard du dépôt :** Déployez les répertoires d'ingénierie logicielle et de documentation.
4. **Étape 4 — Rédiger la documentation vitrine :** Rédigez le fichier `README.md` racine présentant le projet, les objectifs du Sprint 0, la stack technique et l'équipe.
5. **Étape 5 — Publier le dépôt distant :** Créez le dépôt distant sur GitHub à l'aide de GitHub CLI et activez la branche de travail `sprint0`.

## 2. Consignes de Réalisation
- Créez l'arborescence standard des dossiers d'ingénierie :
  ```powershell
  mkdir docs, docs/cadrage, docs/analyse, docs/produit, docs/conception, docs/architecture, scrum, tutoriels, src
  ```
- Créez le fichier `.gitignore` et le fichier `README.md` :
  ```powershell
  echo "" > .gitignore
  echo "" > README.md
  ```
- Renseignez les sections normatives de `README.md` :
  - Nom du projet (*Blog des Lauréats de l'EFP*) et description en deux phrases.
  - Stack technique ciblée (Laravel, MySQL, Tailwind CSS, Preline UI, Alpine.js).
  - Équipe projet et répartition des rôles Scrum.
  - Lien vers la feuille d'engagement active (`sprints/sprint-0.md`).
- Publiez le dépôt distant sur GitHub avec GitHub CLI :
  ```powershell
  gh repo create blog-laureats-efp --public --source=. --remote=origin
  git checkout -b sprint0
  ```

## 3. Livrable attendu
- **Fichier de projet :** `README.md`.
- **Critère de conformité :** Le dépôt Git est initialisé avec l'arborescence officielle et le `README.md` est documenté et accessible sur GitHub.
