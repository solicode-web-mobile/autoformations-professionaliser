---
layout: tuto
title: "CrÃ©ation du prompt-sprint-planning"
sous_titre: "Concevoir le prompt d'ingÃ©nierie prompt-sprint-planning pour automatiser la dÃ©composition des User Stories en tÃ¢ches de sprint"
slug: "prompt-engagement-equipe"
slug_domaine: "realisation-projet"
slug_ua: "planification"
permalink: /tutos/prompt-engagement-equipe/
tuto_id: "T.351.242"
version: "normal"
ua: "UA.351.24"
maturite: "projet"
type: "tuto-tache"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail Ã  faire
Concevoir et tester le prompt d'ingÃ©nierie rÃ©utilisable nommÃ© `prompt-sprint-planning.prompt.md` selon la mÃ©thode RIO.

Ce prompt est un composant agentique rÃ©utilisable permettant Ã  un Agent IA d'automatiser la sÃ©ance de Sprint Planning sur le Projet Fil Rouge : extraire les User Stories prioritaires, les dÃ©composer en tÃ¢ches d'ingÃ©nierie concrÃ¨tes et contractualiser la grille de Definition of Done (DoD).

## 2. Missions ConcrÃ¨tes RÃ©alisÃ©es par le Prompt
1. Extraire les User Stories sÃ©lectionnÃ©es pour le sprint depuis le Product Backlog.
2. DÃ©composer chaque User Story en tÃ¢ches techniques concrÃ¨tes adaptÃ©es Ã  la stack logicielle du projet.
3. RÃ©diger le document `sprint-backlog.md` avec matrice de suivi, estimation d'effort et checklist DoD face au Sprint Goal.

## 3. Cahier des Charges du Prompt (MÃ©thode RIO)
- **RÃ´le (Persona) :** Scrum Master & Coach Agile senior expert en dÃ©composition de tÃ¢ches techniques et gouvernance Scrum.
- **Instruction (Contexte & TÃ¢che) :** Prendre en entrÃ©e les User Stories retenues pour le sprint et produire la dÃ©composition technique dÃ©taillÃ©e avec critÃ¨res DoD bloquants.
- **Output (Format de sortie) :** Fichier Markdown structurÃ© directement intÃ©grable dans `scrum/sprint-backlog-[ID].md`.
- **Contraintes NÃ©gatives :**
  - Pas de tÃ¢ches vagues ou gÃ©nÃ©riques ; chaque tÃ¢che doit spÃ©cifier les fichiers cibles impactÃ©s.
  - ZÃ©ro tableau Markdown dans la dÃ©composition.
  - Pas de bavardage conversationnel.

## 4. Livrables & CritÃ¨res de validation
- **Livrable attendu :**
  - Fichier de prompt rÃ©utilisable : `tutoriels/realisation-projet/planification/prompt-engagement-equipe/prompt-sprint-planning.prompt.md` sur la branche `sprint1`.
- **CritÃ¨res de validation :**
  - [ ] Le prompt est rÃ©digÃ© selon le formalisme RIO avec ses contraintes nÃ©gatives explicites.
  - [ ] TestÃ© avec une User Story d'application mÃ©tier, il produit un dÃ©coupage technique prÃ©cis avec critÃ¨res DoD.
  - [ ] Le document gÃ©nÃ©rÃ© est immÃ©diatement exploitable pour le suivi de sprint.
