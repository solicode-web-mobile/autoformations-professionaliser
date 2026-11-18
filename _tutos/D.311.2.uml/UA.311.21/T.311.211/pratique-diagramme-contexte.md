---
layout: tuto
title: "Pratique : Diagramme de contexte système"
sous_titre: "Délimiter les frontières fonctionnelles du Blog des Lauréats et cartographier les interactions externes en Mermaid"
slug: "modelisation-systeme"
slug_domaine: "uml"
slug_ua: "diagramme-contexte"
permalink: /tutos/modelisation-systeme/
tuto_id: "T.311.211"
version: "normal"
ua: "UA.311.21"
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
- **Position dans le flux :** Phase B — Analyse, Conception & Planification / Étape 2.1 — Frontières Système & Contexte.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/uml/diagramme-contexte.mmd`
- **Stack mobilisée :** Mermaid.js, Syntaxe déclarative Markdown, Diagramme de contexte système.

## 2. Travail à Faire (Projet d'Imitation)
Bâtir le diagramme de contexte système en respectant ces jalons :
1. **Identification des Acteurs :** Recenser au moins 2 profils d'utilisateurs humains primaires (Lecteur public, Lauréat), les acteurs secondaires (Modérateur, PO) et les services tiers (GitHub / Hébergement).
2. **Définition de la Boîte Noire :** Placer le *Blog des Lauréats* au centre du modèle.
3. **Modélisation des Flux :** Relier chaque acteur au système central avec des flux orientés et nommés explicitement en syntaxe `graph LR`.

## 3. Critères de Validation
- [ ] Le fichier `livrables/uml/diagramme-contexte.mmd` est présent et versionné sur la branche `sprint1`.
- [ ] La frontière système est clairement matérialisée (aucun flux direct entre deux acteurs externes).
- [ ] Le diagramme s'affiche sans erreur de rendu sous Mermaid.