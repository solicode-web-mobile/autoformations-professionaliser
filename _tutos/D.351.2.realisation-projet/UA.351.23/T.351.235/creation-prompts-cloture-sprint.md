---
layout: tuto
title: "Création des 4 prompts de clôture de sprint"
sous_titre: "Concevoir les prompts automatisant les livrables de Sprint Review, Retrospective, Refinement et Bilan"
slug: "prompts-ceremonies-bilan"
slug_domaine: "realisation-projet"
slug_ua: "cloture-sprint"
permalink: /tutos/prompts-ceremonies-bilan/
tuto_id: "T.351.235"
version: "normal"
ua: "UA.351.23"
maturite: "UA-Tâche"
nav_order: 5
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif Opérationnel & Prérequis
- **Position dans le flux :** Phase D — Clôture de Sprint, Rétrospective & Bilan / Étape 5.5 — Automatisation des Rituels de Clôture.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :**
  - `livrables/ia/prompts/prompt-sprint-review.prompt.md`
  - `livrables/ia/prompts/prompt-sprint-retrospective.prompt.md`
  - `livrables/ia/prompts/prompt-backlog-refinement.prompt.md`
  - `livrables/ia/prompts/prompt-bilan-session.prompt.md`
- **Objectif :** Concevoir les 4 prompts d'ingénierie réutilisables automatisant la production des livrables pour chacune des cérémonies de clôture de sprint.

## 2. Missions Concrètes des 4 Prompts Réalisés
1. **`prompt-sprint-review` :** Générer le procès-verbal de démonstration et la grille d'audit de la DoD à partir des fonctionnalités livrées sur le sprint.
2. **`prompt-sprint-retrospective` :** Guider l'animation de la rétrospective agile, structurer la collecte des forces/axes d'amélioration et synthétiser les décisions concrètes d'équipe.
3. **`prompt-backlog-refinement` :** Analyser le Product Backlog, actualiser les statuts des User Stories livrées et ré-estimer/réordonner les items prioritaires pour le sprint suivant.
4. **`prompt-bilan-session` :** Générer le canevas de débriefing individuel réflexif et la matrice de positionnement sur les compétences techniques mobilisées.

## 3. Critères de Validation
- [ ] Les 4 fichiers de prompts sont créés dans `livrables/ia/prompts/` et versionnés sur la branche `sprint1`.
- [ ] Chaque prompt adopte la méthode RIO avec contraintes négatives strictes.