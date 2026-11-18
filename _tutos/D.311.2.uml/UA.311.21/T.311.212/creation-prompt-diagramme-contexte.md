---
layout: tuto
title: "Création du prompt-diagramme-contexte"
sous_titre: "Concevoir le prompt prompt-diagramme-contexte pour automatiser la modélisation du contexte système"
slug: "prompt-generation"
slug_domaine: "uml"
slug_ua: "diagramme-contexte"
permalink: /tutos/prompt-generation/
tuto_id: "T.311.212"
version: "normal"
ua: "UA.311.21"
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
- **Position dans le flux :** Phase B — Analyse, Conception & Planification / Étape 2.1 — Automatisation du Contexte.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-diagramme-contexte.prompt.md`

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-diagramme-contexte.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de générer le diagramme de contexte Mermaid pour n'importe quelle application métier.

## 3. Missions Concrètes Réalisées par le Prompt
1. Analyser la description textuelle d'une application métier et en extraire les acteurs primaires, secondaires et systèmes tiers.
2. Déterminer les frontières fonctionnelles et les flux d'échange bidirectionnels.
3. Générer le code source Mermaid.js (`graph LR`) prêt à être intégré dans un fichier `.mmd`.

## 4. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Analyste système senior expert en modélisation fonctionnelle et Mermaid.js.
- **Instruction :** Prendre en entrée la description de l'application métier `[THEME_APPLICATION]` et déduire les acteurs externes, les systèmes tiers et les flux d'échange pour produire le bloc `graph LR`.
- **Output :** Bloc de code Mermaid pur directement intégrable dans un fichier `.mmd`.
- **Contraintes Négatives :** Zéro explication textuelle avant ou après le bloc Mermaid.

## 5. Critères de Validation
- [ ] Le prompt est testé et sauvegardé dans `livrables/ia/prompts/prompt-diagramme-contexte.prompt.md` sur la branche `sprint1`.
- [ ] Il génère un diagramme de contexte syntaxiquement valide en syntaxe `graph LR`.