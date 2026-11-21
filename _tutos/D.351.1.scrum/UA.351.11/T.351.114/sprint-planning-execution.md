---
layout: tuto
title: "Planifier, découper et piloter un Sprint de développement"
sous_titre: "Fixer le Sprint Goal, constituer le Sprint Backlog, découper en tâches techniques et animer le Kanban"
slug: "sprint-planning-execution"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
permalink: /tutos/sprint-planning-execution/
tuto_id: "T.351.114"
version: "normal"
ua: "UA.351.11"
type: "tuto-atelier-notions"
nav_order: 4
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
sprint: "sprint1"
statut_realisation: "realise"
livrables:
  - chemin: "tutoriels/scrum/initiation-scrum/sprint-planning-execution/sprint-planning-execution.md"
    version: "1.0.0"
  - chemin: "tutoriels/scrum/initiation-scrum/sprint-planning-execution/presentation-sprint-planning-execution.md"
    version: "1.0.0"
---

## 1. Travail à faire
Organiser le travail d'une itération de développement sur votre projet technique individuel : formuler l'Objectif de Sprint (*Sprint Goal*), sélectionner les User Stories du *Sprint Backlog*, décomposer les stories en tâches techniques courtes et animer un tableau visuel de suivi (Kanban) avec points quotidiens (*Daily Scrum*).

> [!NOTE]
> **Projet Technique de Référence :** Ce tutoriel est rédigé et illustré à partir du **Portfolio Développeur**, qui sert d'exemple concret de Projet Technique. Vous devez appliquer et transposer cette méthode de planification et de suivi à **votre propre projet technique**.

## 2. Notions fondamentales
- **La Réunion de Planification (Sprint Planning) :**
  - Se déroule au démarrage du sprint et répond à 3 questions : *Pourquoi ce sprint a-t-il de la valeur ?* (Sprint Goal), *Que peut-on faire ?* (sélection dans le Product Backlog), *Comment le travail sera-t-il réalisé ?* (découpage en tâches techniques).
- **L'Objectif de Sprint (Sprint Goal) :**
  - Promesse collective du sprint. Donne du sens et permet d'arbitrer le périmètre en cas d'imprévu sans sacrifier l'objectif central.
- **Le Sprint Backlog et le Découpage Technique :**
  - Comprend le Sprint Goal, les User Stories sélectionnées et l'ensemble des tâches élémentaires.
  - *Règle d'or :* Une User Story est obligatoirement découpée en micro-tâches techniques courtes (1 à 4 heures chacune) pour mesurer l'avancement quotidien et éviter les blocages invisibles.
- **Le Point Quotidien (Daily Scrum) :**
  - Point d'équipe court (15 minutes maximum) centré sur 3 questions : *Qu'ai-je réalisé hier ?*, *Que vais-je faire aujourd'hui ?*, *Quels sont les obstacles rencontrés ?*.
- **Le Tableau de Suivi Visuel (Sprint Board / Kanban) :**
  - Matérialise le flux à travers 3 colonnes : *À faire (To Do)*, *En cours (In Progress)*, *Terminé (Done)*.
  - Limite le travail en cours (WIP) pour finir les tâches avant d'en ouvrir de nouvelles.

## 3. Application pratique sur le Projet Technique (Exemple Portfolio)
- **Exemple de Sprint Goal (Sprint 1) :** Déployer la première version responsive One-Page présentant mon identité professionnelle, mes compétences clés et deux projets phares avec leurs liens GitHub fonctionnels.
- **Exemple de sélection (Sprint Backlog 1) :**
  - US-01 : Présentation personnelle et en-tête (2 points).
  - US-03 : Section Compétences techniques (3 points).
  - US-02 : Vitrine des réalisations (5 points).
  - *Charge totale engagée :* **10 Story Points** sur 5 jours ouvrés.
- **Exemple de décomposition en 13 tâches techniques élémentaires :**
  - *US-01 (4 tâches) :* Balisage HTML5 sémantique, rédaction des textes, optimisation de la photo (WebP), styles CSS et Flexbox.
  - *US-03 (4 tâches) :* Balisage HTML des compétences, grille responsive CSS Grid, styles des badges et tests d'adaptation mobile.
  - *US-02 (5 tâches) :* 2 captures d'écran optimisées, balisage des cartes de projets, boutons d'action sécurisés, styles CSS et vérification des liens externes.
- **Pilotage sur 5 jours :**
  - *Jour 1 :* Réalisation et validation de l'US-01.
  - *Jours 2 et 3 :* Intégration et validation de l'US-03.
  - *Jours 4 et 5 :* Réalisation de l'US-02, tests finaux et contrôle DoD.

## 4. Livrables & Critères de validation
- **Livrables attendus :**
  - Fiche technique d'atelier : `tutoriels/scrum/initiation-scrum/sprint-planning-execution/sprint-planning-execution.md` sur la branche `sprint1`.
  - Diaporama Marp de restitution : `tutoriels/scrum/initiation-scrum/sprint-planning-execution/presentation-sprint-planning-execution.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le Sprint Goal du Sprint 1 est clair, mesurable et contextualisé à votre projet technique.
  - [ ] Le Sprint Backlog engage un nombre de Story Points réaliste adapté à la durée du sprint.
  - [ ] Les User Stories sont découpées en tâches techniques d'une durée unitaire $\le 4$ heures.
  - [ ] La discipline du tableau Kanban avec limitation du travail en cours est appliquée.
