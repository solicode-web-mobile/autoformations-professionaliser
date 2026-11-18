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

## 1. Travail à faire
Concevoir et tester la suite de 4 prompts d'ingénierie réutilisables selon la méthode RIO pour automatiser la production des livrables de cérémonies de clôture de sprint sur le Projet Fil Rouge :
1. `prompt-sprint-review.prompt.md`
2. `prompt-sprint-retrospective.prompt.md`
3. `prompt-backlog-refinement.prompt.md`
4. `prompt-bilan-session.prompt.md`

## 2. Missions Concrètes Réalisées par les 4 Prompts
1. **`prompt-sprint-review` :** Prendre en entrée la liste des User Stories livrées et générer le procès-verbal de démonstration avec la grille d'évaluation DoD.
2. **`prompt-sprint-retrospective` :** Guider l'animation de la rétrospective, structurer les forces et axes de progrès, et acter le constat de dette d'empathie utilisateur.
3. **`prompt-backlog-refinement` :** Mettre à jour l'état des items terminés et structurer les critères d'acceptation du sprint suivant.
4. **`prompt-bilan-session` :** Générer le canevas de débriefing individuel et la matrice de progression sur les compétences du référentiel.

## 3. Cahier des Charges des Prompts (Méthode RIO)
- **Rôle (Persona) :** Scrum Master, Facilitateur Agile & Coach Pédagogique senior.
- **Instruction (Contexte & Tâche) :** Prendre en entrée les artefacts du sprint et produire les documents de clôture au format Markdown rigoureusement structuré.
- **Output (Format de sortie) :** Fichiers Markdown prêts à être commités sous `scrum/`.
- **Contraintes Négatives :**
  - Zéro bavardage conversationnel.
  - Zéro tableau Markdown.
  - Pas de texte générique : chaque document généré doit citer nommément les entités et fichiers du projet.

## 4. Livrables & Critères de validation
- **Livrables attendus :**
  - Suite de 4 prompts réutilisables dans `tutoriels/realisation-projet/cloture-sprint/prompts-ceremonies-bilan/` :
    - `prompt-sprint-review.prompt.md`
    - `prompt-sprint-retrospective.prompt.md`
    - `prompt-backlog-refinement.prompt.md`
    - `prompt-bilan-session.prompt.md`
- **Critères de validation :**
  - [ ] Les 4 fichiers de prompts adoptent le formalisme RIO avec leurs contraintes négatives explicites.
  - [ ] Testés avec un scénario de sprint d'application métier, ils produisent des documents Markdown directement exploitables.
