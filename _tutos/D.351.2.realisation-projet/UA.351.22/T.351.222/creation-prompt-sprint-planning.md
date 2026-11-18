---
layout: tuto
title: "Création du prompt-sprint-planning"
sous_titre: "Concevoir le prompt prompt-sprint-planning pour automatiser la décomposition des User Stories en tâches de sprint"
slug: "prompt-engagement-equipe"
slug_domaine: "realisation-projet"
slug_ua: "planification"
permalink: /tutos/prompt-engagement-equipe/
tuto_id: "T.351.222"
version: "normal"
ua: "UA.351.22"
maturite: "UA-Tâche"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif Opérationnel & Prérequis
- **Position dans le flux :** Phase B — Analyse Fonctionnelle, Backlog & Planification de Sprint / Étape 7 — Automatisation de la Planification.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-sprint-planning.prompt.md`
- **Objectif :** Concevoir le prompt d'ingénierie réutilisable permettant à un agent IA de générer le Sprint Backlog découpé à partir d'une sélection de User Stories.

## 2. Missions Concrètes Réalisées par le Prompt
1. Extraire les User Stories sélectionnées pour le sprint depuis le Product Backlog.
2. Décomposer chaque User Story en tâches techniques concrètes selon la stack du projet.
3. Rédiger le document `sprint-backlog.md` avec matrice de suivi et checklist DoD.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Scrum Master & Coach Agile senior expert en décomposition de tâches techniques.
- **Instruction :** Prendre en entrée les User Stories retenues et produire la décomposition technique détaillée avec critères DoD.
- **Output :** Fichier Markdown structuré directement intégrable dans `scrum/sprint-backlog-[ID].md`.
- **Contraintes Négatives :** Pas de tâches vagues ou génériques ; chaque tâche doit spécifier les fichiers cibles impactés.

## 4. Critères de Validation
- [ ] Le fichier `livrables/ia/prompts/prompt-sprint-planning.prompt.md` est testé et versionné sur la branche `sprint1`.
- [ ] Il génère une décomposition technique rigoureuse prête pour le suivi de sprint.