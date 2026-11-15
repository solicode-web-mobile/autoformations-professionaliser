---
layout: tuto
title: "Prompts & Skills : Cas d'utilisation Fil Rouge"
sous_titre: "Concevoir le prompt RIO réutilisable pour déduire la cartographie des cas d'utilisation Fil Rouge"
slug: "prompts-skills-cas-utilisation-fil-rouge"
permalink: /tutos/prompts-skills-cas-utilisation-fil-rouge/
tuto_id: "T.311.223"
version: "normal"
ua: "UA.311.22"
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
- Transposition de l'Étape 2.4 (Cartographie des Cas d'Utilisation Macro) vers le Projet Fil Rouge (ex : Plateforme Cinéma).

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-use-cases-macro.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de produire le diagramme de cas d'utilisation macro pour le Projet Fil Rouge.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Analyste fonctionnel senior expert en ingénierie des exigences et diagrammes UML.
- **Instruction :** Prendre en entrée la liste des acteurs et les fonctionnalités du carnet produit Fil Rouge pour déduire l'arborescence des cas d'utilisation avec relations `<<include>>` et `<<extend>>`.
- **Output :** Bloc de code Mermaid `graph TD` prêt pour un fichier `.mmd`.
- **Contraintes Négatives :** Pas de diagramme d'activité déguisé en use case, pas de micro-actions techniques.

## 4. Critères de Validation
- [ ] Le prompt est testé sur le thème de l'application Fil Rouge.
- [ ] Le diagramme généré traduit fidèlement les interactions des utilisateurs avec le système métier.
