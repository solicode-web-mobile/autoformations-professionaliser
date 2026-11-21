---
layout: default
title: "Fiche d'Atelier : T.351.111 — Comprendre l'approche Agile et Scrum (Cas TodoList)"
---
# T.351.111 : Comprendre l'approche Agile et le cadre Scrum

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-comprendre-scrum.html](./presentation-comprendre-scrum.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Cas d'étude didactique** : Application TodoList (Gestionnaire de tâches)
- **Encadrant** : ESSARRAJ Fouad

---

## 1. Contexte & Objectif de l'Atelier
Cet atelier d'initiation pose les fondations opérationnelles de l'ingénierie logicielle agile. L'objectif est d'assimiler la rupture avec le cycle en V traditionnel, de maîtriser la gouvernance des 3 rôles Scrum et de comprendre le cadencement des 5 rituels à travers l'étude concrète d'une application TodoList.

## 2. Données de Référence
- **Projet support** : Application TodoList (gestionnaire de tâches responsive).
- **Ressources associées** : Diaporama Marp de restitution interactif (`presentation-comprendre-scrum.md`).
- **Périmètre du Sprint 1** : Cadrage du MVP (ajout, affichage et validation d'achèvement d'une tâche).

## 3. Notions Essentielles

### 3.1 Rupture Cycle en V vs Démarche Agile
- **Cycle en V classique** : Cahier des charges exhaustif au démarrage, effet tunnel de plusieurs mois, découverte tardive des écarts par l'utilisateur final.
- **Démarche Agile** : Itérations courtes (Sprints), livraisons régulières d'un incrément logiciel testé et directement utilisable, intégration fluide du changement.

### 3.2 Les 4 Valeurs du Manifeste Agile
- Les individus et leurs interactions avant les processus et les outils.
- Un logiciel opérationnel avant une documentation exhaustive.
- La collaboration avec les clients avant la négociation contractuelle.
- L'adaptation au changement avant le suivi rigide d'un plan.

### 3.3 Les 3 Piliers Empiriques de Scrum
- **Transparence** : Visibilité partagée de l'ensemble des informations et du code source.
- **Inspection** : Évaluation régulière de l'avancement et de la qualité.
- **Adaptation** : Correction immédiate dès le constat d'une dérive par rapport aux objectifs.

### 3.4 Les 3 Rôles Scrum
- **Product Owner (PO)** : Définit la vision produit, recueille les besoins utilisateurs et ordonne les priorités dans le Product Backlog.
- **Scrum Master (SM)** : Coach et facilitateur méthodologique, garant du respect du cadre Scrum et éliminateur d'obstacles.
- **Développeurs** : Équipe autonome et pluridisciplinaire réalisant la conception, le code et les tests de l'incrément.

### 3.5 Les 5 Événements Fondamentaux
- **Sprint** : Boîte de temps fixe (timebox) contenant tous les travaux de développement.
- **Sprint Planning** : Réunion définissant le Sprint Goal et sélectionnant les tâches du Sprint Backlog.
- **Daily Scrum** : Point quotidien de 15 minutes pour mesurer l'avancement et lever les blocages.
- **Sprint Review** : Démonstration live de l'incrément fonctionnel aux parties prenantes.
- **Sprint Retrospective** : Bilan réflexif pour adopter 2 à 3 actions concrètes d'amélioration d'équipe.

## 4. Pratique & Réalisation Guidée (Cas TodoList)

- **Étape 1 — Analyse d'échec du cycle en V sur une TodoList** :
  - La rédaction d'un cahier des charges préalable de 30 pages (sous-tâches, synchronisation cloud, rappels sonores) produit après des mois un outil surchargé alors que l'utilisateur voulait simplement cocher une tâche en 2 secondes sur mobile.
  - L'approche agile livre immédiatement le cœur vital en Sprint 1 (MVP) et reporte les fonctions secondaires (filtres, persistance) aux itérations suivantes.
- **Étape 2 — Définition des rôles au sein de l'équipe TodoList** :
  - Le Product Owner priorise la simplicité d'utilisation et la rapidité de saisie.
  - Le Scrum Master structure le tableau Kanban (To Do, In Progress, QA, Done) et veille à la fluidité du flux.
  - Les Développeurs conçoivent l'interface sémantique HTML5/CSS et la logique JavaScript réactive sans erreur console.
- **Étape 3 — Cadrage du Sprint 1 et engagements qualité** :
  - Sprint Goal fixé : Livrer une interface One-Page responsive permettant de saisir, afficher et cocher ses tâches quotidiennes.
  - Charte d'équipe : code versionné quotidiennement sur la branche active du sprint, tests systématiques sur mobile 375px et console navigateur 100% propre.

## 5. Travail à faire pour l'apprenant (Transposition sur le Projet Technique)

La présente réalisation sur l'application TodoList constitue votre cas d'école de référence.  
Afin d'assimiler concrètement la démarche agile, vous devez réaliser les travaux suivants sur votre propre projet :

- **Étape 1 : Analyse comparative sur votre projet** : Expliquer pourquoi un cycle en V classique ferait courir un risque d'effet tunnel à votre projet technique individuel, et quels sont les bénéfices attendus d'un découpage en sprints.
- **Étape 2 : Cartographie des 3 rôles Scrum** : Identifier qui assume le rôle de Product Owner (partie prenante / formateur), de Scrum Master et de Développeur pour votre projet.
- **Étape 3 : Cadrage du Sprint initial** : Définir le Sprint Goal du premier sprint de votre projet technique et formaliser votre charte d'engagement agile.
- **Étape 4 : Dépôt des livrables** : Rédiger et consigner vos livrables sous :
  - `tutoriels/scrum/initiation-scrum/comprendre-scrum/comprendre-scrum.md`
  - `tutoriels/scrum/initiation-scrum/comprendre-scrum/presentation-comprendre-scrum.md`

## 6. Livrables de Référence Produits & Critères

- **Fiche technique d'atelier** : `ua-lab/scrum/initiation-scrum/comprendre-scrum/comprendre-scrum.md`
- **Diaporama Marp de restitution** : `ua-lab/scrum/initiation-scrum/comprendre-scrum/presentation-comprendre-scrum.md`
- **Critères de réussite validés** :
  - [x] Analyse comparative Cascade vs Agile appliquée à la TodoList.
  - [x] 3 rôles Scrum et 5 événements décrits avec précision opérationnelle.
  - [x] Travail à faire de transposition sur le Projet Technique clairement formulé.
  - [x] Zéro citation d'établissement conformément aux normes du projet.

## 7. Glossaire
- **Sprint** : Boîte de temps fixe pendant laquelle l'équipe conçoit, code et teste un incrément logiciel utilisable.
- **Product Owner** : Responsable qui porte la vision du produit et priorise le backlog selon la valeur utilisateur.
- **Scrum Master** : Facilitateur méthodologique garant du cadre Scrum et de la levée des obstacles.
- **Incrément** : Version concrète, vérifiée selon la Definition of Done et directement utilisable d'un produit.
- **Effet tunnel** : Risque du cycle en V où l'utilisateur ne découvre le produit qu'à la livraison finale sans validation intermédiaire.
