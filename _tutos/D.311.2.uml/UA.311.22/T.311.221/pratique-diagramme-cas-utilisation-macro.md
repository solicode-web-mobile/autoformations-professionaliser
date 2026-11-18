---
layout: tuto
title: "Pratique : Diagramme de cas d'utilisation macro"
sous_titre: "Modéliser les 15 cas d'utilisation macro du Blog des Lauréats avec relations structurelles en Mermaid"
slug: "modelisation-macro"
slug_domaine: "uml"
slug_ua: "cas-utilisation"
permalink: /tutos/modelisation-macro/
tuto_id: "T.311.221"
version: "normal"
ua: "UA.311.22"
maturite: "UA-Lab"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase B — Analyse, Conception & Planification / Étape 2.4 — Cartographie des Cas d'Utilisation Macro.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/uml/use-cases-macro.mmd`
- **Stack mobilisée :** Mermaid.js, Use Cases UML, Relations structurelles (`<<include>>`, `<<extend>>`).

## 2. Travail à Faire (Projet d'Imitation)
Bâtir le diagramme de cas d'utilisation macro en respectant ces jalons :
1. **Cartographie des 15 UCs :** Identifier les cas d'utilisation couvrant l'espace public (consultation, lecture), l'espace lauréat (rédaction, publication) et la modération.
2. **Association Acteurs-UCs :** Relier chaque acteur à ses cas d'utilisation respectifs.
3. **Formalisation des Relations Structurelles :** Positionner les dépendances obligatoires (`<<include>>`) et conditionnelles (`<<extend>>`).

## 3. Critères de Validation
- [ ] Le fichier `livrables/uml/use-cases-macro.mmd` est versionné sur la branche `sprint1`.
- [ ] L'ensemble des 15 cas d'utilisation de l'application y figurent de manière lisible.
- [ ] La syntaxe Mermaid `graph TD` est propre et sans avertissement.