---
layout: tuto
title: "Création du prompt-sprint-planning"
sous_titre: "Concevoir le prompt d'ingénierie prompt-sprint-planning pour automatiser la décomposition des User Stories en tâches de sprint"
slug: "prompt-engagement-equipe"
slug_domaine: "realisation-projet"
slug_ua: "planification"
permalink: /tutos/prompt-engagement-equipe/
tuto_id: "T.351.222"
version: "normal"
ua: "UA.351.22"
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

## 1. Travail à faire
Concevoir et tester le prompt d'ingénierie réutilisable nommé `prompt-sprint-planning.prompt.md` selon la méthode RIO.

Ce prompt est un composant agentique réutilisable permettant à un Agent IA d'automatiser la séance de Sprint Planning sur le Projet Fil Rouge : extraire les User Stories prioritaires, les décomposer en tâches d'ingénierie concrètes et contractualiser la grille de Definition of Done (DoD).

## 2. Missions Concrètes Réalisées par le Prompt
1. Extraire les User Stories sélectionnées pour le sprint depuis le Product Backlog.
2. Décomposer chaque User Story en tâches techniques concrètes adaptées à la stack logicielle du projet.
3. Rédiger le document `sprint-backlog.md` avec matrice de suivi, estimation d'effort et checklist DoD face au Sprint Goal.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle (Persona) :** Scrum Master & Coach Agile senior expert en décomposition de tâches techniques et gouvernance Scrum.
- **Instruction (Contexte & Tâche) :** Prendre en entrée les User Stories retenues pour le sprint et produire la décomposition technique détaillée avec critères DoD bloquants.
- **Output (Format de sortie) :** Fichier Markdown structuré directement intégrable dans `scrum/sprint-backlog-[ID].md`.
- **Contraintes Négatives :**
  - Pas de tâches vagues ou génériques ; chaque tâche doit spécifier les fichiers cibles impactés.
  - Zéro tableau Markdown dans la décomposition.
  - Pas de bavardage conversationnel.

## 4. Livrables & Critères de validation
- **Livrable attendu :**
  - Fichier de prompt réutilisable : `tutoriels/realisation-projet/planification/prompt-engagement-equipe/prompt-sprint-planning.prompt.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le prompt est rédigé selon le formalisme RIO avec ses contraintes négatives explicites.
  - [ ] Testé avec une User Story d'application métier, il produit un découpage technique précis avec critères DoD.
  - [ ] Le document généré est immédiatement exploitable pour le suivi de sprint.
