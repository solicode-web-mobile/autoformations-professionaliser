# Plan des Tutoriels : D.351.2 — Réalisation de Projet & Rituels Agiles

> **Domaine :** `D.351.2` | **Compétence :** `C.351` — Piloter un projet avec Scrum et gouverner les cérémonies | **Session :** S01  
> **Niveau de Maturité :** UA-tâche (Niveau 0 — Cadrage, cérémonies et phases de projet)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.351.21 — Lancement et cadrage initial du projet (Sprint 1)

- **Code :** `UA.351.21`
- **Maturité :** `UA-tâche` (Cadrage et lancement de projet)
- **Ordre en Session :** Étape 01
- **Positionnement Flux de Travail :** Phase A — Cadrage, Gouvernance & Outillage
- **Briques Stack Technique :** Git, GitHub, VS Code, Laravel 12, Pitch Deck
- **Compétence :** `C.351` — Piloter un projet avec Scrum et gouverner les cérémonies
- **Domaine :** `D.351.2` — Réalisation de projet et rituels agiles
- **Durée estimée :** 6 heures
- **Objectif :** Initialiser le projet collectif et individuel, valider l'environnement de développement et présenter le pitch de cadrage.
- **Description :** Poser les bases opérationnelles du projet. L'apprenant contractualise la charte de cadrage, initialise le dépôt Git, valide sa checklist d'environnement outillé et présente le pitch de lancement du premier sprint.
- **Notions Clés Utilisées dans le Sprint :**
  - Cadrage d'un projet informatique (vision, parties prenantes, périmètre).
  - Gestion de configuration logicielle sous Git et GitHub.
  - Checklist de validation d'un environnement moderne de développement full-stack.
  - Techniques de pitch de synthèse technique et d'alignement d'équipe.
- **Livrables :** Charte de cadrage, dépôt Git initialisé, checklist environnement validée, support de présentation S1 (`presentation-s01.md`).
- **Travail à Faire :** Réaliser les 3 tutoriels opérationnels `T.351.211`, `T.351.212` et `T.351.213`.

---

### UA.351.22 — Planification de sprint et engagement d'équipe (Sprint 1)

- **Code :** `UA.351.22`
- **Maturité :** `UA-tâche` (Planification Scrum de sprint)
- **Ordre en Session :** Étape 06
- **Positionnement Flux de Travail :** Phase B — Analyse, Conception & Planification
- **Briques Stack Technique :** Sprint Backlog, Planning Poker, Definition of Done, Kanban
- **Compétence :** `C.351` — Piloter un projet avec Scrum et gouverner les cérémonies
- **Domaine :** `D.351.2` — Réalisation de projet et rituels agiles
- **Durée estimée :** 4 heures
- **Objectif :** Animer le rituel de Sprint Planning, estimer l'effort relatif, formaliser le Sprint Backlog et contractualiser la Definition of Done.
- **Description :** Cérémonie de planification du sprint. L'équipe sélectionne les User Stories du Product Backlog, les découpe en tâches techniques, calibre l'effort et s'engage collectivement sur le Sprint Goal.
- **Notions Clés Utilisées dans le Sprint :**
  - Rituel du Sprint Planning en 2 parties (Quoi et Comment).
  - Estimation d'effort en Story Points (suite de Fibonacci).
  - Décomposition des User Stories en tâches techniques élémentaires.
  - Contractualisation de la Definition of Done (DoD) en 7 critères bloquants.
- **Livrables :** Sprint Backlog S1 (`scrum/sprint-backlog-s1.md`) et tableau Kanban initialisé.
- **Travail à Faire :** Réaliser le tutoriel opérationnel `T.351.221`.

---

### UA.351.23 — Clôture de sprint, démonstration et rétrospective (Sprint 1)

- **Code :** `UA.351.23`
- **Maturité :** `UA-tâche` (Cérémonies de clôture et amélioration continue)
- **Ordre en Session :** Étape 12
- **Positionnement Flux de Travail :** Phase D — Clôture de Sprint, Rétrospective & Bilan
- **Briques Stack Technique :** Sprint Review, Sprint Retrospective, Backlog Grooming, Bilan
- **Compétence :** `C.351` — Piloter un projet avec Scrum et gouverner les cérémonies
- **Domaine :** `D.351.2` — Réalisation de projet et rituels agiles
- **Durée estimée :** 6 heures
- **Objectif :** Valider l'incrément en Sprint Review, animer la rétrospective réflexive (dette d'empathie), affiner le Backlog et dresser le bilan de session.
- **Description :** Phase de clôture et d'amélioration continue. L'équipe démontre l'incrément déployable aux parties prenantes, conduit une rétrospective approfondie mettant en évidence l'absence d'empathie utilisateur (dette justifiant S02), affine le Product Backlog pour le sprint suivant et formalise son débriefing de progression.
- **Notions Clés Utilisées dans le Sprint :**
  - Démonstration fonctionnelle interactive en direct (Sprint Review).
  - Validation de la Definition of Done (DoD) critère par critère.
  - Dynamique réflexive de rétrospective (forces, freins, axes de progrès).
  - Analyse didactique de dette méthodologique (manque de Design Thinking).
  - Backlog Refinement et projection de vélocité.
- **Livrables :** Procès-verbal de démonstration, grille DoD validée, compte-rendu de rétrospective (`scrum/retrospective-s1.md`), Product Backlog affiné pour Sprint 2, bilan individuel de progression.
- **Travail à Faire :** Réaliser les 4 tutoriels opérationnels `T.351.231`, `T.351.232`, `T.351.233` et `T.351.234`.

---

## 2. Plan des Tutoriels : UA.351.21

### T.351.211 — Cadrage initial et lancement du projet (Sprint 1)

- **Code :** `T.351.211`
- **Maturité :** `UA-tâche` (Tutoriel pas-à-pas opérationnel)
- **Unité d'Apprentissage parente :** `UA.351.21`
- **Titre Canonique :** Cadrage initial et lancement du projet (Sprint 1)
- **Durée :** 2 heures
- **Objectif Opérationnel :** Contractualiser la charte de cadrage projet et initialiser le dépôt Git versionné.
- **Prérequis :** Maîtrise des commandes Git de base (`init`, `commit`, `branch`).
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Définir la vision du produit *Blog des Lauréats* et clarifier les objectifs du Sprint 1.
  2. *Étape 2 :* Initialiser le dépôt Git local et distant (GitHub) avec `.gitignore` standard Laravel.
  3. *Étape 3 :* Rédiger le fichier `charte-cadrage.md` consignant les engagements initiaux.
- **Critère de Réussite :** Le dépôt Git est configuré, accessible et la charte de cadrage est validée.

---

### T.351.212 — Validation de l'environnement technique (Sprint 1)

- **Code :** `T.351.212`
- **Maturité :** `UA-tâche` (Tutoriel pas-à-pas opérationnel)
- **Unité d'Apprentissage parente :** `UA.351.21`
- **Titre Canonique :** Validation de l'environnement technique (Sprint 1)
- **Durée :** 2 heures
- **Objectif Opérationnel :** Vérifier et valider l'outillage local de développement pour l'ensemble de la promotion.
- **Prérequis :** PHP 8.3+, Composer, Node.js 20+, VS Code installés.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Exécuter la checklist de diagnostic des binaires (`php -v`, `composer -V`, `node -v`).
  2. *Étape 2 :* Installer et configurer les extensions recommandées sous VS Code (PHP Intelephense, Tailwind CSS, Mermaid Previewer).
  3. *Étape 3 :* Valider la génération d'un diagramme Mermaid de test en local.
- **Critère de Réussite :** 100% des éléments de la checklist environnement sont validés sans avertissement bloquant.

---

### T.351.213 — Réalisation du pitch de lancement (Sprint 1)

- **Code :** `T.351.213`
- **Maturité :** `UA-tâche` (Tutoriel pas-à-pas opérationnel)
- **Unité d'Apprentissage parente :** `UA.351.21`
- **Titre Canonique :** Réalisation du pitch de lancement (Sprint 1)
- **Durée :** 2 heures
- **Objectif Opérationnel :** Concevoir et présenter le support de pitch pour lancer la dynamique du Sprint 1.
- **Prérequis :** Prise de connaissance du sujet d'imitation et des objectifs certifiants N3.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Rédiger la structure du pitch en 5 slides Markdown (`presentation-s01.md`).
  2. *Étape 2 :* Formuler la proposition de valeur et les personas cibles préliminaires.
  3. *Étape 3 :* Réaliser une restitution orale chronométrée de 5 minutes devant l'équipe.
- **Critère de Réussite :** Le support `presentation-s01.md` est finalisé et le pitch est approuvé par le formateur.

---

## 3. Plan des Tutoriels : UA.351.22

### T.351.221 — Sprint Planning et engagement d'équipe (Sprint 1)

- **Code :** `T.351.221`
- **Maturité :** `UA-tâche` (Tutoriel pas-à-pas opérationnel)
- **Unité d'Apprentissage parente :** `UA.351.22`
- **Titre Canonique :** Sprint Planning et engagement d'équipe (Sprint 1)
- **Durée :** 4 heures
- **Objectif Opérationnel :** Animer la planification du Sprint 1, découper l'incrément en tâches techniques et contractualiser l'engagement d'équipe.
- **Prérequis :** Product Backlog initial validé (`UA.351.12`).
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Examiner la User Story prioritaire : *« Consultation détaillée d'un article de blog »*.
  2. *Étape 2 :* Découper la Story en tâches techniques d'ingénierie (architecture, route, contrôleur, vue, service CSV).
  3. *Étape 3 :* Évaluer l'effort technique en Story Points et renseigner le `sprint-backlog-s1.md`.
  4. *Étape 4 :* Valider formellement la grille Definition of Done (DoD) en 7 critères bloquants.
- **Critère de Réussite :** Le document `sprint-backlog-s1.md` est complet, les tâches sont réparties sur le Kanban et l'engagement d'équipe est validé.

---

## 4. Plan des Tutoriels : UA.351.23

### T.351.231 — Sprint Review et démonstration live (Sprint 1)

- **Code :** `T.351.231`
- **Maturité :** `UA-tâche` (Tutoriel pas-à-pas opérationnel)
- **Unité d'Apprentissage parente :** `UA.351.23`
- **Titre Canonique :** Sprint Review et démonstration live (Sprint 1)
- **Durée :** 1 heure 30
- **Objectif Opérationnel :** Conduire la démonstration fonctionnelle live de l'incrément et valider la DoD avec les parties prenantes.
- **Prérequis :** Code applicatif Laravel 12 stabilisé et fonctionnel.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Démarrer le serveur de développement local et préparer les scénarios de test nominaux et d'erreur (404).
  2. *Étape 2 :* Présenter la fonctionnalité de consultation d'article en direct devant le formateur Product Owner.
  3. *Étape 3 :* Émarger la grille de Definition of Done (7/7 critères validés).
- **Critère de Réussite :** L'incrément est validé en séance sans plantage et le PV de revue est rédigé.

---

### T.351.232 — Sprint Retrospective et dette d'empathie (Sprint 1)

- **Code :** `T.351.232`
- **Maturité :** `UA-tâche` (Tutoriel pas-à-pas opérationnel)
- **Unité d'Apprentissage parente :** `UA.351.23`
- **Titre Canonique :** Sprint Retrospective et dette d'empathie (Sprint 1)
- **Durée :** 1 heure 30
- **Objectif Opérationnel :** Animer le rituel de rétrospective agile et formaliser le constat réflexif de dette méthodologique pour le sprint suivant.
- **Prérequis :** Clôture de la Sprint Review.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Animer la collecte des ressentis (ce qui a bien fonctionné, ce qui a posé problème).
  2. *Étape 2 :* Analyser la question réflexive didactique : l'écran codé répond-il aux besoins réels d'utilisateurs testés ?
  3. *Étape 3 :* Consigner le constat de dette d'empathie dans `scrum/retrospective-s1.md` justifiant l'intégration du Design Thinking en Session S02.
- **Critère de Réussite :** Le rapport `retrospective-s1.md` est formalisé et la dette d'empathie est actée pour le Sprint 2.

---

### T.351.233 — Raffinement du Product Backlog (Sprint 1)

- **Code :** `T.351.233`
- **Maturité :** `UA-tâche` (Tutoriel pas-à-pas opérationnel)
- **Unité d'Apprentissage parente :** `UA.351.23`
- **Titre Canonique :** Raffinement du Product Backlog (Sprint 1)
- **Durée :** 1 heure 30
- **Objectif Opérationnel :** Actualiser, ré-estimer et réordonner le Product Backlog pour préparer le Sprint 2.
- **Prérequis :** Bilan de la Sprint Review et de la Retrospective.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Intégrer les retours d'utilisateurs et ajuster les User Stories en suspens.
  2. *Étape 2 :* Définir les critères d'acceptation préliminaires pour les Stories du Sprint 2 (Personas, Formulaire de création, persistance).
  3. *Étape 3 :* Actualiser le fichier `scrum/product-backlog.md`.
- **Critère de Réussite :** Le Product Backlog actualisé reflète fidèlement la trajectoire du Sprint 2.

---

### T.351.234 — Débriefing de session et bilan de progression (Sprint 1)

- **Code :** `T.351.234`
- **Maturité :** `UA-tâche` (Tutoriel pas-à-pas opérationnel)
- **Unité d'Apprentissage parente :** `UA.351.23`
- **Titre Canonique :** Débriefing de session et bilan de progression (Sprint 1)
- **Durée :** 1 heure 30
- **Objectif Opérationnel :** Dresser le bilan individuel et collectif d'acquisition des compétences sur les 80h de formation.
- **Prérequis :** Épreuve de Live Coding 40 min terminée et cérémonies Scrum clôturées.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Remplir la grille d'auto-évaluation réflexive sur les compétences mobilisées ($C.311, C.312, C.321, C.325, C.351$).
  2. *Étape 2 :* Analyser les axes d'amélioration identifiés lors de l'épreuve de Live Coding.
  3. *Étape 3 :* Clôturer le journal de session et valider la feuille de progression individuelle.
- **Critère de Réussite :** La fiche de débriefing individuel est complétée et archivée dans le dossier de progression de l'apprenant.
