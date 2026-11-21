---
layout: default
title: "Fiche d'Atelier : Planifier, découper et piloter un Sprint"
---
# Tutoriel 4 : Planifier, découper et piloter un Sprint de développement

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-sprint-planning-execution.html](./presentation-sprint-planning-execution.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Encadrant** : ESSARRAJ Fouad | EFP

---

## 1. Objectifs d'apprentissage

Ce quatrième tutoriel permet d'apprendre à organiser le travail quotidien dans un cycle de développement :
- Maîtriser le déroulement de la réunion de planification de sprint (*Sprint Planning*).
- Savoir formuler un *Sprint Goal* clair qui donne du sens au travail de la semaine.
- Sélectionner les User Stories adaptées à sa capacité réelle pour constituer le *Sprint Backlog*.
- Savoir décomposer une fonctionnalité générale en tâches techniques concrètes de code.
- Mettre en place et animer un tableau de suivi visuel (Sprint Board / Kanban).
- Pratiquer le point quotidien (*Daily Scrum*) pour détecter et lever les blocages.
- Appliquer concrètement cette démarche pour piloter le **Sprint 1 de votre Portfolio**.

---

## 2. Volet Théorique : Planification et Pilotage du Sprint

### 2.1 La réunion de planification (Sprint Planning)
Le Sprint Planning se déroule au tout début de chaque itération. Il répond à trois questions fondamentales :
- **Pourquoi ce Sprint a-t-il de la valeur ?** : Définition de l'Objectif de Sprint (*Sprint Goal*).
- **Que peut-on faire dans ce Sprint ?** : Sélection des User Stories prioritaires issues du haut du Product Backlog.
- **Comment le travail sera-t-il réalisé ?** : Découpage technique de chaque User Story en tâches élémentaires de développement.

### 2.2 L'Objectif de Sprint (Sprint Goal)
- Le Sprint Goal est la promesse collective du Sprint : c'est un résultat concret et mesurable.
- Il permet à l'équipe de garder le cap sans se disperser sur des détails accessoires.
- Si un obstacle imprévu survient, l'équipe négocie le périmètre technique des stories avec le Product Owner, tout en protégeant coûte que coûte l'atteinte du Sprint Goal.

### 2.3 Le Sprint Backlog et le découpage en tâches
- Le Sprint Backlog comprend : le Sprint Goal, les User Stories sélectionnées, et la liste détaillée des tâches techniques nécessaires à leur accomplissement.
- **Règle du découpage technique** : Une User Story n'est pas codée d'un seul bloc. Elle est découpée en tâches courtes et précises (idéalement de 1 à 4 heures chacune).
- Cela permet de mesurer l'avancement chaque jour et d'éviter les tâches géantes qui restent bloquées à 90%.

### 2.4 Le suivi quotidien (Daily Scrum)
- C'est un point d'échange rapide (15 minutes maximum), debout ou en ligne, au début de chaque journée de travail.
- Chaque membre de l'équipe répond à 3 questions clés :
  - Qu'ai-je réalisé hier pour contribuer à l'Objectif de Sprint ?
  - Que vais-je accomplir aujourd'hui ?
  - Quels sont les obstacles ou blocages (*impediments*) qui me freinent ?
- Ce n'est pas un rapport hiérarchique au manager, mais une synchronisation d'équipe pour s'entraider.

### 2.5 Le tableau de suivi visuel (Sprint Board / Kanban)
Le tableau de suivi matérialise le flux de travail de gauche à droite à travers 3 ou 4 colonnes :
- **À faire (To Do)** : Toutes les tâches planifiées pour le Sprint, en attente de prise en charge.
- **En cours (In Progress)** : Les tâches actuellement en cours de développement (limiter le travail en cours pour finir avant de commencer autre chose).
- **Terminé (Done)** : Les tâches achevées satisfaisant pleinement à la Definition of Done.

---

## 3. Application Pratique : Lancement du Sprint 1 du Portfolio

### 3.1 Définition du Sprint Goal du Sprint 1
- **Sprint Goal** : *"Déployer la première version responsive One-Page présentant mon identité professionnelle, mes compétences clés et deux projets phares avec leurs liens GitHub."*
- **Durée** : 1 semaine (5 jours de travail).

### 3.2 Sélection des User Stories du Sprint 1
Pour respecter une charge de travail réaliste d'une semaine sans surcharge, nous sélectionnons 3 stories prioritaires du Product Backlog :
- **US-01** : Présentation personnelle et en-tête (2 points).
- **US-03** : Section Compétences techniques (3 points).
- **US-02** : Vitrine des deux projets phares (5 points).
- **Charge totale engagée pour le Sprint 1** : **10 Story Points**.
- Les stories restantes (US-04 Contact et US-05 Téléchargement CV) sont planifiées pour le Sprint 2.

### 3.3 Décomposition des User Stories en tâches techniques

- **Tâches pour US-01 (Présentation - 2 pts)** :
  - *Tâche 1.1* : Structurer le balisage HTML5 sémantique (`<header>`, `<nav>`, `<section id="hero">`).
  - *Tâche 1.2* : Rédiger le texte de présentation professionnelle et choisir un titre percutant.
  - *Tâche 1.3* : Optimiser et intégrer la photo de profil (format WebP, dimensionnement responsive).
  - *Tâche 1.4* : Appliquer les styles CSS modernes (typographie lisible, espacements, alignements Flexbox).

- **Tâches pour US-03 (Compétences - 3 pts)** :
  - *Tâche 2.1* : Structurer le balisage HTML de la section compétences (`<section id="skills">`).
  - *Tâche 2.2* : Concevoir la grille responsive CSS (CSS Grid) avec 3 colonnes : Front-End, Back-End, Outils.
  - *Tâche 2.3* : Styliser les badges de compétences (couleurs, bordures douces, contrastes accessibles).
  - *Tâche 2.4* : Tester l'affichage sur petit écran mobile (bascule automatique en une seule colonne).

- **Tâches pour US-02 (Projets phares - 5 pts)** :
  - *Tâche 3.1* : Réaliser 2 captures d'écran soignées de vos projets et les compresser.
  - *Tâche 3.2* : Structurer le balisage HTML des cartes de projets (`<article class="project-card">`).
  - *Tâche 3.3* : Coder les liens et boutons vers les démos en ligne et dépôts GitHub avec attributs de sécurité.
  - *Tâche 3.4* : Styliser les cartes (effets de survol légers, marges régulières, ombres douces).
  - *Tâche 3.5* : Vérifier que chaque lien fonctionne et s'ouvre dans un nouvel onglet sans erreur 404.

### 3.4 Organisation du tableau de suivi Kanban
- Créez votre tableau de bord visuel (sur papier, tableau blanc ou outil de suivi).
- Placez l'ensemble des 13 tâches techniques dans la colonne **À faire**.
- **Règle de discipline** : Ne prenez qu'une seule tâche à la fois dans la colonne **En cours**. Terminez-la, vérifiez sa conformité avec la DoD, puis déplacez-la dans **Terminé** avant d'entamer la suivante.

### 3.5 Déroulement du suivi quotidien sur les 5 jours
- **Jour 1** : Réalisation et validation de l'US-01 (Présentation). Déplacement des tâches 1.1 à 1.4 dans Terminé.
- **Jour 2** : Structure et mise en page CSS de l'US-03 (Compétences - tâches 2.1 et 2.2).
- **Jour 3** : Finalisation des badges et tests responsive de l'US-03 (tâches 2.3 et 2.4).
- **Jour 4** : Conception des cartes de projets de l'US-02 (tâches 3.1 à 3.3).
- **Jour 5** : Finitions CSS, tests des liens externes (tâches 3.4 et 3.5) et vérification finale de la DoD.

---

## 4. Auto-évaluation et Validation

Vérifiez les acquis suivants avant la clôture du sprint :
- Vous avez formulé un Sprint Goal clair pour votre première semaine.
- Votre Sprint Backlog compte 10 Story Points découpés en sous-tâches concrètes.
- Vous utilisez un tableau de tâches avec une colonne "En cours" limitée.
- Vous avez appliqué le rituel du point quotidien pour suivre votre propre cadence.
- Vous êtes prêt à présenter votre incrément lors de la Sprint Review dans le Tutoriel 5.
