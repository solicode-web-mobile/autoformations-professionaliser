---
layout: tuto
title: "Prompts & Skills : Méta-prompt Fil Rouge"
sous_titre: "Concevoir le méta-prompt prompt-creator pour automatiser la génération des prompts Fil Rouge"
slug: "prompts-skills-meta-prompt-fil-rouge"
permalink: /tutos/prompts-skills-meta-prompt-fil-rouge/
tuto_id: "T.325.113"
version: "normal"
ua: "UA.325.11"
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
- Transposition de l'Étape 1.3 (Outillage Prompt Engineering) vers la chaîne d'outillage transverse du Projet Fil Rouge.

## 2. Travail à Faire
Concevoir et tester dans `livrables/ia/prompt-creator.prompt.md` le méta-prompt officiel permettant à l'agent IA de générer, sur simple description d'un besoin, le prompt RIO complet et contextualisé pour chaque étape future du Projet Fil Rouge.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Expert senior en Prompt Engineering et architecture logicielle pour développeurs augmentés.
- **Instruction :** Prendre en entrée la description d'une tâche d'ingénierie logicielle et produire un prompt directif structuré en Rôle / Contexte / Instructions pas-à-pas / Contraintes négatives / Format de sortie.
- **Output :** Bloc Markdown contenant le prompt prêt à être enregistré dans un fichier `*.prompt.md`.
- **Contraintes Négatives :** Le méta-prompt ne doit pas exécuter la tâche lui-même ; il doit **produire le prompt** qui permettra d'exécuter la tâche.

## 4. Critères de Validation
- [ ] Le fichier `livrables/ia/prompt-creator.prompt.md` est présent et testé.
- [ ] Soumis à une tâche test (ex: « Générer un diagramme de séquence »), il produit un prompt RIO complet, testable et conforme aux standards de la promotion.
