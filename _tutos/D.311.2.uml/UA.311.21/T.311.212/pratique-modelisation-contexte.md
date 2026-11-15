---
layout: tuto
title: "Pratique : Modélisation du contexte"
sous_titre: "Construire le diagramme de contexte système Mermaid délimitant le Blog des Lauréats et ses acteurs"
slug: "pratique-modelisation-contexte"
permalink: /tutos/pratique-modelisation-contexte/
tuto_id: "T.311.212"
version: "normal"
ua: "UA.311.21"
maturite: "UA-Lab"
nav_order: 2
simplified: true
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Livrable Attendu
- `livrables/uml/diagramme-contexte.mmd` : Diagramme de contexte complet en syntaxe Mermaid.js.

## 2. Consignes & Jalons de Réalisation
Bâtir le diagramme de contexte en respectant ces 3 jalons :
1. **Identification des Acteurs :** Recenser au moins 2 profils d'utilisateurs humains primaires (Lecteur public, Lauréat), les acteurs secondaires (Modérateur, PO) et les services tiers (GitHub / Hébergement).
2. **Définition de la Boîte Noire :** Placer le *Blog des Lauréats* au centre du modèle.
3. **Modélisation des Flux :** Relier chaque acteur au système central avec des flux orientés et nommés explicitement.

## 3. Points de Vigilance
- ⚠️ Aucun flux ne doit relier directement deux acteurs externes entre eux (tous les flux transitent par le système).
- ⚠️ Le diagramme doit rester de niveau macroscopique sans détails de protocoles techniques (ex : pas de mention « TCP/IP »).

## 4. Critères de Validation
- [ ] Le fichier `livrables/uml/diagramme-contexte.mmd` est présent et s'affiche sans erreur de rendu sous Mermaid.
- [ ] La frontière système est clairement matérialisée.
- [ ] Tous les acteurs du brief projet sont représentés.
