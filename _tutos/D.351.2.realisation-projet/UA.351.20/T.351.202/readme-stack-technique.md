---
layout: tuto
title: "Rédiger le README et spécifier la stack technique du projet"
sous_titre: "Créer l'arborescence des dossiers racine, initialiser sprints/ et rédiger le README.md racine"
slug: "readme-stack-technique"
slug_domaine: "realisation-projet"
slug_ua: "initialisation"
permalink: /tutos/readme-stack-technique/
tuto_id: "T.351.202"
version: "normal"
ua: "UA.351.20"
maturite: "UA-Tâche"
nav_order: 2
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
  - Organisation standard d'un dépôt (arborescence des dossiers racine).
  - Structure canonique d'un fichier `README.md` d'ingénierie logicielle intégrant la stack Laravel.
  - Planification Scrum de base sous Git.
- **Prérequis de projet :** Dépôt Git initialisé et publié sur la branche `sprint1` (`T.351.201`).
- **Branche Git :** `sprint1`

## 2. Travail à Faire
- **Tâche 1 : Arborescence de projet :** Créer les répertoires d'organisation du projet (`.agents/`, `docs/`, `issues/`, `tutoriels/`, `presentations/`, `rapport/`, `sprints/`).
- **Tâche 2 : Planification Scrum de base :** Créer les fichiers de suivi `sprints/sprints.md` et `sprints/README.md`.
- **Tâche 3 : Rédaction du README.md :** Rédiger le fichier `README.md` racine selon la structure standardisée Solicode en intégrant la stack technique du projet (Laravel).
- **Tâche 4 : Journalisation des commandes :** Consigner les commandes exécutées dans `tutoriels/realisation-projet/initialisation/readme-stack-technique/readme-stack-technique.command.md`.

## 3. Étapes de Réalisation

1. **Étape 1 — Création de l'arborescence des dossiers racine :**  
   À la racine du projet `blog-des-laureats`, créez les répertoires d'organisation du projet :

```bash
mkdir .agents, docs, issues, tutoriels, presentations, rapport, sprints
```

2. **Étape 2 — Initialisation de la planification Scrum dans `sprints/` :**  
   Dans le dossier `sprints/`, créez le fichier `sprints.md` pour référencer la feuille de route du projet :

```markdown
# Planification des Sprints

Ce document enregistre les sprints du projet. Les sprints suivants seront ajoutés ultérieurement, après chaque session de planification. Pour le moment, seul le Sprint 1 est actif avec la description détaillée du sprint actuel ci-dessous.

---

## Sprint 1 : Initialisation, Cadrage & Première Fonctionnalité Laravel
- **Statut** : Actif
- **Branche Git** : `sprint1`
- **Objectif pédagogique** : Au terme de la session, l'apprenant est capable d'initialiser un dépôt distant avec GitHub CLI, d'outiller l'environnement avec un Agent IA et un catalogue de missions, de formaliser le processus de développement et le flux de travail, de cadrer le projet sous gouvernance Scrum, de modéliser le diagramme de contexte et les cas d'utilisation avec Mermaid, de gérer les tâches via le dossier `issues/`, et de développer sous Laravel une page de consultation détaillée d'un article selon une architecture 2 couches (Contrôleur mince -> Classe Service) avec gabarit Blade responsive et gestion de l'erreur 404.
- **Déroulement (Vue d'ensemble du travail de la session)** :
  - Initialiser le projet et publier sur GitHub.
  - Outiller l'environnement avec un Agent IA et son catalogue de missions.
  - Formaliser le flux de travail d'ingénierie.
  - Cadrer le périmètre sous gouvernance Scrum.
  - Modéliser le contexte et les cas d'utilisation avec Mermaid.
  - Structurer le Product Backlog et les issues dans `issues/`.
  - Concevoir l'architecture en 2 couches (Contrôleur mince -> Classe Service).
  - Implémenter la consultation d'un article sous Laravel (gabarit Blade responsive et gestion 404).
```

   Créez également le guide `sprints/README.md` :

```markdown
# Dossier des Sprints (`sprints/`)

Ce dossier centralise la planification et le suivi des Sprints selon la méthodologie Agile/Scrum.

---

## 1. Rôle du dossier

- Il contient le calendrier et les objectifs de chaque sprint du projet.
- Il sert de source de vérité unique (SSOT) pour identifier le sprint actif et sa branche Git associée.
- L'Agent IA consulte ce dossier pour vérifier sur quelle branche de travail il doit opérer.

---

## 2. Règle de gouvernance des Sprints

- Seul le concepteur (ou chef de projet) ajoute de nouveaux sprints dans la planification.
- L'Agent IA ne doit jamais inventer de futurs sprints non validés.
- Chaque sprint actif doit posséder sa branche Git dédiée au format `sprint[N]`.

---

## 3. Contenu du dossier

- [sprints.md](./sprints.md) : Fichier de suivi de la planification des sprints.
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

## 3. Stack technique et Architecture
- **Framework Backend** : Laravel 12 (PHP).
- **Architecture logicielle** : Architecture en 2 couches (Contrôleur mince -> Classe Service).
- **Frontend & Vues** : Alpine.js (SPA, composants réactifs), gabarits Blade responsives, HTML5, CSS3, Tailwind CSS.
- **Base de données** : MySQL.
- **Modélisation** : Diagramme de contexte et cas d'utilisation avec Mermaid.
- **Gestion de versions & Outils** : Git et GitHub CLI (`gh`).
- **Intelligence Artificielle & Automatisation** : Agent Antigravity (Skills natifs et règles Always-On).
- **Documentation et Présentations** : Markdown standard et Marp.

---

## 4. Organisation des dossiers
- [.agents/](./.agents/) : Configuration native de l'Agent IA (règles permanentes et skills outillés avec leurs missions).
- [docs/](./docs/) : Documentation libre, recherches et veilles technologiques personnelles.
- [issues/](./issues/) : Gestion et suivi des tâches et user stories du projet.
- [presentations/](./presentations/) : Diaporamas Marp du projet et des restitutions de sprints.
- [rapport/](./rapport/) : Rapport modulaire du projet, chapitres et script de compilation Node.js.
- [sprints/](./sprints/) : Planification Scrum des sprints et suivi de la branche active.
- [src/](./src/) : Code source de l'application Laravel (architecture 2 couches, contrôleurs, services, vues Blade).
- [tutoriels/](./tutoriels/) : Restitution des tutoriels et ateliers pratiques organisés par domaine.

---

## 5. Méthodologie de développement
Le projet intègre les meilleures pratiques de l'ingénierie logicielle :
- **Agile / Scrum** : Découpage par sprints, réunions quotidiennes et revues de sprint.
- **Processus 2TUP** : Séparation claire entre la branche fonctionnelle et la branche technique.
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
````

4. **Étape 4 — Journalisation des commandes exécutées :**  
   Dans le fichier `tutoriels/realisation-projet/initialisation/readme-stack-technique/readme-stack-technique.command.md`, consignez les commandes exécutées :

```bash
mkdir .agents, docs, issues, tutoriels, presentations, rapport, sprints
```

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - Fichier `README.md` racine propre et conforme au standard Solicode (stack Laravel).
  - Planification Scrum : `sprints/sprints.md` et `sprints/README.md`.
  - Journal des commandes : `tutoriels/realisation-projet/initialisation/readme-stack-technique/readme-stack-technique.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] L'arborescence des dossiers racine est créée à la racine.
  - [ ] Le fichier `README.md` racine documente intégralement la stack technique N3 Laravel et l'architecture en 2 couches.
  - [ ] Les fichiers `sprints/sprints.md` et `sprints/README.md` sont initialisés sur la branche `sprint1`.
  - [ ] Le journal `readme-stack-technique.command.md` est présent et consigne fidèlement les commandes.
