---
layout: tuto
title: "Prompts & Skills : Contexte système Fil Rouge"
sous_titre: "Concevoir le prompt RIO réutilisable pour générer le diagramme de contexte sur l'application Fil Rouge"
slug: "prompts-skills-contexte-fil-rouge"
permalink: /tutos/prompts-skills-contexte-fil-rouge/
tuto_id: "T.311.213"
version: "normal"
ua: "UA.311.21"
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
- Transposition de l'Étape 2.1 (Frontières Système & Contexte) vers le Projet Fil Rouge (ex : Plateforme Cinéma).

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-diagramme-contexte.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de générer le diagramme de contexte Mermaid pour n'importe quelle application métier.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Analyste système senior expert en modélisation fonctionnelle et Mermaid.js.
- **Instruction :** Prendre en entrée la description de l'application métier `[THEME_APPLICATION]` et déduire les acteurs externes, les systèmes tiers et les flux d'échange pour produire le bloc `graph LR`.
- **Output :** Bloc de code Mermaid pur directement intégrable dans un fichier `.mmd`.
- **Contraintes Négatives :** Zéro explication textuelle avant ou après le bloc Mermaid.

## 4. Critères de Validation
- [ ] Le prompt est testé avec l'agent IA sur le thème du Projet Fil Rouge.
- [ ] Le code Mermaid généré est syntaxiquement valide et fidèlement aligné sur le domaine métier.
