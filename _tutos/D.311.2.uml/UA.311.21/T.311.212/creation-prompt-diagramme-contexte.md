---
layout: tuto
title: "Création du prompt-diagramme-contexte"
sous_titre: "Concevoir le prompt d'ingénierie prompt-diagramme-contexte pour automatiser la modélisation du contexte système"
slug: "prompt-generation"
slug_domaine: "uml"
slug_ua: "diagramme-contexte"
permalink: /tutos/prompt-generation/
tuto_id: "T.311.212"
version: "normal"
ua: "UA.311.21"
maturite: "lab"
type: "tuto-atelier"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
Concevoir et tester le prompt d'ingénierie réutilisable nommé `prompt-diagramme-contexte.prompt.md` selon la méthode RIO.

Ce prompt est un composant agentique réutilisable permettant à un Agent IA de générer automatiquement le diagramme de contexte Mermaid (`graph LR`) pour n'importe quelle application métier lors du Projet Fil Rouge.

## 2. Missions Concrètes Réalisées par le Prompt
1. Analyser la description fonctionnelle textuelle d'une application métier `[THEME_APPLICATION]`.
2. Identifier les acteurs primaires, les acteurs secondaires et les systèmes tiers.
3. Délimiter les frontières de la boîte noire système et formaliser les flux d'échange bidirectionnels.
4. Produire le code source Mermaid.js (`graph LR`) directement prêt à être injecté dans un fichier `.mmd`.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle (Persona) :** Analyste système senior expert en modélisation fonctionnelle et syntaxe déclarative Mermaid.js.
- **Instruction (Contexte & Tâche) :** Prendre en entrée la description de l'application métier cible et construire le diagramme de contexte en respectant rigoureusement les conventions UML (système au centre, acteurs autour, flux orientés et nommés).
- **Output (Format de sortie) :** Bloc de code Mermaid pur débutant par `graph LR`.
- **Contraintes Négatives :**
  - Interdiction d'ajouter du texte d'introduction, de conclusion ou de bavardage conversationnel.
  - Interdiction de relier directement deux acteurs externes entre eux.
  - Zéro tableau Markdown dans la restitution.

## 4. Livrables & Critères de validation
- **Livrable attendu :**
  - Fichier de prompt réutilisable : `tutoriels/uml/diagramme-contexte/prompt-generation/prompt-diagramme-contexte.prompt.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le prompt est rédigé selon le formalisme RIO avec ses contraintes négatives explicites.
  - [ ] Testé avec un exemple d'application métier (ex : Plateforme Cinéma), il génère un bloc Mermaid `graph LR` syntaxiquement valide.
  - [ ] Le code produit s'intègre directement sans retouche manuelle.
