---
layout: tuto
title: "Structurer le README du projet avec la stack technique N3"
sous_titre: "Créer l'arborescence des 7 dossiers et rédiger le README.md racine"
slug: "structuration-readme"
slug_domaine: "realisation-projet"
slug_ua: "initialisation"
permalink: /tutos/structuration-readme/
tuto_id: "T.351.202"
version: "normal"
ua: "UA.351.20"
maturite: "UA-Tâche"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement & Emplacement du Livrable
- **Domaine :** `D.351.2` (`realisation-projet`)
- **Unité d'Apprentissage :** `UA.351.20` (`initialisation`)
- **Tutoriel :** `T.351.202` (`structuration-readme`)
- **Type d'UA :** `UA-Tâche` *(Les livrables sont des fichiers de projet opérationnels — ils ne sont PAS placés dans le dossier `labs/`)*.
- **Position dans le flux :** Phase A — Initialisation du Projet, Outillage IA & Méthodologie / Étape 01 — Initialisation et publication du projet.
- **Branche Git :** `sprint1`
- **Emplacement exact des livrables :** `README.md` *(Racine du projet)* et l'arborescence des 7 dossiers.

## 2. Déroulement Pas-à-Pas de la Tâche

1. **Étape 1 — Création de l'arborescence des 7 dossiers de projet :**  
   À la racine du projet `blog-des-laureats`, créez les répertoires d'organisation du projet :
   ```bash
   mkdir -p .agents docs flux-travail issues labs missions sprints
   ```

2. **Étape 2 — Rédaction du fichier `README.md` racine avec la Stack N3 fixée :**  
   Créez à la racine le fichier `README.md` en intégrant rigoureusement les informations validées pour le Niveau 3 :

   ```markdown
   # Blog des Lauréats - Projet d'Imitation Niveau 3

   ## 1. Description du projet
   Le Blog des Lauréats est une application web conçue pour la communauté de Solicode Tanger.
   Les lauréats peuvent rédiger, publier et administrer leurs articles professionnels.
   Les apprenants actuels de Solicode peuvent consulter et lire ces retours d'expérience. L'application est déployée et accessible en ligne sur Internet.

   ---

   ## 2. Contexte et Objectifs

   ### Contexte général
   - **Établissement** : Solicode Tanger.
   - **Promotion** : Niveau 3 - Développement Web et Mobile.
   - **Formateur référent** : ESSARRAJ Fouad.

   ### Démarche pédagogique : Méthode par imitation
   Ce projet s'appuie sur la méthode par imitation pour guider l'apprenant pas à pas de A à Z :
   - **Tutoriels** : Guides complets détaillant les étapes et les résultats attendus.
   - **UA-Lab** : Laboratoires d'apprentissage guidés pour maîtriser les bases théoriques et pratiques.
   - **Lab** : Recherche autonome d'une solution technique validée par le formateur.
   - **Veille technologique** : Découverte et intégration de nouveaux outils ou composants.
   - **Tâches** : Actions pratiques d'ingénierie et d'organisation Scrum.

   ### Composants pédagogiques (Approche Par Compétences - APC)
   - **Domaine de compétence** : Regroupement thématique des compétences du référentiel.
   - **Unité d'apprentissage (UA)** :
     - **UA-Tuto** : Unité basée sur des tutoriels pas-à-pas.
     - **UA-Lab** : Unité pratique guidée par le formateur.
     - **UA-Tâche** : Unité regroupant les tâches récurrentes de gestion Scrum à chaque sprint.

   ---

   ## 3. Stack technique
   - **Backend & Framework** : PHP 8.2+, Framework **Laravel 12** (Architecture 2 couches : Contrôleur mince -> Classe Service).
   - **Frontend & Rendu** : Gabarits **Blade**, utilitaires CSS **Tailwind CSS**, réactivité légère avec **Alpine.js**.
   - **Persistance des données** :
     - *Sprint 1* : Données tabulaires CSV (`app/Services/ArticleService.php`).
     - *Sprints ultérieurs* : Base de données relationnelle MySQL et ORM Eloquent.
   - **Tests automatisés & Qualité** : **PHPUnit / Pest** (TDD) et respect strict des standards **PSR-12**.
   - **Modélisation & Conception** : **UML avec Mermaid.js** (diagramme de contexte système, cas d'utilisation macro).
   - **Méthodologie & Cadre Agile** : **Scrum** (Sprints calibrés de 80h, branche Git unique par sprint `sprint1`, Definition of Done en 7 critères bloquants).
   - **Gestion de versions & Outillage CLI** : **Git** et **GitHub CLI (`gh`)**.
   - **Intelligence Artificielle & Automatisation** : **Agent IA Antigravity** (méthode de prompting structuré RIO, règles permanentes Always-On et skills modulaires).
   - **Documentation & Restitution** : Markdown standard et diaporamas **Marp**.

   ---

   ## 4. Organisation des dossiers
   - [.agents/](./.agents/) : Configuration native de l'Agent IA (règles permanentes et skills outillés).
   - [docs/](./docs/) : Documentation libre, recherches et veilles technologiques personnelles.
   - [flux-travail/](./flux-travail/) : Référentiel méthodologique et suivi des étapes de réalisation du projet.
   - [issues/](./issues/) : Gestion et suivi des tâches et user stories du projet.
   - [labs/](./labs/) : Restitution des laboratoires théoriques et pratiques organisés par domaine et UA-Lab (`labs/slug-domaine/slug-ua/slug-tuto/`).
   - [missions/](./missions/) : Catalogue des missions normalisées pour les apprenants en mode chatbot.
   - [sprints/](./sprints/) : Planification Scrum des sprints et suivi de la branche active.

   ---

   ## 5. Méthodologie de développement
   Le projet intègre les meilleures pratiques de l'ingénierie logicielle :
   - **Agile / Scrum** : Découpage par sprints, réunions quotidiennes et revues de sprint.
   - **Processus de développement** : Séparation claire entre la branche fonctionnelle et la branche technique.
   - **Design Thinking** : Conception centrée sur les besoins réels des utilisateurs.
   - **Modélisation UML** : Schémas de cas d'utilisation, diagrammes de classes et de séquences.

   ---

   ## 6. Démarrage rapide

   ### Prérequis
   - Git installé sur votre machine.
   - GitHub CLI (`gh`) configuré et authentifié.

   ### Cloner le projet
   ```bash
   git clone https://github.com/[votre-compte-github]/blog-des-laureats.git
   cd blog-des-laureats
   git checkout sprint1
   ```
   ```

3. **Étape 3 — Validation et commit sur la branche de sprint :**  
   Indexez et validez le fichier `README.md` sur la branche `sprint1` :
   ```bash
   git add README.md
   git commit -m "docs: formaliser le README.md avec la stack N3 et l'arborescence des dossiers"
   git push origin sprint1
   ```

## 3. Livrables & Critères de Réussite
- **Livrables attendus :**
  - Fichier `README.md` à la racine de la branche `sprint1`.
  - Arborescence des 7 dossiers (`.agents/`, `docs/`, `flux-travail/`, `issues/`, `labs/`, `missions/`, `sprints/`).
- **Critères de validation :**
  - [ ] Le `README.md` détaille rigoureusement la stack N3 (Laravel 12, Blade, Tailwind, Alpine, CSV).
  - [ ] Les 7 répertoires racines sont créés et versionnés.
  - [ ] Le commit est publié sur la branche `sprint1` du compte personnel.
