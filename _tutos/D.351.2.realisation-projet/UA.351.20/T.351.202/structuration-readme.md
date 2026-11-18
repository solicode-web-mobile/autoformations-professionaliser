---
layout: tuto
title: "Structurer le README du projet avec la stack technique N3"
sous_titre: "Créer l'arborescence des 7 dossiers, initialiser sprints/ et rédiger le README.md racine"
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

## 1. Prérequis
- **Base théorique et pratique requise :**
  - Organisation standard d'un dépôt Solicode N3 (arborescence des 7 dossiers).
  - Structure canonique d'un fichier `README.md` d'ingénierie logicielle intégrant la stack Laravel 12.
  - Planification Scrum de base sous Git.
- **Prérequis de projet :** Dépôt Git initialisé et publié sur la branche `sprint1` (`T.351.201`).
- **Branche Git :** `sprint1`

## 2. Travail à Faire
- **Tâche 1 : Arborescence de projet :** Créer les 7 répertoires d'organisation du projet (`.agents/`, `docs/`, `flux-travail/`, `issues/`, `labs/`, `missions/`, `sprints/`).
- **Tâche 2 : Planification Scrum de base :** Créer les fichiers de suivi `sprints/sprints.md` et `sprints/README.md`.
- **Tâche 3 : Rédaction du README.md :** Rédiger le fichier `README.md` racine selon la structure standardisée Solicode en intégrant la stack technique du projet (Laravel 12).

## 3. Étapes de Réalisation

1. **Étape 1 — Création de l'arborescence des 7 dossiers de projet :**  
   À la racine du projet `blog-des-laureats`, créez les répertoires d'organisation du projet :
   ```bash
   mkdir -p .agents docs flux-travail issues labs missions sprints
   ```

2. **Étape 2 — Initialisation de la planification Scrum dans `sprints/` :**  
   Dans le dossier `sprints/`, créez le fichier `sprints.md` pour référencer la feuille de route du projet :
   ```markdown
   # Feuille de Route des Sprints - Blog des Lauréats

   | Sprint | Branche | Objectif Principal | Statut |
   | :--- | :--- | :--- | :--- |
   | **Sprint 1** | `sprint1` | Initialisation, cadrage et consultation publique d'un article | En cours |
   | **Sprint 2** | `sprint2` | Gestion et publication des articles | À venir |
   | **Sprint 3** | `sprint3` | Authentification et administration | À venir |
   ```

   Créez également le guide `sprints/README.md` :
   ```markdown
   # Dossier des Sprints

   Ce dossier regroupe le suivi Scrum du projet :
   - `sprints.md` : Feuille de route globale des sprints.
   - `sprint[N]/` : Dossier spécifique à chaque sprint (cadrage, sprint backlog, revues et rétrospectives).
   ```

3. **Étape 3 — Rédaction du fichier `README.md` racine avec la Stack N3 :**  
   À la racine du projet, créez ou modifiez le fichier `README.md` selon le standard officiel Solicode :

````markdown
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
  - **UA-tâche** : Unité regroupant les tâches récurrentes de gestion Scrum à chaque sprint.

---

## 3. Stack technique
- **Framework Backend** : PHP 8.2+, Laravel 12 (Architecture 2 couches : Contrôleur mince -> Service).
- **Frontend & Rendu** : Blade Templates, Tailwind CSS, Alpine.js (composants interactifs légers).
- **Persistance des données** : Fichiers tabulaires CSV (Sprint 1) puis base relationnelle MySQL avec Eloquent ORM.
- **Tests automatisés** : PHPUnit / Pest (approche TDD), respect strict de PSR-12.
- **Modélisation & Architecture** : Diagrammes UML en Markdown via syntaxe Mermaid.js, fiches de décision ADR.
- **Méthodologie & Cadre Agile** : Scrum (Sprint de 80h, branche unique `sprint1`, DoD à 7 critères).
- **Gestion de versions** : Git et GitHub CLI (`gh`).
- **Intelligence Artificielle & Automatisation** : Agent Antigravity (Skills outillés natifs et prompts RIO réutilisables).

---

## 4. Organisation des dossiers
- [.agents/](./.agents/) : Configuration native de l'Agent IA (règles permanentes et skills outillés).
- [docs/](./docs/) : Documentation libre, recherches et veilles technologiques personnelles.
- [flux-travail/](./flux-travail/) : Référentiel méthodologique et suivi des étapes de réalisation du projet.
- [issues/](./issues/) : Gestion et suivi des tâches et user stories du projet.
- [labs/](./labs/) : Restitution des laboratoires théoriques et pratiques organisés par domaine et UA-Lab.
- [missions/](./missions/) : Catalogue des missions normalisées pour les apprenants en mode chatbot.
- [sprints/](./sprints/) : Planification Scrum des sprints et suivi de la branche active.

---

## 5. Méthodologie de développement
Le projet intègre les meilleures pratiques de l'ingénierie logicielle :
- **Agile / Scrum** : Découpage par sprints, réunions quotidiennes et revues de sprint.
- **Processus de développement** : Séparation claire entre les étapes de cadrage fonctionnel et d'implémentation technique.
- **Design Thinking** : Conception centrée sur les besoins réels des utilisateurs.
- **Modélisation UML** : Schémas de cas d'utilisation, diagrammes de contexte et diagrammes de séquences.

---

## 6. Démarrage rapide

### Prérequis
- Git installé et configuré.
- GitHub CLI (`gh`) authentifié.
- PHP 8.2+ et Composer installés.

### Cloner et explorer le projet
```bash
git clone https://github.com/[votre-compte-github]/blog-des-laureats.git
cd blog-des-laureats
git checkout sprint1
```
````

4. **Étape 4 — Commit et synchronisation sur `sprint1` :**  
   Indexez les nouveaux fichiers, validez le commit et poussez sur le dépôt distant :
   ```bash
   git add .
   git commit -m "docs: structurer l'arborescence des 7 dossiers, sprints et le README standard N3"
   git push origin sprint1
   ```

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - Fichier `README.md` racine propre et conforme au standard Solicode (stack Laravel 12).
  - Planification Scrum : `sprints/sprints.md` et `sprints/README.md`.
- **Critères de validation :**
  - [ ] L'arborescence des 7 dossiers (`.agents/`, `docs/`, `flux-travail/`, `issues/`, `labs/`, `missions/`, `sprints/`) est créée à la racine.
  - [ ] Le fichier `README.md` racine documente intégralement la stack technique N3.
  - [ ] Les fichiers `sprints/sprints.md` et `sprints/README.md` sont initialisés sur la branche `sprint1`.
