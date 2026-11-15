---
layout: tuto
title: "Pratique : Modélisation des cas d'utilisation"
sous_titre: "Cartographier les 15 cas d'utilisation du Blog des Lauréats en syntaxe Mermaid avec relations structurelles"
slug: "pratique-modelisation-cas-utilisation"
permalink: /tutos/pratique-modelisation-cas-utilisation/
tuto_id: "T.311.222"
version: "normal"
ua: "UA.311.22"
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
- `livrables/uml/use-cases-macro.mmd` : Diagramme des cas d'utilisation macro de l'application de référence.

## 2. Consignes & Jalons de Réalisation
Bâtir le diagramme en respectant ces 3 jalons :
1. **Cartographie des 15 UCs :** Identifier les cas d'utilisation couvrant l'espace public (consultation, lecture), l'espace lauréat (rédaction, publication) et l'espace modération.
2. **Association Acteurs-UCs :** Relier chaque acteur à ses cas d'utilisation respectifs.
3. **Formalisation des Relations Structurelles :** Positionner les dépendances obligatoires (`<<include>>`, ex: authentification) et optionnelles (`<<extend>>`).

## 3. Points de Vigilance
- ⚠️ Ne pas confondre une relation `<<include>>` avec un simple appel de sous-programme.
- ⚠️ Respecter la matrice de traçabilité avec les PBIs du Product Backlog.

## 4. Critères de Validation
- [ ] Le fichier `livrables/uml/use-cases-macro.mmd` est présent et versionné sous Git.
- [ ] L'ensemble des 15 cas d'utilisation du projet de référence y figurent de manière lisible.
- [ ] La syntaxe Mermaid est propre et sans avertissement de compilation.
