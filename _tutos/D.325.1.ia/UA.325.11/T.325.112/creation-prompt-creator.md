---
layout: tuto
title: "Création du prompt-creator"
sous_titre: "Concevoir le méta-prompt prompt-creator pour automatiser la génération des prompts du sprint"
slug: "creation-prompt-creator"
permalink: /tutos/creation-prompt-creator/
tuto_id: "T.325.112"
version: "normal"
ua: "UA.325.11"
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
- **Position dans le flux :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 1.1 — Méta-Prompt Générateur.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-creator.prompt.md`

## 2. Travail à Faire
Concevoir, tester et valider dans `livrables/ia/prompts/prompt-creator.prompt.md` le méta-prompt officiel permettant à l'agent IA de générer, sur simple description d'un besoin de tâche, le prompt RIO complet et contextualisé pour chaque étape future du sprint.

## 3. Missions Concrètes Réalisées par le Prompt
1. Analyser une consigne brute de tâche ou d'exigence logicielle.
2. Structurer le prompt selon le formalisme RIO (Rôle expert, Intention opérationnelle fermée, Output délimité).
3. Injecter les contraintes négatives bloquantes (zéro bavardage de politesse, code exécutable complet sans omission, chemins relatifs stricts).
4. Produire un fichier `.prompt.md` prêt à l'emploi.

## 4. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Métaprompt Engineer expert en systèmes multi-agents et architecture logicielle.
- **Instruction :** Prendre en entrée la description d'une tâche d'ingénierie logicielle et produire un prompt directif structuré en Rôle / Contexte / Instructions pas-à-pas / Contraintes négatives / Format de sortie.
- **Output :** Bloc Markdown contenant le prompt prêt à être enregistré dans un fichier `*.prompt.md`.
- **Contraintes Négatives :** Le méta-prompt ne doit pas exécuter la tâche lui-même ; il doit produire le prompt qui permettra d'exécuter la tâche.

## 5. Critères de Validation
- [ ] Le fichier `livrables/ia/prompts/prompt-creator.prompt.md` est présent et versionné sur la branche `sprint1`.
- [ ] Soumis à une consigne brute de test, il génère un prompt RIO complet, testable et conforme aux standards de la promotion.