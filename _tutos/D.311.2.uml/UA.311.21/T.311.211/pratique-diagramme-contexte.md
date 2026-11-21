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
maturite: "lab"
type: "tuto-atelier"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
Délimiter les frontières fonctionnelles du *Blog des Lauréats* et modéliser en syntaxe déclarative Mermaid.js son diagramme de contexte système, à partir des acteurs et du périmètre contractualisés lors du cadrage (`UA.351.21`).

Vous devez concevoir :
1. Le fichier source Mermaid du diagramme de contexte : `diagramme-contexte.mmd`.
2. La fiche technique d'analyse de contexte : `modelisation-systeme.md`.
3. Le diaporama Marp de restitution technique : `presentation-modelisation-systeme.md`.

## 2. Consignes & Spécifications de Réalisation

1. **Étape 1 — Identification des Acteurs Externes :**  
   Recensez les profils d'utilisateurs humains identifiés lors du cadrage :
   - *Acteurs primaires :* L'Apprenant ou le Visiteur public (consommateur des articles en S1) et le Lauréat (futur rédacteur d'articles).
   - *Acteur secondaire :* Le Modérateur (supervision des contenus).
   - *Système tiers :* Le service d'hébergement ou dépôt Git.

2. **Étape 2 — Modélisation de la Boîte Noire Système :**  
   Positionnez le *Blog des Lauréats* au centre du modèle en tant que boîte noire. Le diagramme de contexte ne détaille pas la cuisine interne de l'application (pas de classes, pas de bases de données internes).

3. **Étape 3 — Définition des Flux Orientés :**  
   Reliez chaque acteur au système central avec des flux orientés et nommés explicitement en syntaxe Mermaid `graph LR` (consultation d'un article, lecture des profils, soumission de réalisations).  
   *Règle d'or :* Il est strictement interdit d'établir un flux direct entre deux acteurs externes ; tout échange transite obligatoirement par le système central.

4. **Étape 4 — Préparation du Diaporama Marp :**  
   Concevez le diaporama `presentation-modelisation-systeme.md` au format Marp Markdown pour présenter oralement les frontières de l'application et justifier les flux modélisés.

## 3. Livrables & Critères de validation
- **Livrables attendus :**
  - Diagramme Mermaid : `tutoriels/uml/diagramme-contexte/modelisation-systeme/diagramme-contexte.mmd` sur la branche `sprint1`.
  - Fiche technique : `tutoriels/uml/diagramme-contexte/modelisation-systeme/modelisation-systeme.md` sur la branche `sprint1`.
  - Diaporama Marp : `tutoriels/uml/diagramme-contexte/modelisation-systeme/presentation-modelisation-systeme.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le fichier `diagramme-contexte.mmd` est syntaxiquement valide sous Mermaid.js en orientation `graph LR`.
  - [ ] La frontière système est clairement matérialisée avec le Blog des Lauréats au centre.
  - [ ] Les acteurs primaires (*Lauréat*, *Apprenant/Visiteur*) et secondaires sont fidèlement représentés.
  - [ ] Aucun flux direct ne relie deux acteurs externes.
  - [ ] Le diaporama Marp respecte les standards de présentation Solicode (zéro tableau Markdown).
