---
layout: tuto
title: "Initialiser les présentations racine au format Marp"
sous_titre: "Structurer le dossier presentations/ avec son guide et créer les diaporamas Marp du projet et du sprint 1"
slug: "presentation-marp"
slug_domaine: "realisation-projet"
slug_ua: "initialisation"
permalink: /tutos/presentation-marp/
tuto_id: "T.351.204"
version: "normal"
ua: "UA.351.20"
maturite: "projet"
type: "tuto-tache"
nav_order: 4
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
  - Principes de base de l'outil Marp pour diaporamas en Markdown (`marp: true`, séparateur `---`).
  - Configuration des en-têtes et pieds de page Marp.
  - Structuration d'une soutenance de projet et d'une revue de sprint.
- **Prérequis de projet :** Dépôt Git initialisé, README racine et arborescence créés sur `sprint1` (`T.351.202`).
- **Branche Git :** `sprint1`

## 2. Travail à Faire
- **Tâche 1 : Structuration du dossier :** Créer le répertoire `presentations/` à la racine du projet.
- **Tâche 2 : Rédaction du guide du dossier :** Rédiger `presentations/README.md` avec les instructions d'utilisation et d'export Marp.
- **Tâche 3 : Diaporama général du projet :** Initialiser `presentations/presentation-blog.md` avec son en-tête et sa page de garde Marp.
- **Tâche 4 : Diaporama de restitution du Sprint 1 :** Initialiser `presentations/presentation-sprint1.md` avec son en-tête et sa page de garde Marp.
- **Tâche 5 : Journalisation des commandes :** Consigner les commandes exécutées dans `tutoriels/realisation-projet/initialisation/presentation-marp/presentation-marp.command.md`.

## 3. Étapes de Réalisation

1. **Étape 1 — Création du répertoire des présentations :**  
   À la racine du projet `blog-des-laureats`, créez le dossier `presentations/` :

```bash
mkdir presentations
```

2. **Étape 2 — Rédaction du guide `presentations/README.md` :**  
   Dans `presentations/`, créez le fichier `README.md` :

```markdown
# Dossier des Présentations (`presentations/`)

Ce dossier regroupe les diaporamas du projet conçus au format Marp Markdown.

## 1. Rôle du dossier
- Centraliser les présentations orales pour la soutenance globale du projet et les restitutions de chaque sprint.
- Faciliter la modification rapide des diapositives via le format texte Markdown.
- Permettre l'export direct en PDF ou HTML avec Marp.

## 2. Contenu du dossier
- `presentation-blog.md` : Diaporama de présentation générale du projet Blog des lauréats.
- `presentation-sprint1.md` : Diaporama de restitution du Sprint 1 (dépôt, modélisation, architecture 2 couches).

## 3. Guide d'utilisation
- Ouvrir un fichier de présentation dans votre éditeur de code.
- Utiliser l'extension VS Code Marp pour prévisualiser les diapositives.
- Respecter la page de garde normalisée (Apprenant, Encadrant, Établissement Solicode).
```

3. **Étape 3 — Initialisation du diaporama général `presentations/presentation-blog.md` :**  
   Créez le fichier `presentations/presentation-blog.md` avec son en-tête Marp et sa page de garde :

````markdown
---
marp: true
theme: default
paginate: true
header: "Solicode N3 - Projet Imitation : Blog des lauréats"
footer: "Encadrant : ESSARRAJ Fouad | Solicode Tanger"
---

<!-- _class: lead -->
# Blog des Lauréats
### Présentation Générale du Projet

- **Apprenant** : Apprenant Solicode
- **Encadrant** : ESSARRAJ Fouad
- **Établissement** : Solicode Tanger
- **Domaine** : Développement Web
- **Compétence** : Développer une application web complète
- **Date** : 2026-11-18
````

4. **Étape 4 — Initialisation du diaporama de sprint `presentations/presentation-sprint1.md` :**  
   Créez le fichier `presentations/presentation-sprint1.md` avec son en-tête Marp et sa page de garde :

````markdown
---
marp: true
theme: default
paginate: true
header: "Solicode N3 - Sprint 1 : Cadrage et Initialisation"
footer: "Encadrant : ESSARRAJ Fouad | Solicode Tanger"
---

<!-- _class: lead -->
# Restitution du Sprint 1
### Cadrage, Environnement IA et Consultation d'un Article

- **Apprenant** : Apprenant Solicode
- **Encadrant** : ESSARRAJ Fouad
- **Établissement** : Solicode Tanger
- **Domaine** : Développement Web
- **Compétence** : Initialisation, Cadrage Scrum et Architecture 2 couches
- **Date** : 2026-11-18
````

5. **Étape 5 — Journalisation des commandes exécutées :**  
   Dans le fichier `tutoriels/realisation-projet/initialisation/presentation-marp/presentation-marp.command.md`, consignez les commandes exécutées :

```bash
mkdir presentations
```

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - Dossier `presentations/` avec `README.md`.
  - Diaporama général `presentations/presentation-blog.md` au format Marp.
  - Diaporama de restitution `presentations/presentation-sprint1.md` au format Marp.
  - Journal des commandes : `tutoriels/realisation-projet/initialisation/presentation-marp/presentation-marp.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Les diaporamas comportent l'en-tête Marp (`marp: true`, `theme: default`, `paginate: true`).
  - [ ] La page de garde identifie l'apprenant, l'encadrant et l'établissement Solicode.
  - [ ] Le journal `presentation-marp.command.md` consigne fidèlement les commandes exécutées.
