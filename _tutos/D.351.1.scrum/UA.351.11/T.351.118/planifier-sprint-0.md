---
layout: tuto
title: "Planifier le Sprint 0 et formaliser la feuille d'engagement d'Ã©quipe"
sous_titre: "Contractualiser l'organisation agile avec le Product Owner et dÃ©finir les engagements du Sprint 0"
slug: "planifier-sprint-0"
slug_domaine: "scrum"
slug_ua: "UA.351.11"
permalink: /tutos/planifier-sprint-0/
tuto_id: "T.351.118"
version: "normal"
ua: "UA.351.11"
type: "tuto-tache"
etape: 10
nav_order: 8
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
livrables:
  - chemin: "sprints/sprint-0.md"
    version: "0.1.0"
---

## 1. Travail Ã  faire
Organisez le travail de cadrage du Sprint 0 sur le projet du *Blog des LaurÃ©ats* :
1. **Ã‰tape 1 â€” Contractualiser avec le Product Owner :** Prenez contact avec les reprÃ©sentants du **Groupe 1** (Product Owner) pour caler les modalitÃ©s de collaboration et les crÃ©neaux d'arbitrage fonctionnel.
2. **Ã‰tape 2 â€” RÃ©partir les responsabilitÃ©s d'Ã©quipe :** DÃ©signez le Scrum Master et les DÃ©veloppeurs au sein de votre Ã©quipe projet.
3. **Ã‰tape 3 â€” Cadrer la timebox :** Enregistrez la durÃ©e indicative du sprint (10 jours ouvrÃ©s / 80 heures) ainsi que les dates de dÃ©but et de fin du Sprint 0.
4. **Ã‰tape 4 â€” Formaliser la Definition of Done (DoD) de cadrage :** DÃ©finissez la liste des critÃ¨res d'acceptation stricts que tout livrable de cadrage doit respecter avant d'Ãªtre prÃ©sentÃ© en revue de sprint.
5. **Ã‰tape 5 â€” RÃ©diger la feuille d'engagement :** CrÃ©ez le fichier `sprints/sprint-0.md` et faites-le signer par l'ensemble des membres de l'Ã©quipe et le Product Owner.

## 2. Consignes de RÃ©alisation
- CrÃ©ez le rÃ©pertoire dÃ©diÃ© aux cÃ©rÃ©monies de sprint :
  ```powershell
  mkdir sprints
  ```
- CrÃ©ez le fichier de planification du sprint :
  ```powershell
  echo "" > sprints/sprint-0.md
  ```
- Renseignez les sections obligatoires de `sprints/sprint-0.md` :
  - Identification du projet, du sprint et de la branche Git active (`sprint0`).
  - Composition nominative de l'Ã©quipe et rÃ´le attribuÃ© Ã  chaque membre.
  - Objectif de sprint (*Sprint Goal* centrÃ© sur la maquette de la page d'accueil).
  - CritÃ¨res explicites de la Definition of Done (DoD) de cadrage.
  - Calendrier prÃ©visionnel des cÃ©rÃ©monies (Daily, Sprint Review 0, RÃ©trospective 0).

## 3. Livrable attendu
- **Fichier de projet :** `sprints/sprint-0.md`.
- **CritÃ¨re de conformitÃ© :** La feuille d'engagement est complÃ¨te, signÃ©e et validÃ©e conjointement avec le Product Owner.
