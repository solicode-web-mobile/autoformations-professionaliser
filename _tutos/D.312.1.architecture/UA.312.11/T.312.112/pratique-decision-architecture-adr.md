---
layout: tuto
title: "Pratique : Décision d'architecture (ADR-01) & Diagramme de séquence"
sous_titre: "Formaliser le choix d'architecture 2 couches avec persistance CSV et modéliser le flux HTTP sous Mermaid"
slug: "decision-adr-sequence"
slug_domaine: "architecture"
slug_ua: "deux-couches"
permalink: /tutos/decision-adr-sequence/
tuto_id: "T.312.112"
version: "normal"
ua: "UA.312.11"
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
- **Position dans le flux :** Phase B — Analyse, Conception & Planification / Étape 3.1 — Rédaction ADR & Séquence.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/architecture/architecture-sprint1.md`
- **Stack mobilisée :** Architecture 2 couches, Mermaid.js (sequenceDiagram), ADR-01.

## 2. Travail à Faire (Projet d'Imitation)
Bâtir le livrable d'architecture en respectant ces jalons :
1. **Rédaction de l'ADR-01 :** Documenter le choix de l'architecture 2 couches avec persistance tabulaire CSV (`database/data/articles.csv`) pour amorcer le Sprint 1 sans dépendance SGBD.
2. **Analyse d'Impact & Conséquences :** Lister les bénéfices (rapidité d'amorçage, simplicité, testabilité) et les contraintes acceptées (pas de transactions SQL, volumétrie limitée).
3. **Modélisation de la Séquence HTTP :** Rédiger le diagramme `sequenceDiagram` décrivant l'enchaînement : Client $\to$ `routes/web.php` $\to$ `ArticleController` $\to$ `ArticleService` $\to$ Vue Blade (cas nominal 200 et cas d'exception 404).

## 3. Critères de Validation
- [ ] Le fichier `livrables/architecture/architecture-sprint1.md` existe et adopte le formalisme canonique ADR sur la branche `sprint1`.
- [ ] Le diagramme de séquence Mermaid compile sans avertissement et illustre le cas nominal ainsi que l'exception 404.
- [ ] L'isolation entre contrôleur mince et classe service est formellement garantie.