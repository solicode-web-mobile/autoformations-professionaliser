---
layout: tuto
title: "Création du prompt-product-backlog"
sous_titre: "Concevoir le prompt d'ingénierie prompt-product-backlog pour découper et prioriser le carnet de produit"
slug: "prompt-user-stories"
slug_domaine: "scrum"
slug_ua: "product-backlog"
permalink: /tutos/prompt-user-stories/
tuto_id: "T.351.123"
version: "normal"
ua: "UA.351.12"
maturite: "UA-Lab"
nav_order: 3
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase B — Analyse, Conception & Planification / Étape 2.2 — Automatisation du Backlog.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-product-backlog.prompt.md`

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-product-backlog.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de transformer un cahier des charges textuel en un Product Backlog structuré selon la méthode INVEST et priorisé en MoSCoW.

## 3. Missions Concrètes Réalisées par le Prompt
1. Extraire les besoins fonctionnels bruts d'une application métier.
2. Structurer chaque exigence en User Story INVEST avec persona cible, intention et bénéfice.
3. Rédiger les critères d'acceptation vérifiables (Gherkin ou liste à puces).
4. Appliquer la classification MoSCoW (Must, Should, Could, Won't).

## 4. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Product Owner senior expert en découpage agile INVEST et classification MoSCoW.
- **Instruction :** Prendre en entrée la description des fonctionnalités métier `[THEME_APPLICATION]` et produire le carnet de produit structuré en tableau Markdown.
- **Output :** Tableau Markdown propre avec colonnes : ID, Titre, En tant que, Je veux, Afin de, Priorité MoSCoW, Critères d'acceptation.
- **Contraintes Négatives :** Zéro tâches techniques (ex : pas de « créer la migration BDD » comme Story), uniquement des tranches verticales observables par l'utilisateur.

## 5. Critères de Validation
- [ ] Le prompt est consigné dans `livrables/ia/prompts/prompt-product-backlog.prompt.md` sur la branche `sprint1`.
- [ ] Il génère un carnet produit immédiatement exploitable pour le sprint.