---
layout: presentation
title: "Présentation : T.351.114 — Sprint Planning et Pilotage Kanban (Cas TodoList)"
marp: true
theme: default
paginate: true
header: "T.351.114 : Sprint Planning et Pilotage Kanban"
footer: "Scrum & Ingénierie Agile"
nav_exclude: true
---

<!-- _class: lead -->
# T.351.114 : Planifier, découper et piloter un Sprint de développement
### Cas d'étude didactique : Application TodoList
**Unité d'Apprentissage : UA.351.11 — Initiation Scrum**

- **Public** : Développeurs Web (Niveau N3)
- **Domaine** : Scrum & Ingénierie Agile (`D.351.1`)
- **Compétence** : `C.351` — Piloter et animer la démarche Scrum

---

## 1. Le Sprint Planning & Le Sprint Goal

- **Les 3 questions du Sprint Planning :**
  1. *Pourquoi ce sprint a-t-il de la valeur ?* $\rightarrow$ Le **Sprint Goal**.
  2. *Que peut-on faire ?* $\rightarrow$ Sélection du **Sprint Backlog**.
  3. *Comment allons-nous le concevoir ?* $\rightarrow$ Découpage technique.

- **Sprint Goal du Sprint 1 (TodoList) :**
  > *"Livrer une première version opérationnelle permettant de saisir, d'afficher et de cocher ses tâches quotidiennes en toute fluidité."*

---

## 2. Découpage en Micro-Tâches Techniques Courtes

### La règle d'or : Tâches de 1 à 3 heures
- Évite les retards invisibles et les blocages prolongés.
- Facilite l'entraide immédiate au sein de l'équipe.

### Découpage des 8 Story Points en 9 micro-tâches :
- **US-02 (2 pts) :** T-01 Squelette HTML (1h30), T-02 CSS responsive (2h), T-03 Compteur dynamique (1h).
- **US-01 (3 pts) :** T-04 Formulaire (1h), T-05 Écouteur submit (1h30), T-06 Création nœud DOM (2h).
- **US-03 (3 pts) :** T-07 Checkbox interactive (1h30), T-08 Style barré & recalcul (1h30), T-09 Test DoD (2h30).

---

## 3. Le Management Visuel Kanban

- **Les 4 colonnes du tableau :**
  - **À faire (To Do)**
  - **En cours (In Progress)** $\rightarrow$ *WIP Limit : maximum 2 tâches en cours simultanées*.
  - **En revue (Review / QA)**
  - **Terminé (Done)** $\rightarrow$ *100% conforme à la Definition of Done*.

> **Devise Agile :** « Arrêter de commencer, commencer à terminer ! »

---

## 4. Le Daily Scrum & La Levée d'Obstacles

- **Le rituel en 15 minutes chrono (debout) :**
  - *Qu'ai-je accompli hier ?*
  - *Que vais-je faire aujourd'hui ?*
  - *Quels sont les obstacles qui me bloquent ?*

- **Cas vécu sur la TodoList (Jour 3) :**
  - **Obstacle :** Rechargement intempestif de la page lors de la touche Entrée.
  - **Action du Scrum Master :** Conseil technique post-réunion pour injecter `event.preventDefault()`.
  - **Résultat :** Blocage résolu en 10 minutes, livraison sécurisée dans les temps.

---

<!-- _class: lead -->
# Conclusion de l'Atelier T.351.114
### Prêt pour la Démonstration et la Rétrospective

- Le sprint s'exécute avec fluidité grâce au découpage court et au Kanban.
- **Prochaine étape (T.351.115) :** Valider l'incrément en direct lors de la Sprint Review et animer la Sprint Retrospective.
