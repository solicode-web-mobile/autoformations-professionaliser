---
layout: tuto
title: "Création du prompt-use-cases-macro"
sous_titre: "Concevoir le prompt d'ingénierie prompt-use-cases-macro pour automatiser la cartographie des cas d'utilisation"
slug: "prompt-use-cases"
slug_domaine: "uml"
slug_ua: "cas-utilisation"
permalink: /tutos/prompt-use-cases/
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

## 1. Travail à faire
Concevoir et tester le prompt d'ingénierie réutilisable nommé `prompt-use-cases-macro.prompt.md` selon la méthode RIO.

Ce prompt permet à un Agent IA d'extraire la cartographie des cas d'utilisation macro d'une application métier à partir de sa description fonctionnelle, et de générer directement le diagramme Mermaid `graph TD` avec ses dépendances d'inclusion et d'extension lors du Projet Fil Rouge.

## 2. Missions Concrètes Réalisées par le Prompt
1. Extraire la liste des fonctionnalités par profil utilisateur à partir de la description métier `[THEME_APPLICATION]`.
2. Déduire les cas d'utilisation macroscopiques en éliminant les micro-actions techniques (ex: pas d'étape "Cliquer sur un bouton").
3. Identifier les relations structurelles indispensables : inclusions obligatoires `<<include>>` et extensions conditionnelles `<<extend>>`.
4. Produire le code Mermaid.js (`graph TD`) prêt à être intégré dans un fichier `.mmd`.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle (Persona) :** Analyste fonctionnel senior expert en ingénierie des exigences et diagrammes UML.
- **Instruction (Contexte & Tâche) :** Prendre en entrée la liste des acteurs et les besoins fonctionnels de l'application métier pour déduire l'arborescence des cas d'utilisation macro et produire le code source Mermaid complet.
- **Output (Format de sortie) :** Bloc de code Mermaid pur débutant par `graph TD`.
- **Contraintes Négatives :**
  - Interdiction de générer un diagramme d'activité déguisé en cas d'utilisation (pas de séquence temporelle).
  - Zéro bavardage avant ou après le bloc Mermaid.
  - Zéro tableau Markdown.

## 4. Livrables & Critères de validation
- **Livrable attendu :**
  - Fichier de prompt réutilisable : `tutoriels/uml/cas-utilisation/prompt-use-cases/prompt-use-cases-macro.prompt.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le prompt applique la méthode RIO avec des contraintes négatives explicites.
  - [ ] Testé sur une application métier (ex : Plateforme Cinéma), il génère un diagramme `graph TD` complet et lisible.
  - [ ] Les relations structurelles `<<include>>` et `<<extend>>` sont correctement stéréotypées.
