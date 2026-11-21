---
layout: tuto
title: "Planifier le Sprint 0 et formaliser la feuille d'engagement d'équipe"
sous_titre: "Contractualiser l'organisation agile avec le Product Owner et définir les engagements du Sprint 0"
slug: "planifier-sprint-0"
slug_domaine: "realisation-projet"
slug_ua: "depot-cadrage-stack-backlog"
permalink: /tutos/planifier-sprint-0/
tuto_id: "T.351.011"
version: "normal"
ua: "UA.351.01"
type: "tuto-tache"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
livrables:
  - chemin: "sprints/sprint-0.md"
    version: "0.1.0"
---

## 1. Travail à faire
Organisez le travail de cadrage du Sprint 0 sur le projet du *Blog des Lauréats* :
1. **Étape 1 — Contractualiser avec le Product Owner :** Prenez contact avec les représentants du **Groupe 1** (Product Owner) pour caler les modalités de collaboration et les créneaux d'arbitrage fonctionnel.
2. **Étape 2 — Répartir les responsabilités d'équipe :** Désignez le Scrum Master et les Développeurs au sein de votre équipe projet.
3. **Étape 3 — Cadrer la timebox :** Enregistrez la durée indicative du sprint (10 jours ouvrés / 80 heures) ainsi que les dates de début et de fin du Sprint 0.
4. **Étape 4 — Formaliser la Definition of Done (DoD) de cadrage :** Définissez la liste des critères d'acceptation stricts que tout livrable de cadrage doit respecter avant d'être présenté en revue de sprint.
5. **Étape 5 — Rédiger la feuille d'engagement :** Créez le fichier `sprints/sprint-0.md` et faites-le signer par l'ensemble des membres de l'équipe et le Product Owner.

## 2. Consignes de Réalisation
- Créez le répertoire dédié aux cérémonies de sprint :
  ```powershell
  mkdir sprints
  ```
- Créez le fichier de planification du sprint :
  ```powershell
  echo "" > sprints/sprint-0.md
  ```
- Renseignez les sections obligatoires de `sprints/sprint-0.md` :
  - Identification du projet, du sprint et de la branche Git active (`sprint0`).
  - Composition nominative de l'équipe et rôle attribué à chaque membre.
  - Objectif de sprint (*Sprint Goal* centré sur la maquette de la page d'accueil).
  - Critères explicites de la Definition of Done (DoD) de cadrage.
  - Calendrier prévisionnel des cérémonies (Daily, Sprint Review 0, Rétrospective 0).

## 3. Livrable attendu
- **Fichier de projet :** `sprints/sprint-0.md`.
- **Critère de conformité :** La feuille d'engagement est complète, signée et validée conjointement avec le Product Owner.
