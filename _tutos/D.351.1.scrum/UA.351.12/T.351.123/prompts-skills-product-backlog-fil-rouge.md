---
layout: tuto
title: "Prompts & Skills : Product Backlog Fil Rouge"
sous_titre: "Concevoir le prompt RIO réutilisable pour générer le Product Backlog tabulaire du Projet Fil Rouge"
slug: "prompts-skills-product-backlog-fil-rouge"
permalink: /tutos/prompts-skills-product-backlog-fil-rouge/
tuto_id: "T.351.123"
version: "normal"
ua: "UA.351.12"
maturite: "UA-Lab"
nav_order: 3
simplified: true
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'Étape 2.2 (Découpage User Stories & Product Backlog) vers l'application métier Fil Rouge (ex : Plateforme Cinéma).

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-product-backlog.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de produire le Product Backlog complet et ordonné pour le Projet Fil Rouge.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Product Owner senior expert en analyse de la valeur et backlog grooming agile.
- **Instruction :** Prendre en entrée le thème du Projet Fil Rouge `[THEME_PROJET]` et la liste des acteurs identifiés pour générer un Product Backlog tabulaire complet (10 à 15 User Stories, critères d'acceptation, points Fibonacci et priorité MoSCoW).
- **Output :** Tableau Markdown directement intégrable dans le carnet agile du projet Fil Rouge.
- **Contraintes Négatives :** Pas de saucissonnage horizontal, pas de formulations techniques hors User Story.

## 4. Critères de Validation
- [ ] Le prompt est testé avec l'agent IA sur le contexte de l'application Fil Rouge.
- [ ] Le backlog généré couvre l'ensemble des parcours utilisateurs du projet avec une priorisation cohérente.
