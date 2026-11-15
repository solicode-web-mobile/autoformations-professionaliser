---
layout: tuto
title: "Création du prompt-use-cases-macro"
sous_titre: "Concevoir le prompt prompt-use-cases-macro pour automatiser la cartographie des cas d'utilisation"
slug: "creation-prompt-use-cases-macro"
permalink: /tutos/creation-prompt-use-cases-macro/
tuto_id: "T.311.222"
version: "normal"
ua: "UA.311.22"
maturite: "UA-Lab"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase B — Analyse, Conception & Planification / Étape 2.4 — Automatisation des Cas d'Utilisation.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-use-cases-macro.prompt.md`

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-use-cases-macro.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de produire le diagramme de cas d'utilisation macro avec relations structurelles.

## 3. Missions Concrètes Réalisées par le Prompt
1. Extraire la liste des fonctionnalités et des profils utilisateurs depuis le Product Backlog.
2. Déduire les cas d'utilisation à granularité macroscopique en éliminant la sur-segmentation technique.
3. Identifier et relier les relations `<<include>>` et `<<extend>>`.
4. Produire le code Mermaid.js (`graph TD`) complet.

## 4. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Analyste fonctionnel senior expert en ingénierie des exigences et diagrammes UML.
- **Instruction :** Prendre en entrée la liste des acteurs et les fonctionnalités du carnet produit pour déduire l'arborescence des cas d'utilisation avec relations structurelles.
- **Output :** Bloc de code Mermaid `graph TD` prêt pour un fichier `.mmd`.
- **Contraintes Négatives :** Pas de diagramme d'activité déguisé en use case, pas de micro-actions techniques.

## 5. Critères de Validation
- [ ] Le prompt est testé et consigné dans `livrables/ia/prompts/prompt-use-cases-macro.prompt.md` sur la branche `sprint1`.
- [ ] Il génère une cartographie complète et lisible conforme aux standards UML.